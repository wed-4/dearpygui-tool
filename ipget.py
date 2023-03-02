import requests
import socket
from urllib.parse import urlparse
import os
import base64
import configparser
import psutil
import re
import ctypes


def get_gip_addr():
    res = requests.get('https://ifconfig.me')
    return res.text


def get_host():
    return socket.gethostname()


def urlanalyze(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == "line.me":
        return 0
    else:
        return 1


def imageinput():
    config = configparser.ConfigParser()
    config.read('image.ini')
    imagepath = config['IMAGE']['PATH']
    return imagepath


def dllfile():
    configb = configparser.ConfigParser()
    configb.read('image.ini')
    return configb['DLL']['DLLPATH']


def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
    return cpu_percent


def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()
