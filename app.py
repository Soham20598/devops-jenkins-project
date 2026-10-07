from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", version=os.getenv("APP_VERSION", "1.0"))

@app.route("/health")
def health():
    return {"status": "healthy", "service": "DevOps Demo App"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
