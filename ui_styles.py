from PyQt5.QtGui import QColor, QPalette

class AppStyles:
    @staticmethod
    def get_main_style(is_dark_theme):
        # This is for the main summarizer page (will be overridden by background image, but kept for consistency)
        if is_dark_theme:
            return "background-color: #1a1a2e; color: #ffffff;"
        else:
            return "background-color: #f8f9fa; color: #333333;"

    @staticmethod
    def get_frame_style(is_dark_theme):
        # Frame background will have opacity to let the image show through
        if is_dark_theme:
            return """
                background-color: rgba(22, 33, 62, 0.85); /* Slightly more opaque dark background */
                border-radius: 15px;
                border: 1px solid #0f3460;
            """
        else:
            return """
                background-color: rgba(255, 255, 255, 0.85); /* Slightly more opaque white background */
                border-radius: 15px;
                border: 1px solid #e0e0e0;
            """

    @staticmethod
    def get_input_style(is_dark_theme):
        if is_dark_theme:
            return """
                background-color: #0f3460;
                color: #ffffff;
                border: 2px solid #1a1a2e;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            """
        else:
            return """
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #e0e0e0;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            """

    @staticmethod
    def get_primary_button_style(is_dark_theme):
        if is_dark_theme:
            return """
                background-color: #4e54c8; /* A vibrant blue-purple */
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            """
        else:
            return """
                background-color: #3498db; /* A standard blue */
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            """

    @staticmethod
    def get_secondary_button_style(is_dark_theme):
        if is_dark_theme:
            return """
                background-color: #1a1a2e; /* Dark background with border */
                color: #ffffff;
                border: 2px solid #4e54c8;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            """
        else:
            return """
                background-color: #f8f9fa; /* Light background with border */
                color: #3498db;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            """

    @staticmethod
    def get_toggle_button_style(is_dark_theme):
        # This style is specifically for the toggle button on the summarizer page.
        if is_dark_theme:
            return """
                background-color: #0f3460;
                color: #ffffff;
                border: 1px solid #4e54c8;
                border-radius: 10px;
                padding: 5px 10px;
                font-size: 12px;
            """
        else:
            return """
                background-color: #ffffff;
                color: #3498db;
                border: 1px solid #3498db;
                border-radius: 10px;
                padding: 5px 10px;
                font-size: 12px;
            """

    @staticmethod
    def get_label_style(is_dark_theme, font_size="16px", font_weight="normal"):
        if is_dark_theme:
            return f"font-size: {font_size}; font-weight: {font_weight}; color: #ffffff;"
        else:
            return f"font-size: {font_size}; font-weight: {font_weight}; color: #333333;"

    @staticmethod
    def get_title_style(is_dark_theme):
        # Title color now adjusts with the theme: white for dark mode, black/dark gray for light mode
        if is_dark_theme:
            return "font-size: 36px; font-weight: bold; color: #ffffff;" # White for dark mode
        else:
            return "font-size: 36px; font-weight: bold; color: #333333;" # Dark gray/black for light mode

    @staticmethod
    def get_subtitle_style(is_dark_theme):
        if is_dark_theme:
            return "font-size: 20px; color: #bbbbbb;"
        else:
            return "font-size: 20px; color: #555555;"