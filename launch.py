import sys
import os
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebViewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quizziee')
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://localhost/web/login.html'))

        self.setCentralWidget(self.browser)

def start_server():
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    web_dir = os.path.join(os.path.dirname(__file__), '')
    os.chdir(web_dir)
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving on http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

if __name__ == '__main__':
    import threading
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    app = QApplication(sys.argv)
    window = WebViewApp()
    window.show()
    sys.exit(app.exec_())