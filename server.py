from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos anéis',
        'author': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'author': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'author': 'Hábitos Atômicos'
    }
]

@app.route('/livros')

def obter_livros():
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)