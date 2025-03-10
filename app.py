from flask import Flask, request, render_template, jsonify
import requests
import os
from PIL import Image
import base64
import io

app = Flask(__name__)

# アップロードされたファイルを保存するディレクトリ
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 画像を読み込んでbase64エンコード
    img = Image.open(image)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Ollamaのエンドポイント
    url = "http://localhost:11434/api/generate"
    
    # リクエストデータ
    data = {
        "model": "granite3.2-vision:latest",  # または他のvisionモデル
        "prompt": "What do you see in this image?",
        "stream": False,
        "images": [img_str]
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
        return jsonify({'message': result['response']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)