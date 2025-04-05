from flask import Flask
from models import db  # Import database instance

app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # For session security

# Initialize database with app
db.init_app(app)

# Create tables before running the app
with app.app_context():
    db.create_all()

@app.route('/')  # ✅ Moved out of the `with` block
def home():
    return "🎉 Flask App is Running!"

if __name__ == '__main__':
    app.run(debug=True)
