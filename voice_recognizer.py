import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_and_recognize(self):
        """
        Listens to microphone input and attempts to recognize speech.
        Returns (recognized_text, error_message).
        """
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1) # Adjust for noise
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10) # Listen for up to 10 seconds of speech
            except sr.WaitTimeoutError:
                return None, "No speech detected within the timeout period."
            except Exception as e:
                return None, f"Could not access microphone or listening error: {e}"

        try:
            # Use Google Web Speech API for recognition (requires internet connection)
            text = self.recognizer.recognize_google(audio)
            return text, None
        except sr.UnknownValueError:
            return None, "Google Speech Recognition could not understand audio."
        except sr.RequestError as e:
            return None, f"Could not request results from Google Speech Recognition service; check your internet connection: {e}"
        except Exception as e:
            return None, f"An unexpected error occurred during speech recognition: {e}"