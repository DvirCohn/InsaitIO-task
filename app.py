from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/ask', methods=['POST'])
def ask():
    data = request.json

    if not data or 'question' not in data:
        return jsonify({'error': 'invalid input! pls insert a question.'}), 400

    question = data['question']


if __name__ == "__main__":
    app.run(port=5000, debug=True)