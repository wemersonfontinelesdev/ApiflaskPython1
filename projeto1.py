from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Kama Sutra',
        'autor': 'Um indiano'
    },
    {
        'id': 2,
        'título': 'Kama Sutra2',
        'autor': 'Um indiano2'
    },
    {
        'id': 3,
        'título': 'Kama Sutra3',
        'autor': 'Um indiano3'
    },
]

#consultar(todos)
@app.route('/livros',methods=['GET'])  # Corrigido aqui
def obter_livros():
  return jsonify (livros)
#consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
  for livro in livros:
    if livro.get('id')==id:
      return jsonify(livro)
    #/2
#Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_id(id):
  livro_alterado= request.get_json()
  for indice, livro in enumerate(livros):
    if livro.get('id')==id:
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])
#CRIARR
@app.route('/livros', methods=['POST'])
def incluir_novo():
  novo_livro=request.get_json()
  livros.append(novo_livro)
  return jsonify(livros)
#Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
  for indice, livro in enumerate(livros):
    if livro.get('id')==id:
      del livros[indice]
  return jsonify(livros)
app.run(port=5000, host='localhost', debug=True)
