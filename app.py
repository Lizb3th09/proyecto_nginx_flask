from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "parece que va llover, Flask está funcionando detrás de NGINX!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
