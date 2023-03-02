from http.server import SimpleHTTPRequestHandler, HTTPServer


def serversys(port):
    try:
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)  # サーバインスタンスを生成
        print("起動成功")
        server.serve_forever()
    except PermissionError:
        print("起動失敗")

