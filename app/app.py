from flask import Flask, render_template

app = Flask(__name__)
import subprocess

def execute_command(user_input):
    subprocess.call(user_input, shell=True)
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
