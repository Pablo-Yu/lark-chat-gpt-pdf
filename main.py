from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 从 Secrets 中获取你的 OpenAI 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["POST"])
def analyze_pdf_text():
    data = request.json
    content = data.get("text", "")

    if not content:
        return jsonify({"error": "No text provided"}), 400

    # 发送给 ChatGPT 分析文本内容
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "你是一位文献分析专家，请用中文整理用户提交的文献内容"},
            {"role": "user", "content": content}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"result": reply})

# 启动 Flask 服务
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)