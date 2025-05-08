from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os
import tempfile

app = Flask(__name__)
CORS(app)

@app.route("/upload_audio", methods=["POST"])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    # Save the file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        file.save(temp_audio.name)
        audio_path = temp_audio.name

    # ---- Simulate dynamic analysis (replace with real ML logic later) ----
    communication_score = random.randint(60, 95)
    grammar_score = random.randint(60, 95)

    tips = random.choice([
        "Work on reducing filler words like 'um' and 'uh'.",
        "Try to speak more clearly and slowly.",
        "Focus on maintaining eye contact when possible.",
        "Add more structure to your answers.",
        "Use more precise vocabulary."
    ])

    os.remove(audio_path)

    return jsonify({
        "communication_score": communication_score,
        "grammar_score": grammar_score,
        "feedback": tips
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)