import dearpygui.dearpygui as dpg
import ipget
from PIL import Image


def imgshow(self):
    imgPIL = Image.open(ipget.imageinput())
    imgPIL.show()


dpg.create_context()

with dpg.font_registry():
    with dpg.font(file="./resources/NotoSansJP-Medium.otf", size=20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
    dpg.bind_font(default_font)
    with dpg.font(file="./resources/NotoSansJP-Bold.otf", size=14) as small_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)

with dpg.window(label="追加", collapsed=False, no_close=True):
    dpg.add_text("PDFレポート作成")
    dpg.add_button("画像を確認", callback=imgshow)

with dpg.window(label="貴方の情報", collapsed=False, no_close=True):
    dpg.add_text("グローバルIPアドレス:" + ipget.get_gip_addr())
    dpg.add_text("コンピュータ名:" + ipget.get_host())

dpg.create_viewport(title=f"Ragnarok", width=640, height=480)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
