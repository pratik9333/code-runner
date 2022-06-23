import os
from flask import Flask, jsonify, request 
from runner import call_runner

app = Flask(__name__)

UPLOAD_FOLDER = "solutions"

@app.route("/run",methods=["POST","OPTIONS"])
def run():
    try:
        data = request.form
        print(data)
        if request.method == 'POST':  
            f = request.files['main']  
            f.save(f'{UPLOAD_FOLDER}/{f.filename}')  
            call_runner(data["language"],f.filename,data["test_cases"])
            return jsonify({"data":data})
    except Exception as e: 
        return jsonify({"error": f"{e}"})

port = os.getenv('PORT') or 4000

app.run(host="0.0.0.0",port=port)

