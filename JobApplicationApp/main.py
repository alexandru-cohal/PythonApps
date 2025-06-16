from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask app instance
app = Flask(__name__)
# Create a SQLAlchemy database instance
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


# Create the database model
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    available_date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


# Handle HTTP requests
# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        available_date = datetime.strptime(request.form["available_date"], "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    available_date=available_date,
                    occupation=occupation)
        db.session.add(form)
        db.session.commit()

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        # Create the database
        db.create_all()
        # Execute the web app
        app.run(debug=True,
                port=5001)