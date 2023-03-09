import cv2
import socket

# カメラから画像をキャプチャする
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

# 画像をJPEG形式にエンコードしてバイナリデータに変換する
_, img_encoded = cv2.imencode('.jpg', frame)
img_bytes = img_encoded.tobytes()

# Socketを使用して、公開されたngrok URLに接続し、送信されたデータを受信する
NGROK_URL = 'https://xxxxxxxx.ngrok.io'  # ngrokで公開されたURL
BUFFER_SIZE = 4096                      # バッファサイズ

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostbyname('xxxxxxxx.ngrok.io'), 80))
    s.sendall(f"POST / HTTP/1.1\r\nHost: {NGROK_URL}\r\nContent-Type: image/jpeg\r\nContent-Length: {len(img_bytes)}\r\n\r\n".encode('utf-8'))
    s.sendall(img_bytes)
    response = s.recv(BUFFER_SIZE)

print('Received', repr(response))
