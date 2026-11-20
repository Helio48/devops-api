from app import app


def test_home():
    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200

    dados = resposta.get_json()

    assert dados["projeto"] == "Pratica 3 - Docker"


def test_status():
    cliente = app.test_client()

    resposta = cliente.get("/status")

    assert resposta.status_code == 200

    dados = resposta.get_json()

    assert dados["status"] == "ok"