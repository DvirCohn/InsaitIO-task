from flask import Flask, request, jsonify
# import openai
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# openai.api_key = 'your-openai-api-key'

class QuestionAnswer(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400

    # Mock response instead of OpenAI API call
    # response = openai.Completion.create(
    #     engine="davinci",
    #     prompt=question,
    #     max_tokens=150
    # )
    # answer = response.choices[0].text.strip()
    answer = "This is a mock answer."

    qa = QuestionAnswer(question=question, answer=answer)
    db.session.add(qa)
    db.session.commit()

    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
