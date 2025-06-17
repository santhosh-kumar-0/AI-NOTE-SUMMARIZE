from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QFont

class LoadingPage(QWidget):
    """
    A simple loading page with a GIF animation.
    """
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Loading...")
        # This page will now automatically take the size of its parent QStackedWidget (800x700).

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter) # This ensures content is centered within this page
        main_layout.setSpacing(20)

        # Loading text
        self.loading_text = QLabel("Loading...", self)
        self.loading_text.setFont(QFont("Segoe UI", 20, QFont.Bold))
        self.loading_text.setAlignment(Qt.AlignCenter)
        self.loading_text.setStyleSheet("color: #4e54c8;") # Match primary button color

        # Loading GIF
        # IMPORTANT: You need a 'loading.gif' file in your project directory
        # You can download one or create a simple one.
        # Example search: "loading spinner gif transparent background"
        self.loading_movie = QMovie("loading.gif")
        if not self.loading_movie.isValid():
            print("Error: loading.gif not found or is invalid.")
            # Fallback if GIF isn't found
            self.loading_animation = QLabel("Loading animation missing!", self)
            self.loading_animation.setAlignment(Qt.AlignCenter)
            self.loading_animation.setStyleSheet("color: red;")
            main_layout.addWidget(self.loading_animation)
        else:
            self.loading_animation = QLabel(self)
            self.loading_animation.setMovie(self.loading_movie)
            self.loading_animation.setAlignment(Qt.AlignCenter)
            self.loading_movie.start()
            main_layout.addWidget(self.loading_animation)

        main_layout.addWidget(self.loading_text)
        self.setLayout(main_layout)

        self.setStyleSheet("background-color: #1a1a2e;") # Dark background for loading page