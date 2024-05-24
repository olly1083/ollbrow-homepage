import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebEnginePage(QWebEngineView):
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if url.scheme() == "ollbrow":
            query = url.toString().split('google.com/search?q=')[1]
            search_url = QUrl(f"https://www.google.com/search?q={query}")
            self.setUrl(search_url)
            return False
        return super().acceptNavigationRequest(url, _type, isMainFrame)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = WebEnginePage()
        # Set the home page to the GitHub Pages URL
        self.browser.setUrl(QUrl("https://olly1083.github.io/ollbrow-homepage/home.html"))

        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        # Navigate to the GitHub Pages URL
        self.browser.setUrl(QUrl("https://olly1083.github.io/ollbrow-homepage/home.html"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("OLLBROW")
window = Browser()
app.exec_()
