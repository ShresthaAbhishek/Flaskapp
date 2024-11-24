from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy;
from datetime import datetime

#app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

#Data class; this is our model (rows)
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task{self.id}"



#Setting up route HOME PAGE
@app.route("/", methods = ["POST", "GET"])
def index():
    #ADD TASK
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error:{e}")
            return f"ERROR:{e}"
        #See all current Tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)

























if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    #use context manager
    app.run(debug=True)