import os

# Get the absolute path of the current directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ✅ Use SQLite instead of MySQL (no external DB needed)
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"

# ✅ Turn off tracking to reduce overhead
SQLALCHEMY_TRACK_MODIFICATIONS = False

# ✅ Secret key for sessions (from Render environment variable or fallback)
SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey123")
