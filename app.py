import datetime
from flask import Flask, render_template_string
app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <h1>Hello, Flask!</h1>
        <p>Welcome to your Flask application running on port 5001.</p>
        <p>This is a simple web page served by Flask.</p>
        <p>You can modify this content in the app.py file.</p>
        <p>Current time: {{ current_time }}</p>
        <p>Happy coding!</p>
    """, current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
