from sqlalchemy.sql import func

from project import db


class Tienda(db.Model):

    __tablename__ = 'tienda'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)
    sucursal = db.Column(db.String(128), nullable=False)
    direccion = db.Column(db.String(128), nullable=False)
    telefono = db.Column(db.String(128), nullable=False)
    encargado = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'sucursal': self.sucursal,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'encargado': self.encargado,
            'active': self.active
        }

    def __init__(self, nombre, sucursal, direccion, telefono, encargado):
        self.nombre = nombre
        self.sucursal = sucursal
        self.direccion = direccion
        self.telefono = telefono
        self.encargado = encargado


