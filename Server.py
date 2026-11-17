
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Fuga do Professor</title>
    </head>
    <body style="background:#171725;color:white;text-align:center;font-family:Arial;padding:40px">
        <h1>🎮 FUGA DO PROFESSOR</h1>
        <h2>Servidor online!</h2>
        <p>Nosso projeto está na internet!</p>
    </body>
    </html>
    """

@app.route("/status")
def status():
    return jsonify({
        "jogo": "Fuga do Professor",
        "servidor": "online"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
