from flask import Flask, request, jsonify, send_file
import random
from datetime import datetime

app = Flask(__name__)

import random
from datetime import datetime, timedelta

respostas_desconhecidas = [
    "Xavier: Infelizmente não consigo te responder isso",
    "Xavier: Ainda não consigo responder essa pergunta",
    "Xavier: Infelizmente nao tenho essas imformações",
    ]

respostas_somas = [
    "Xavier: essa e facil e igual a",
    "Xavier: muito facil logico que e",
    "Xavier: claro que o resultado e" ]


while True:

    agora = datetime.utcnow() - timedelta(hours=3)
    hora = agora.strftime("%H:%M")
    data = agora.strftime("%d/%m/%Y")
    pergunta = input ("Você:")
    pergunta = pergunta.lower()
    
    if "oi" in pergunta or "ola" in pergunta or "opa" in pergunta or "eai" in pergunta:
        print ("Xavier: Opa, sou Xavier seu assistente pessoal, em que posso te ajudar?")
        
    elif "hora" in pergunta.lower():
        print ("Xavier: Agora são",hora)
        
    elif "data" in pergunta.lower():
        print ("Xavier: a data e",data)
        
    elif "tudo bem" in pergunta:
        print ("Xavier: Tudo otimo, e com você?")

    elif "comigo esta otimo" in pergunta or "estou bem" in pergunta:
        print("Xavier: Otimo! Fico muito feliz de saber isso")
        
    elif "obrigado"in pergunta or "otimo obrigado" in pergunta:
        print("Que nada! Foi um prazer te ajudar")
        
    elif "qual seu nome" in pergunta:
        print("Xavier: meu nome e Xavier, estou na versão 1.23")
    elif "tchau" in pergunta or "ate mais" in pergunta:
        print("Xavier: Ate mais, espero ter te ajudado hoje.")

    elif "criador" in pergunta.lower():
        print ("Xavier: Meu criador se chama Estêvão me criou pelo python uma patlaforma de progamação")
        
    elif "+" in pergunta:
        numeros = pergunta.split("+")
        numero1 = float(numeros[0])
        numero2 = float(numeros[1])
        resultado = numero1 + numero2
        print(random.choice(respostas_somas),resultado)

    elif "-" in pergunta:
        numeros = pergunta.split("-")
        numero1 = float(numeros[0])
        numero2 = float(numeros[1])
        resultado = numero1 - numero2
        print ("o resultado dessa subtração e",resultado)

    elif "*" in pergunta:
        numeros = pergunta.split("*")
        numero1 = float(numeros[0])
        numero2 = float(numeros[1]) 
        resultado = numero1 * numero2
        print ("o resultado dessa multiplicação e",resultado)

 
    else:
        print(random.choice(respostas_desconhecidas))



@app.route("/")
def inicio():
    return send_file("index.html")


@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.json
    pergunta = dados["pergunta"]

    resposta = responder(pergunta)

    return jsonify({
        "resposta": resposta
    })
