from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# OpenAI API Key
openai.api_key = os.environ['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']

# ホームページ
@app.route('/')
def index():
    return render_template('index.html')

# ChatGPTに対してリクエストを送信するAPI
@app.route('/chat', methods=['POST'])
def chat():
    input_text = request.form['input_text']
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
