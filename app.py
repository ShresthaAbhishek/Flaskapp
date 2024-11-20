from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy;
from datetime import datetime

#app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

#Data class this is out model
class MyTask(db.Model):
    id = db.Column(db.integer, primary_key=True)
    content = db.Column(db.string(100), nullable=False)
    completed = db.Column(db.integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task{self.id}"



#Setting up route
@app.route("/")
def index():
    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=True)