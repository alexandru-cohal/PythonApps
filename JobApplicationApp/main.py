from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Handle HTTP requests
# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Execute the web app
app.run(debug=True,
        port=5001)