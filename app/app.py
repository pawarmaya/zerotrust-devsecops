from flask import Flask, render_template

app = Flask(__name__)
import subprocess

def execute_command(user_input):
    subprocess.call(user_input, shell=True)
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/run')
def run():
    cmd = request.args.get('cmd')
    subprocess.call(cmd, shell=True)  # Security issue
    return "Executed"

if __name__ == '__
