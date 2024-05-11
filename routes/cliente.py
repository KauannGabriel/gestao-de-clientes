from flask import Blueprint, render_template, request
from database.models.cliente import cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    clientee = cliente.select()
    return render_template('lista_clientes.html', clientes=clientee)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json
    novo_usuario =cliente.create(
        nome = data['nome'],
        email = data['email']
    )

    return render_template('item_cliente.html', clientes=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    return render_template('form_clientes.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):

    clientee = cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente = clientee)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    clientee = cliente.get_by_id(cliente_id)
    return render_template('form_clientes.html', cliente=clientee)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    data = request.json
    cliente_editado = cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    return render_template('item_cliente.html', clientes=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    clientee = cliente.get_by_id(cliente_id)
    clientee.delete_instance()

    return {'deleted': 'ok'}