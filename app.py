from flask import Flask
from flask_session import Session
from routes.authen_routes import auth_routes
from routes.chatbot_routes import chatbot_routes
from routes.file_routes import file_routes
from routes.course_routes import course_routes
from config.db import init_mongo, init_pinecone
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure Flask Session
app.config['SECRET_KEY'] = '9442e31a2e8c1e1b39826a3db7ef388e88e7fc93cab68e1c'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Initialize MongoDB
mongo_db = init_mongo()
user_collection = mongo_db["users"]

# Initialize Pinecone
pinecone_index = init_pinecone()

# Register Blueprints
app.register_blueprint(auth_routes, url_prefix="/auth")
app.register_blueprint(chatbot_routes, url_prefix="/chat")
app.register_blueprint(file_routes, url_prefix="/files")
app.register_blueprint(course_routes, url_prefix="/courses")

@app.route('/')
def home():
    return {"message": "Welcome to MyPal API"}

######change kenza
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)