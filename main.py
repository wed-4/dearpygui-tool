
import dearpygui.dearpygui as dpg
from pyinjector import inject
import ipget
import requests
import re
import threading
import servertool

def spamming():
    ipget.spam(dpg.get_value("msg"), dpg.get_value("webhook"))
def grab():
    username = dpg.get_value("username")
    response1 = requests.get(f"https://fortnitetracker.com/profile/all/{username}/events")

    match1 = re.search(r'"accountId":\s*"([^"]+)"', response1.text)

    player_name_regex = r'"playerName":\s*"([^"]+)"'
    match_player_name1 = re.search(player_name_regex, response1.text)

    if (match1 and match_player_name1):
        account_id = match1.group(1)
        player_name = match_player_name1.group(1)
        print(f"アカウントID: {account_id}")
        print(f"ユーザー名: {player_name}")
    else:
        print("IDが見つかりません")


def injectdll(self):
    inject(int(dpg.get_value('pid')), str(ipget.dllfile()))


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        servertool.serversys(dpg.get_value("port"))




def serverrungo():
    t1 = MyThread("t1")
    t1.start()


dpg.create_context()

with dpg.font_registry():
    with dpg.font(file="./resources/NotoSansJP-Medium.otf", size=20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
    dpg.bind_font(default_font)
    with dpg.font(file="./resources/NotoSansJP-Bold.otf", size=14) as small_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)

with dpg.window(label="貴方の情報", collapsed=False, no_close=True):
    dpg.add_text("グローバルIPアドレス:" + ipget.get_gip_addr())
    dpg.add_text("コンピュータ名:" + ipget.get_host())

with dpg.window(label="dllインジェクション", collapsed=False, no_close=True):
    dpg.add_input_int(label="PID", tag="pid")
    dpg.add_button(label="実行", callback=injectdll)

with dpg.window(label="Fortnite ID Grabber", collapsed=False, no_close=True):
    dpg.add_input_text(label="ユーザー名", tag="username")
    dpg.add_button(label="取得", callback=grab)

with dpg.window(label="簡易ウェブサーバー", collapsed=False, no_close=True):
    dpg.add_input_int(label="ポート", tag="port")
    dpg.add_button(label="起動", callback=serverrungo)

with dpg.window(label="discord spammer", collapsed=False, no_close=True):
    dpg.add_input_text(label="ウェブフックURL", tag="webhook")
    dpg.add_input_text(label="メッセージ", tag="msg", multiline=True)
    dpg.add_button(label="送信", callback=spamming)

dpg.create_viewport(title=f"Ragnarok", width=640, height=480)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
