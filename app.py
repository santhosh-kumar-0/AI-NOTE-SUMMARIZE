import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from login_page import LoginPage
from loading_page import LoadingPage
from ainote_summarizer import AINoteSummarizer

class App(QApplication):
    """
    Main application class that sets up the UI and manages different pages.
    """
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.init_ui()

    def init_ui(self):
        # QStackedWidget allows us to switch between different pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setWindowTitle("AI Note Summarizer") # Set main window title
        self.stacked_widget.setFixedSize(800, 700) # Fixed size for the main application window

        # Initialize pages
        self.login_page = LoginPage(self.stacked_widget)
        self.loading_page = LoadingPage(self.stacked_widget)
        self.ainote_summarizer_page = AINoteSummarizer(self.stacked_widget) # Pass stacked_widget

        # Add pages to the stacked widget
        self.stacked_widget.addWidget(self.login_page)          # Index 0
        self.stacked_widget.addWidget(self.loading_page)        # Index 1
        self.stacked_widget.addWidget(self.ainote_summarizer_page) # Index 2

        # Set the initial page to the login page
        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())