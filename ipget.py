import configparser
import socket
import time
from urllib.parse import urlparse
import requests

import psutil
import requests


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


def spam(webhook, file):
    while True:
        try:
            data = requests.post(webhook, json={'content': file})
            if data.status_code == 204:
                print(f"Send successfully!")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit()


