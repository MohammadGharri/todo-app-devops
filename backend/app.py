from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/api/todos")
def get_todos():
    return jsonify([
        {"id": 1, "title": "🔥 Learn Docker (updated)", "done": False},
        {"id": 2, "title": "Build a CI/CD pipeline", "done": False}
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
