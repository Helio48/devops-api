from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "mensagem": "Bem-vindo a minha API DevOps!",
        "projeto": "Pratica 3 - Docker"
    })


@app.route("/status")
def status():
    return jsonify({
        "status": "erro",
        "mensagem": "Aplicacao funcionando corretamente!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)