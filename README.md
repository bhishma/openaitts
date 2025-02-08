# Text-to-Speech Converter

## Overview
This is a simple web-based Text-to-Speech (TTS) converter that allows users to enter text or upload a `.txt` file, select a voice model, output format, and adjust the speech speed. The processed audio can be downloaded in different formats.

## Features
- Enter text manually or upload a `.txt` file.
- Choose from multiple AI models for speech synthesis.
- Select different voices to customize the speech output.
- Choose an output format: MP3, WAV, or OGG.
- Adjust speech speed (0.5x to 2.0x).
- Simple and intuitive user interface with help tooltips.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/bhishma/openaitts.git
   ```
2. Navigate to the project directory:
   ```sh
   cd openaitts
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Environment Variables
Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application
1. Start the server:
   ```sh
   python app.py
   ```
2. Open your browser and navigate to `http://localhost:5000`.

## Usage
1. Enter text or upload a `.txt` file.
2. Select a model, voice, output format, and speed.
3. Click the **Convert to Speech** button.
4. Download the generated audio file.

## Technologies Used
- Python (Flask)
- OpenAI API
- HTML, CSS, JavaScript

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests for improvements.

## Acknowledgments
Thanks to OpenAI for their powerful TTS API!