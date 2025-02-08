import os
from flask import Flask, request, render_template, send_file
from openai import OpenAI
from pathlib import Path

# Load environment variables
OPENAI_API_KEY = "OPENAI_API_KEY"

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Flask app setup
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

AVAILABLE_MODELS = ["tts-1", "tts-1-hd"]
AVAILABLE_VOICES = ["alloy", "ash","coral","echo", "fable", "onyx", "nova","sage", "shimmer"]
AVAILABLE_FORMATS = ["mp3", "wav","opus","aac","flac","pcm"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get("text")
        file = request.files.get("file")
        model = request.form.get("model", "tts-1")
        voice = request.form.get("voice", "alloy")
        response_format = request.form.get("response_format", "mp3")
        speed = float(request.form.get("speed", 1.0))
        
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read().strip()

        if not text:
            return "Error: No text provided.", 400

        output_file = os.path.join(OUTPUT_FOLDER, f"output.{response_format}")
        
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text,
            response_format=response_format,
            speed=speed
        )
        
        response.stream_to_file(output_file)

        return send_file(output_file, as_attachment=True)
    
    return render_template("index.html", models=AVAILABLE_MODELS, voices=AVAILABLE_VOICES, formats=AVAILABLE_FORMATS)

if __name__ == '__main__':
    app.run(debug=True)
