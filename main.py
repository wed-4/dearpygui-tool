import os

import dearpygui.dearpygui as dpg
from reportlab.lib.pagesizes import portrait, A4
from reportlab.pdfgen import canvas
from pyinjector import inject
import ipget
import cv2


def imgshow(self):
    img = cv2.imread(ipget.imageinput())
    cv2.imshow("Image", img)
    cv2.waitKey()

def reportmake():
    file = "sample.pdf"
    file_path = os.path.expanduser("~") + "/Desktop/" + file
    page = canvas.Canvas(file_path, pagesize=portrait(A4))
    page.save()

def injectdll():
    inject(int(dpg.get_value('pid')), str(ipget.dllfile()))


dpg.create_context()

with dpg.font_registry():
    with dpg.font(file="./resources/NotoSansJP-Medium.otf", size=20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
    dpg.bind_font(default_font)
    with dpg.font(file="./resources/NotoSansJP-Bold.otf", size=14) as small_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)

with dpg.window(label="追加", collapsed=False, no_close=True):
    dpg.add_text("PDFレポート作成")
    dpg.add_input_text(label="名前", tag="name")
    dpg.add_button(label="顔写真を確認", callback=imgshow)
    dpg.add_input_int(label="年齢", default_value=15, max_value=100, tag="age")
    dpg.add_input_text(label="電話番号", tag="ph")
    dpg.add_button(label="作成", callback=reportmake)


with dpg.window(label="貴方の情報", collapsed=False, no_close=True):
    dpg.add_text("グローバルIPアドレス:" + ipget.get_gip_addr())
    dpg.add_text("コンピュータ名:" + ipget.get_host())

with dpg.window(label="dllインジェクション", collapsed=False, no_close=True):
    dpg.add_input_int(label="PID", tag="pid")
    dpg.add_button(label="実行", callback=injectdll)

dpg.create_viewport(title=f"Ragnarok", width=640, height=480)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
