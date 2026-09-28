from flask import Flask, request, jsonify, send_file
import random
from datetime import datetime, timedelta

app = Flask(__name__)

respostas_desconhecidas = [
    "Xavier: Infelizmente não consigo te responder isso",
    "Xavier: Ainda não consigo responder essa pergunta",
    "Xavier: Infelizmente nao tenho essas imformações",
]

respostas_somas = [
    "Xavier: essa e facil e igual a",
    "Xavier: muito facil logico que e",
    "Xavier: claro que o resultado e"
]


def responder(pergunta):
    agora = datetime.utcnow() - timedelta(hours=3)
    hora = agora.strftime("%H:%M")
    data = agora.strftime("%d/%m/%Y")

    pergunta = pergunta.lower().strip()

    if pergunta == "":
        return ""

    if "oi" in pergunta or "ola" in pergunta or "opa" in pergunta or "eai" in pergunta:
        return "Xavier: Opa, sou Xavier seu assistente pessoal, em que posso te ajudar?"

    elif "hora" in pergunta:
        return "Xavier: Agora são " + hora

    elif "data" in pergunta:
        return "Xavier: a data e " + data

    elif "tudo bem" in pergunta:
        return "Xavier: Tudo otimo, e com você?"

    elif "comigo esta otimo" in pergunta or "estou bem" in pergunta:
        return "Xavier: Otimo! Fico muito feliz de saber isso"

    elif "obrigado" in pergunta or "otimo obrigado" in pergunta:
        return "Xavier: Que nada! Foi um prazer te ajudar"

    elif "qual seu nome" in pergunta:
        return "Xavier: meu nome e Xavier, estou na versão 1.23"

    elif "tchau" in pergunta or "ate mais" in pergunta:
        return "Xavier: Ate mais, espero ter te ajudado hoje."

    elif "criador" in pergunta:
        return "Xavier: Meu criador se chama Estêvão me criou pelo python uma patlaforma de progamação"

    elif "+" in pergunta:
        try:
            numeros = pergunta.split("+")
            numero1 = float(numeros[0].strip())
            numero2 = float(numeros[1].strip())
            resultado = numero1 + numero2
            return random.choice(respostas_somas) + " " + str(resultado)
        except (ValueError, IndexError):
            return random.choice(respostas_desconhecidas)

    elif "-" in pergunta:
        try:
            numeros = pergunta.split("-")
            numero1 = float(numeros[0].strip())
            numero2 = float(numeros[1].strip())
            resultado = numero1 - numero2
            return "Xavier: o resultado dessa subtração e " + str(resultado)
        except (ValueError, IndexError):
            return random.choice(respostas_desconhecidas)

    elif "*" in pergunta:
        try:
            numeros = pergunta.split("*")
            numero1 = float(numeros[0].strip())
            numero2 = float(numeros[1].strip())
            resultado = numero1 * numero2
            return "Xavier: o resultado dessa multiplicação e " + str(resultado)
        except (ValueError, IndexError):
            return random.choice(respostas_desconhecidas)

    else:
        return random.choice(respostas_desconhecidas)


@app.route("/")
def inicio():
    return send_file("index.html")


@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.get_json()

    if not dados or "pergunta" not in dados:
        return jsonify({
            "resposta": "Xavier: Não entendi a pergunta."
        })

    pergunta = dados["pergunta"]
    resposta = responder(pergunta)

    return jsonify({
        "resposta": resposta
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)