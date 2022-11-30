from flask import Flask
from flask import render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack n slash', 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')

    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

app.run()