from backend.app import app
from backend.database.db import db
    
if __name__ == "__main__":
    app.run(debug=True)

with app.app_context():
    db.create_all()