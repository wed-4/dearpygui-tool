import requests
import socket
from urllib.parse import urlparse
import os
import base64
import configparser


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
