import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
cache = redis.from_url(os.getenv('REDIS_URL'))

class User(db.Model):
    __tablename__ = 'user_model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "phone": self.phone}

#with app.app_context():
#    db.create_all()

@app.route('/users', methods=['GET'])
def get_users():
    cached_users = cache.get('all_users')
    if cached_users:
        return jsonify(json.loads(cached_users)), 200

    users = User.query.all()
    result = [user.to_dict() for user in users]

    cache.set('all_users', json.dumps(result), ex=60)
    
    return jsonify(result), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_user)
    db.session.commit()
    
    cache.delete('all_users')
    
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.phone = data.get('phone', user.phone)
    db.session.commit()
    
    cache.delete('all_users')
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    
    cache.delete('all_users')
    return jsonify({"message": "User deleted"}), 200