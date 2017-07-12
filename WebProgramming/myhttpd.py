# -*- coding: utf-8 -*-

'''
本脚本是简单的web服务器，可以读取GET请求，获取web页面(.html)文件，
并将其返回给调用的客户。
使用BaseHTTPServer(http.server in py3)中的BaseHTTPRequestHandler,
并实现do_GET()方法来启用对GET请求的处理
'''

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        server = HTTPServer(('', 8080), MyHandler)
        print('Welcome to the machine...')
        print('Press ^C once or twice to quit.')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server.')
        server.socket.close()

if __name__ == "__main__":
    main()
