
import configparser
import json
import tkinter as tk
from tkinter import ttk
from tkcode import CodeEditor
import aiohttp
import asyncio
from aioconsole import aprint
import ssl


def codeeditoropen():
    root = tk.Tk()
    root.title("json editor")
    root.option_add("*tearOff", 0)

    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save as")
    file_menu.add_separator()
    file_menu.add_command(label="Exit")

    help_menu = tk.Menu(menubar)
    help_menu.add_command(label="Help")
    help_menu.add_command(label="About")

    menubar.add_cascade(menu=file_menu, label="File")
    menubar.add_cascade(menu=help_menu, label="Help")

    root.config(menu=menubar)

    notebook = ttk.Notebook(root)
    tab_1 = ttk.Frame(notebook)
    notebook.add(tab_1, text="a.json")
    notebook.pack(fill="both", expand=True)

    code_editor = CodeEditor(
        tab_1,
        width=40,
        height=10,
        language="json",
        highlighter="dracula",
        autofocus=True,
        blockcursor=True,
        insertofftime=0,
        padx=10,
        pady=10,
    )

    code_editor.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()


def jsonread():
    configj = configparser.ConfigParser()
    configj.read('image.ini')
    with open(configj['JSON']['JSONPATH']) as f:
        di = json.load(f)
    return json.dumps(di)


async def joiner(code):
    tokens = open("settings\\tokens.txt").read().splitlines()
    proxies = open("settings\\proxies.txt").read().splitlines()
    if len(proxies) > 0:
        for token, proxy in zip(tokens, proxies):
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers,
                                            json={}, proxy=f"http://{proxy}") as resp:
                        if resp.status == 200:
                            await aprint("Joined successfully")
                        elif resp.status == 429:
                            j = await resp.json()
                            await aprint(f"Ratelimited for {j['retry_after']} seconds")
                            await asyncio.sleep(j['retry_after'])
                        elif resp.status == 403:
                            await aprint("Locked token")
                        else:
                            j = await resp.json()
                            await aprint(resp.status, j, )
                await asyncio.sleep(0.7)
            except Exception as e:
                await aprint(f"Error: {e}")
                continue
    else:
        for token in tokens:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers,
                                            json={}) as resp:
                        if resp.status == 200:
                            await aprint("Joined successfully")
                        elif resp.status == 429:
                            j = await resp.json()
                            await aprint(f"Ratelimited for {j['retry_after']} seconds")
                            await asyncio.sleep(j['retry_after'])
                        elif resp.status == 403:
                            await aprint("Locked token")
                        else:
                            j = await resp.json()
                            await aprint(resp.status, j, )
                await asyncio.sleep(0.7)
            except Exception as e:
                await aprint(f"Error: {e}")
                continue

