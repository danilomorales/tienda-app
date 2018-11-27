# services/tienda/project/api/tienda.py

from flask import Blueprint, jsonify, request, render_template

from project.api.models import Tienda
from project import db

from sqlalchemy import exc


tienda_blueprint = Blueprint('tienda', __name__, template_folder='./templates')


@tienda_blueprint.route('/tienda/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'estado': 'satisfactorio',
        'mensaje': 'Conectado exitosamente!'
    })


@tienda_blueprint.route('/tienda', methods=['POST'])
def add_tienda():
    post_data = request.get_json()
    response_object = {
        'estado': 'falló',
        'mensaje': 'Datos no validos.'
    }
    if not post_data:
        return jsonify(response_object), 400
    nombre = post_data.get('nombre')
    sucursal = post_data.get('sucursal')
    direccion = post_data.get('direccion')
    telefono = post_data.get('telefono')
    encargado = post_data.get('encargado')
    try:
        tienda = Tienda.query.filter_by(encargado=encargado).first()
        if not tienda:
            db.session.add(Tienda(nombre=nombre, sucursal=sucursal, direccion=direccion, telefono=telefono, encargado=encargado))
            db.session.commit()
            response_object['estado'] = 'satisfactorio'
            response_object['mensaje'] = f'{nombre} fue agregado!!!'
            return jsonify(response_object), 201
        else:
            response_object['mensaje'] = 'Lo siento, ese nombre ya existe.'
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@tienda_blueprint.route('/tienda/<tienda_id>', methods=['GET'])
def get_single_user(tienda_id):
    """Obteniendo detalles de un unico usuario"""
    response_object = {
        'estado': 'falló',
        'mensaje': 'La Tienda no existe'
    }

    try:
        tienda = Tienda.query.filter_by(id=int(tienda_id)).first()
        if not tienda:
            return jsonify(response_object), 404
        else:
            response_object = {
                'estado': 'satisfactorio',
                'data': {
                    'id': tienda.id,
                    'nombre': tienda.nombre,
                    'sucursal': tienda.sucursal,
                    'direccion': tienda.direccion,
                    'telefono': tienda.telefono,
                    'encargado': tienda.encargado,
                    'active': tienda.active
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@tienda_blueprint.route('/tienda', methods=['GET'])
def get_all_tienda():
    """Get all tienda"""
    response_object = {
        'estado': 'satisfactorio',
        'data': {
            'tienda': [tienda.to_json() for tienda in Tienda.query.all()]
        }
    }
    return jsonify(response_object), 200


@tienda_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        sucursal = request.form['sucursal']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        encargado = request.form['encargado']
        db.session.add(Tienda(nombre=nombre, sucursal=sucursal, direccion=direccion, telefono=telefono, encargado=encargado))
        db.session.commit()
    tienda = Tienda.query.all()
    return render_template('index.html', tienda=tienda)
