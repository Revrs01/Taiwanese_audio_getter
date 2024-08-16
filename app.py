import base64
import json
from flask import Flask, request
import os
import logging
from werkzeug.middleware.proxy_fix import ProxyFix

AUDIO_DIR = os.path.join('..', 'Tai_audio_test')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route('/get_record_file', methods=["POST"])
# pending
def get_record_file():
    req = request.get_json()
    student = req["grade_studentClass_seatNumber_studentName"]
    school_name = req["schoolName"]
    question_number = req["questionNumber"]

    path_of_audio = ""

    full_path = os.path.join(AUDIO_DIR, school_name, student)

    for root, dirs, files in os.walk(full_path):
        for file in files:
            if file.endswith(f"2_{question_number}.wav"):
                path_of_audio = os.path.join(root, file)
                break

    try:
        base64_encoder = base64.b64encode(open(path_of_audio, "rb").read())
        base64_decoder = base64_encoder.decode("utf-8")
    except FileNotFoundError as error:
        logging.warning(error)
        base64_decoder = ""
    return json.dumps({"base64String": base64_decoder}, ensure_ascii=False)
