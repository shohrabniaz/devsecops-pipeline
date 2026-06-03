import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "devsecops-demo"})


@app.get("/")
def index():
    return jsonify({"message": "DevSecOps pipeline sample API", "version": "1.0.0"})


if __name__ == "__main__":
    # Default 127.0.0.1 for local dev; Docker sets FLASK_HOST=0.0.0.0
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8080"))
    app.run(host=host, port=port)
