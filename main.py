import win32com.client as wincl

class TextToSpeech:
    """
    TextToSpeech is a Python class that utilizes the Windows SAPI (Speech Application Programming Interface)
    to convert text input into speech output.
    """

    def __init__(self):
        self.speaker = wincl.Dispatch("SAPI.SpVoice")

    def speak(self, text):
        """
        Converts the given text into speech using the Windows SAPI.
        Args:
            text (str): The text to be spoken.
        """
        self.speaker.Speak(text)

    def start(self):
        """
        Starts the text-to-speech loop, prompting the user for input and speaking it out.
        """
        print("Text-to-Speech Program")
        print("======================")
        print("Type your text below. Press Ctrl+C to exit.")
        print("======================")
        print("By @GhalbeYou on GitHub.")
        print()

        while True:
            try:
                text = input("Enter input > ")
                print("Saying it...")
                self.speak(text)
            except KeyboardInterrupt:
                print("\nExiting...")
                break


if __name__ == "__main__":
    t2s = TextToSpeech()
    t2s.start()