# Text-to-Speech Program

Text-to-Speech is a Python program that utilizes the Windows SAPI (Speech Application Programming Interface) to convert text input into speech output.

## Features

- Converts text into speech using the Windows SAPI.
- Interactive loop for entering text to be spoken.
- Graceful exit with Ctrl+C.

## Prerequisites

- Windows operating system
- Python 3.x
- `win32com.client` library (install using `pip install pywin32`)

## Installation

1. Clone the repository:

    ```shell
    $ git clone https://github.com/GhalbeYou/text-to-speech.git
    ````

2. Change to the project directory:

    ```shell
    cd text-to-speech
    ```

3. Install the required dependencies:

    ```shell
    pip install pywin32
    ```

## Usage

1. Open a command prompt or terminal.

1. Navigate to the project directory.

1. Run the following command:

   ```shell
   python text_to_speech.py
   ```

1. Type your text and press Enter. The program will convert it into speech.

1. Press Ctrl+C to exit the program.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).