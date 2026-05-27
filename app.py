from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 画面と通信するためのお守り

@app.route('/process', methods=['POST'])
def process_audio():
    lecture_name = request.form.get('lectureName', '無題の講義')
    print(f"【受信】講義名: {lecture_name}")

    return jsonify({
        "transcription": f"「{lecture_name}」の音声から文字起こししたテキストがここに表示されます。",
        "summary": "これはPythonサーバーから返ってきたテスト用の要約文です。",
        "keyPoints": [
            "Pythonサーバーとの接続に成功しました！",
            "次はここに本物のAI（Gemini）を組み込みます",
            "音声ファイルの読み込みもここでおこないます"
        ]
    })

if __name__ == '__main__':
    print("--- Flaskサーバーを起動しています ---")
    app.run(port=3000, debug=True)