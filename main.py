import src.controllers.usuarioController as usuarioController
import src.controllers.vendedorController as vendedorController
import src.controllers.produtoController as produtoController
import src.controllers.compraController as compraController
import src.controllers.redisController as redisController



from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

#--------------------------------------------------------
#Usuarios
@app.route("/usuario/insert_sample", methods=['POST'])
@cross_origin()
def insert_sample():
    return usuarioController.inserir_amostra()

@app.route("/usuarios", methods=['GET'])
@cross_origin()
def usuarios():
	return usuarioController.find_usuarios()

@app.route("/usuario", methods=['GET'])
@cross_origin()
def usuario():
	return usuarioController.find_por_id(request)

@app.route("/usuario/create", methods=['POST'])
@cross_origin()
def usuario_create():
	return usuarioController.inserir(request)

@app.route("/usuario/delete", methods=['DELETE'])
@cross_origin()
def usuario_delete():
	return usuarioController.delete(request)

#--------------------------------------------------------
#vendedores
@app.route("/vendedores/inserir_amostra", methods=['POST'])
@cross_origin()
def inserir_amostra_vendedor():
    return vendedorController.inserir_amostra()

@app.route("/vendedores", methods=['GET'])
@cross_origin()
def vendedores():
	return vendedorController.find_vendedores()

@app.route("/vendedor", methods=['GET'])
@cross_origin()
def vendedor():
	return vendedorController.find_por_id(request)

@app.route("/vendedor/create", methods=['POST'])
@cross_origin()
def vendedor_create():
	return vendedorController.inserir(request)

@app.route("/vendedor/delete", methods=['DELETE'])
@cross_origin()
def vendedor_delete():
	return vendedorController.delete(request)

#--------------------------------------------------------
#Produtos
@app.route("/produtos/inserir_amostra", methods=['POST'])
@cross_origin()
def inserir_amostra_produtos():
    return produtoController.inserir_amostra()

@app.route("/produtos", methods=['GET'])
@cross_origin()
def produtos():
	return produtoController.find_produtos()

@app.route("/produto", methods=['GET'])
@cross_origin()
def produto():
	return produtoController.find_por_id(request)

@app.route("/produto/create", methods=['POST'])
@cross_origin()
def produto_create():
	return produtoController.inserir(request)

@app.route("/produto/delete", methods=['DELETE'])
@cross_origin()
def produto_delete():
	return produtoController.delete(request)

#--------------------------------------------------------
#Compras
@app.route("/compras/inserir_amostra", methods=['POST'])
@cross_origin()
def inserir_amostra_compras():
    return compraController.inserir_amostra()

@app.route("/compras", methods=['GET'])
@cross_origin()
def compras():
	return compraController.find_compras()

@app.route("/compra", methods=['GET'])
@cross_origin()
def compra():
	return compraController.find_por_id(request)

@app.route("/compra/create", methods=['POST'])
@cross_origin()
def compra_create():
	return compraController.inserir(request)

@app.route("/compra/delete", methods=['DELETE'])
@cross_origin()
def compra_delete():
	return compraController.delete(request)


# Redis
@app.route("/produto/redis/incremento_view", methods=['GET'])
@cross_origin()
def incrementar_view_produto():
	return redisController.incrementar_view_produto(request)

@app.route("/website/redis/incremento_view", methods=['GET'])
@cross_origin()
def incrementar_view_website():
	return redisController.incrementar_view_website()

@app.route("/website/redis/relatorio-geral", methods=['GET'])
@cross_origin()
def relatorio_geral():
	return redisController.relatorio_geral()

@app.route("/redis/delete-keys", methods=['DELETE'])
@cross_origin()
def delete_all_keys():
	return redisController.delete_all_keys()

@app.route("/redis/salvar-relatorio", methods=['POST'])
@cross_origin()
def salvar_relatorio():
	return redisController.salvar_relatorio()




if __name__ == '__main__':
	app.run(debug=True)