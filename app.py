from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!123"

# ---- Đây là nơi đặt dòng app.run ----
if __name__ == "__main__":
    # Chạy Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)
