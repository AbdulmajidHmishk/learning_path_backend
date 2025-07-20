


from flask import Flask, jsonify, request
from data_manager import JsonDataManager
import os
import uuid 
app = Flask(__name__)
data_manager = JsonDataManager()



@app.route('/topics',methods=['GET'])
def get_topics(): 
    data_file = os.path.join(os.path.dirname(__file__),'data','topics.json')
    with open(data_file , 'r' ,encoding='utf-8') as f:
        topics = data_manager.read_data(data_file)
    return jsonify(topics)

@app.route ('/skills', methods=['GET'])
def get_skills():
     data_file = os.path.join (os.path.dirname(__file__),'data','skills.json')
     skills = data_manager.read_data(data_file )
     return jsonify (skills)

@app.route('/topics/<id>', methods=['GET'])
def get_topic_by_id(id):
    topics = data_manager.read_data('data/topics.json')
    for topic in topics:
        if topic.get("id") == id:
            return jsonify(topic)
    return jsonify({"error": "Topic not found"}), 404

@app.route('/skills/<id>', methods=['GET'])
def get_skill_by_id(id):
    data_file = os.path.join(os.path.dirname(__file__), 'data', 'skills.json')
    skills = data_manager.read_data(data_file)
    
    for skill in skills:
        if skill.get("id") == id:
            return jsonify(skill)
    
    return jsonify({"error": "Skill not found"}), 404
    


@app.route('/')
def hello():
    return "Hello from Topic & Skill Service!"


@app.route('/topics', methods=['POST'])
def create_topic():
    data = request.get_json()

    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "name and description are required"}), 400

    new_topic = {
        "id": str(uuid.uuid4()),
        "name": data["name"],
        "description": data["description"]
    }

    data_file = os.path.join(os.path.dirname(__file__), 'data', 'topics.json')
    topics = data_manager.read_data(data_file)

    topics.append(new_topic)
    data_manager.write_data(data_file, topics)

    return jsonify(new_topic), 201


if __name__ == '__main__':
    app.run(debug=True) 