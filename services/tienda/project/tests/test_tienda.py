# services/tienda/project/tests/test_tienda.py


import json
import unittest

from project.tests.base import BaseTestCase

from project import db
from project.api.models import Tienda


def add_tienda(nombre, encargado, sucursal, direccion, telefono):
    tienda = Tienda(
        nombre=nombre,
        encargado=encargado,
        sucursal=sucursal,
        direccion=direccion,
        telefono=telefono
    )
    db.session.add(tienda)
    db.session.commit()
    return tienda


class TestTiendaService(BaseTestCase):
    """Pruebas para el Servicio de Tiendas """

    def test_tienda(self):
        """comprobado que la ruta /ping funcione correctamente."""
        response = self.client.get('/tienda/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Conectado exitosamente!', data['mensaje'])
        self.assertIn('satisfactorio', data['estado'])

    def test_add_tienda(self):
        """ Asegurando que se pueda agregar
         un nueva tienda a la base de datos"""
        with self.client:
            response = self.client.post(
                '/tienda',
                data=json.dumps({
                    'nombre': 'Tienda Central',
                    'encargado': 'Moises',
                    'sucursal': 'Thiagos S.A',
                    'direccion': 'La alameda22',
                    'telefono': '12345678'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                'Tienda Central fue agregado!!!',
                data['mensaje'])
            self.assertIn('satisfactorio', data['estado'])

    def test_add_tienda_invalid_json(self):
        """Asegurando de que se lance un error
         cuando el objeto JSON esta vacío."""
        with self.client:
            response = self.client.post(
                '/tienda',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Datos no validos.', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_add_tienda_invalid_json_keys(self):
        """Asegurando de que se produce un error si el
         objeto JSON no tiene una clave de nombre de
          la tienda."""
        with self.client:
            response = self.client.post(
                '/tienda',
                data=json.dumps({'nombre': 'Tienda Central'}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Datos no validos.', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_add_tienda_duplicate_nombre(self):
        """Asegurando que se produce un error si
         el nombre ya existe."""
        with self.client:
            self.client.post(
                '/tienda',
                data=json.dumps({
                    'nombre': 'Tienda Central',
                    'encargado': 'Moises',
                    'sucursal': 'Thiagos S.A',
                    'direccion': 'La alameda22',
                    'telefono': '12345678'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/tienda',
                data=json.dumps({
                    'nombre': 'Tienda Central',
                    'encargado': 'Moises',
                    'sucursal': 'Thiagos S.A',
                    'direccion': 'La alameda22',
                    'telefono': '12345678'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Lo siento, ese nombre ya existe.', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_single_tienda(self):
        """Asegurando que la tienda único se comporte
         correctamente."""
        tienda = add_tienda('Tienda Central', 'Moises', 'Thiagos S.A', 'La alameda22', '12345678')
        with self.client:
            response = self.client.get(f'/tienda/{tienda.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('Tienda Central', data['data']['nombre'])
            self.assertEqual('Moises', data['data']['encargado'])
            self.assertEqual('Thiagos S.A', data['data']['sucursal'])
            self.assertIn(
                'La alameda22',
                data['data']['direccion'])
            self.assertIn(
                '12345678',
                data['data']['telefono']
                )
            self.assertIn('satisfactorio', data['estado'])

    def test_single_tienda_no_id(self):
        """Asegúrese de que se arroje un error si
         no se proporciona una identificación."""
        with self.client:
            response = self.client.get('/tienda/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn(
                'La Tienda no existe',
                data['mensaje']
                )
            self.assertIn('falló', data['estado'])

    def test_single_tienda_incorrect_id(self):
        """Asegurando de que se arroje un error si
         la identificación no existe."""
        with self.client:
            response = self.client.get('/tienda/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('La Tienda no existe', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_all_tienda(self):
        """Asegurando obtener todos los Tiendas
         correctamente."""
        add_tienda('Tienda Central', 'Moises', 'Thiagos S.A', 'La alameda22', '12345678')
        add_tienda('Tienda CentralB', 'Elena', 'Dist Panini', 'La era Mg Lt49', '987654321')
        with self.client:
            response = self.client.get('/tienda')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['tienda']), 2)
            self.assertIn(
                'Tienda Central',
                data['data']['tienda'][0]['nombre']
                )
            self.assertEqual(
                'Moises',
                data['data']['tienda'][0]['encargado']
                )
            self.assertEqual(
                'Thiagos S.A',
                data['data']['tienda'][0]['sucursal']
                )
            self.assertIn(
                'La alameda22',
                data['data']['tienda'][0]['direccion']
                )
            self.assertIn(
                '12345678',
                data['data']['tienda'][0]['telefono']
                )
            self.assertIn(
                'Tienda CentralB',
                data['data']['tienda'][1]['nombre']
                )
            self.assertEqual(
                'Elena',
                data['data']['tienda'][1]['encargado']
                )
            self.assertEqual(
                'Dist Panini',
                data['data']['tienda'][1]['sucursal']
                )
            self.assertIn(
                'La era Mg Lt49',
                data['data']['tienda'][1]['direccion']
                )
            self.assertIn(
                '987654321',
                data['data']['tienda'][1]['telefono']
                )

    def test_main_no_tienda(self):
        """Asegura que la ruta principal actua
         correctamente cuando no hay Tiendas en
          la base de datos"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Listado de <b>Tiendas</b></h2>', response.data)
        self.assertIn(
            b'<p>No tiendas!</p>',
            response.data
            )

    def test_main_with_tienda(self):
        """Asegura que la ruta principal actua
         correctamente cuando hay Tiendas en la
          base de datos"""
        add_tienda('Tienda Market', 'Cesar', 'Dist. Central', 'Villa', '95454545')
        add_tienda('Farolito', 'August', 'Dist. Mercado', 'Carapongo', '58585845')
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h2>Listado de <b>Tiendas</b></h2>', response.data)
            self.assertNotIn(
                b'<p>No tiendas!</p>',
                response.data
                )
            self.assertIn(b'Tienda Market', response.data)
            self.assertIn(b'Farolito', response.data)

    def test_main_add_tienda(self):
        """Asegura que una nueva tienda puede ser
         agregado a la db"""
        with self.client:
            response = self.client.post(
                '/',
                data=dict(
                    nombre='Tienda Tia',
                    encargado='Pedro',
                    sucursal='Dist.Tia',
                    direccion='Carretera Central Km:19.5',
                    telefono='456456465'
                    ),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h2>Listado de <b>Tiendas</b></h2>', response.data)
            self.assertNotIn(
                b'<p>No tiendas!</p>',
                response.data
                )
            self.assertIn(b'Tienda Tia', response.data)


if __name__ == '__main__':
    unittest.main()
