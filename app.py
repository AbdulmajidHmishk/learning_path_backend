


from flask import Flask, jsonify
from data_manager import JsonDataManager
import json
import os

app = Flask(__name__)
data_manager = JsonDataManager()

@app.route('/topics',methods=['GET'])
def get_topics(): 
       data_file = os.path.join(os.path.dirname(__file__),'data','topics.json')
       with open(data_file , 'r' ,encoding='utf-8') as f:
          topics = data_manager.read_data(data_file)
       return jsonify(topics)


@app.route('/')
def hello():
    return "Hello from Topic & Skill Service!"

if __name__ == '__main__':
    app.run(debug=True) 