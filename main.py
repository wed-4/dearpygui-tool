import asyncio
import os

import dearpygui.dearpygui as dpg
from pyinjector import inject
import ipget
import requests
import re
import threading
import servertool
import cbg
from guildedjoiner import Exploit


def spamming():
    ipget.spam(dpg.get_value("webhook"), dpg.get_value("fp"))


def grab():
    username = dpg.get_value("username")
    response1 = requests.get(f"https://fortnitetracker.com/profile/all/{username}/events")

    match1 = re.search(r'"accountId":\s*"([^"]+)"', response1.text)

    player_name_regex = r'"playerName":\s*"([^"]+)"'
    match_player_name1 = re.search(player_name_regex, response1.text)

    if match1 and match_player_name1:
        account_id = match1.group(1)
        player_name = match_player_name1.group(1)
        print(f"アカウントID: {account_id}")
        print(f"ユーザー名: {player_name}")
    else:
        print("IDが見つかりません")


def injectdll():
    inject(int(dpg.get_value('pid')), str(ipget.dllfile()))


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        servertool.serversys(dpg.get_value("port"))


class Mythread1(threading.Thread):
    def __init__(self, n):
        super(Mythread1, self).__init__()
        self.n = n

    def run(self):
        cbg.codeeditoropen()


def serverrungo():
    t1 = MyThread("t1")
    t1.start()


def openide():
    t2 = Mythread1("t2")
    t2.start()


def accountkill():
    exploit = Exploit(dpg.get_value("token"))
    exploit.execute()

def accountjoinner():
    asyncio.run(cbg.joiner(dpg.get_value("ic")))




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

with dpg.window(label="discord message spammer", collapsed=False, no_close=True):
    dpg.add_input_text(label="ウェブフックURL", tag="webhook")
    dpg.add_input_text(label="メッセージ", tag="fp")
    dpg.add_button(label="送信", callback=spamming)

with dpg.window(label="discord account disabler", collapsed=False, no_close=True):
    dpg.add_input_text(label="トークン", tag="token")
    dpg.add_button(label="実行", callback=accountkill)

with dpg.window(label="discord joiner", collapsed=False, no_close=True):
    dpg.add_input_text(label="招待コード", tag="ic")
    dpg.add_button(label="実行", callback=accountjoinner)

with dpg.window(label="file grabber", collapsed=False, no_close=True):
    dpg.add_input_text(label="ホスト名", tag="host")
    dpg.add_input_int(label="ポート", tag="portnum")
    with dpg.child_window():
        dpg.add_text("操作盤")
        dpg.add_checkbox(label="サーバーON/OFF", tag="toggle")
        dpg.add_listbox(label="ファイル一覧", items=os.listdir(os.getcwd()))


dpg.show_imgui_demo()

dpg.create_viewport(title=f"Ragnarok", width=640, height=480)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
