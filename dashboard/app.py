from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_json(file_path):

    if os.path.exists(file_path):

        with open(file_path) as f:
            return json.load(f)

    return {}

@app.route("/")
def dashboard():

    sonar = load_json("reports/sonar.json")
    trivy = load_json("reports/trivy.json")
    build = load_json("reports/build.json")
    deployment = load_json("reports/deployment.json")

    return render_template(
        "index.html",
        sonar=sonar,
        trivy=trivy,
        build=build,
        deployment=deployment
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
import requests

def get_sonar_metrics():

    response = requests.get(
        "http://localhost:9000/api/measures/component",
        params={
            "component":"secure-app",
            "metricKeys":"bugs,vulnerabilities,code_smells"
        },
        auth=(squ_8b3f0bb2fcfcc69275faedba7a214db5dd390785
,"")
    )

    return response.json()
