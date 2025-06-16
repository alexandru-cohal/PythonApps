from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os

# Create a Flask app instance
app = Flask(__name__)

# Create a SQLAlchemy database and mail instances
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("EMAIL_AUTOMATION")
app.config["MAIL_PASSWORD"] = os.getenv("PASS_EMAIL_AUTOMATION")

db = SQLAlchemy(app)
mail = Mail(app)

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

        message_body = (f"Thank you for your submission, {first_name}.\n"
                        f"Here are your data:\n"
                        f"\t{first_name}\n"
                        f"\t{last_name}\n"
                        f"\t{available_date}\n"
                        f"\t{occupation}.\n"
                        f"Thank you!")
        message = Message(subject="New form submission",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)
        mail.send(message)

        flash("The Form was submitted successfully!", "success")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        # Create the database
        db.create_all()
        # Execute the web app
        app.run(debug=True,
                port=5001)