from flask import Flask, render_template, request

# Create a Flask app instance
app = Flask(__name__)

# Handle HTTP requests
# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        available_date = request.form["available_date"]
        occupation = request.form["occupation"]
        print(first_name, last_name, email, available_date, occupation)

    return render_template("index.html")

# Execute the web app
app.run(debug=True,
        port=5001)