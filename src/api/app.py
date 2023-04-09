from flask import Flask, request, jsonify
from database import get_db
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


db = get_db()


@app.route('/create_user', methods=['POST'])
def create_user():
        try:
            data = json.loads(request.data)
            telegram_id = data['telegram_id']
            first_name = data['first_name']
            last_name = data['last_name']
            chat_id = data['chat_id']
            user_ref = db.collection('users').document(telegram_id)
            user_ref.set({
                'telegram_id': telegram_id,
                'first_name': first_name,
                'last_name': last_name,
                'score': 0,
                'remaining_attempts': 5,
                'chat_id': chat_id,
                'answered_questions': []
            })
            
            return {'message': 'User created successfully!'}
        except Exception as e:
            print(e)
            return jsonify({'message': 'Error occurred'})