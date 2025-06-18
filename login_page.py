import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLabel,
                             QLineEdit, QMessageBox, QFrame, QStackedLayout)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer

from db_manager import hash_password, authenticate_user_db, register_user_db
from ui_styles import AppStyles

class LoginPage(QWidget):
    """
    Represents the login and registration page of the application.
    Allows users to log in or register new accounts.
    """
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("✨ Keypoint AI 💡 - Login")
        self.setGeometry(100, 100, 500, 500)

        self.setObjectName("LoginPage")
        self.is_dark_theme = False # Login page starts in light theme

        # --- Background Image Layer ---
        self.background_label = QLabel(self)
        self.background_label.setScaledContents(True)

        # --- Content Layer ---
        content_layout = QVBoxLayout()
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(100, 50, 100, 50)

        # Title
        title = QLabel("✨ Keypoint AI 💡")
        title.setObjectName("AppTitle")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        # Subtitle
        subtitle = QLabel("Sign in or create an account to continue")
        subtitle.setObjectName("AppSubtitle")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 16))

        # Form Frame for better visual grouping
        form_frame = QFrame()
        form_frame.setObjectName("FormFrame")
        form_frame.setFrameShape(QFrame.StyledPanel)
        form_frame.setFrameShadow(QFrame.Raised)
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(30, 30, 30, 30)

        # Username input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMinimumHeight(45)
        self.username_input.setFont(QFont("Segoe UI", 12))

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(45)
        self.password_input.setFont(QFont("Segoe UI", 12))

        # Login button
        self.login_button = QPushButton("Login", self)
        self.login_button.setMinimumHeight(50)
        self.login_button.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.login_button.clicked.connect(self.authenticate_user)

        # Register button
        self.register_button = QPushButton("Create Account", self)
        self.register_button.setMinimumHeight(50)
        self.register_button.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.register_button.clicked.connect(self.register_user)

        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.login_button)
        form_layout.addWidget(self.register_button)

        form_frame.setLayout(form_layout)

        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)
        content_layout.addStretch(1)
        content_layout.addWidget(form_frame)
        content_layout.addStretch(2)

        # --- Wrap content_layout in a QWidget to add to QStackedLayout ---
        content_widget = QWidget()
        content_widget.setLayout(content_layout)

        # --- Stacked Layout to layer background and content ---
        main_stacked_layout = QStackedLayout()
        main_stacked_layout.addWidget(self.background_label)
        main_stacked_layout.addWidget(content_widget)
        main_stacked_layout.setStackingMode(QStackedLayout.StackAll)

        self.setLayout(main_stacked_layout)
        self.apply_theme_styles()

    def apply_theme_styles(self):
        """Applies the current theme's stylesheets to all widgets on the login page."""
        self._set_background_image("images\login_background.jpg")

        self.setStyleSheet(AppStyles.get_label_style(self.is_dark_theme, "16px", "normal"))

        self.findChild(QLabel, "AppTitle").setStyleSheet(AppStyles.get_title_style(self.is_dark_theme))
        self.findChild(QLabel, "AppSubtitle").setStyleSheet(AppStyles.get_subtitle_style(self.is_dark_theme))

        self.findChild(QFrame, "FormFrame").setStyleSheet(AppStyles.get_frame_style(self.is_dark_theme))
        self.username_input.setStyleSheet(AppStyles.get_input_style(self.is_dark_theme))
        self.password_input.setStyleSheet(AppStyles.get_input_style(self.is_dark_theme))
        self.login_button.setStyleSheet(AppStyles.get_primary_button_style(self.is_dark_theme))
        self.register_button.setStyleSheet(AppStyles.get_secondary_button_style(self.is_dark_theme))

    def _set_background_image(self, image_path):
        """Loads and sets the background image to the QLabel."""
        try:
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                raise FileNotFoundError(f"Failed to load image: {image_path}. Pixmap is null.")
            self.background_label.setPixmap(pixmap)
        except Exception as e:
            QMessageBox.critical(self, "Image Load Error",
                                 f"Could not load background image from '{image_path}'.\n"
                                 f"Please ensure the file exists and is readable.\nError: {e}")
            self.background_label.setStyleSheet("background-color: #333333;") # Fallback color
            print(f"Error loading background image: {e}")

    def toggle_theme(self):
        """Toggles the current theme between dark and light and applies the new styles."""
        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme_styles()

    def authenticate_user(self):
        """Authenticates the user based on provided username and password."""
        username = self.username_input.text().strip()
        password_text = self.password_input.text().strip()
        password_hash = hash_password(password_text)

        if not username or not password_text:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            return

        user = authenticate_user_db(username, password_hash)

        if user:
            self.stacked_widget.setCurrentIndex(1) # Go to loading page
            QTimer.singleShot(1500, lambda: self.finish_authentication(self.is_dark_theme))
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def finish_authentication(self, theme_state):
        # Access the AINoteSummarizer page and set its theme
        ainote_summarizer_page = self.stacked_widget.widget(2)
        ainote_summarizer_page.is_dark_theme = theme_state
        ainote_summarizer_page.apply_theme_styles() # Apply theme based on login page's state

        self.stacked_widget.setCurrentIndex(2) # Go to AINoteSummarizer Page

    def register_user(self):
        """Registers a new user with the provided username and password."""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Registration Failed", "Please enter a username and password.")
            return

        hashed_password = hash_password(password)

        if register_user_db(username, hashed_password):
            QMessageBox.information(self, "Success", "User registered successfully! You can now log in.")
        else:
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")