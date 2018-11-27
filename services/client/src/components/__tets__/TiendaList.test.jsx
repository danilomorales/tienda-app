import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
 
import TiendaList from '../TiendaList';
 
const Tienda = [
  {
    'active': true,
    'telefono': 202323,
    'direccion': 'Alameda',
    'sucursal': 'La era',
    'encargado': 'Jose',
    'id': 1,
    'nombre': 'TiendaC'
  },
  {
    'active': true,
    'telefono': 2523234,
    'direccion': 'Alamos',
    'sucursal': 'Alameda',
    'encargado': 'David',
    'id': 2,
    'nombre': 'TiendaD'
  }
];
 
test('TiendaList renders properly', () => {
  const wrapper = shallow(<TiendaList Tienda={Tienda}/>);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('Oreo');
});

test('TiendaList renders a snapshot properly', () => {
  const tree = renderer.create(<TiendaList Tienda={Tienda}/>).toJSON();
  expect(tree).toMatchSnapshot();
});
