import os
import psutil
import platform
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app) # Mobil uygulamaların bağlanabilmesi için kritik

# Yapılandırma
API_KEY = "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"
MODEL = "llama-3.3-70b-versatile"
client = Groq(api_key=API_KEY)

@app.route('/api/stats')
def get_stats():
    return jsonify({
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "os": platform.system(),
        "status": "Secure"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '')
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Adın Holy. Oğuzhan'ın siber güvenlik asistanısın. Net ve profesyonel ol."},
                {"role": "user", "content": user_msg}
            ],
            model=MODEL,
        )
        return jsonify({"reply": chat_completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": f"Hata: {str(e)}"}), 500

if __name__ == '__main__':
    # host='0.0.0.0' sayesinde telefonun bilgisayarına bağlanabilir
    print("[*] Holy Sunucusu Mobil Erişime Açık (Port: 5000)")
    app.run(host='0.0.0.0', port=5000)