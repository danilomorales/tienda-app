import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import AddTienda from '../AddTienda';

test('AddTienda renders properly', () => {
    const wrapper = shallow(<AddTienda/>);
    const element = wrapper.find('form');
    expect(element.find('input').length).toBe(6);
    expect(element.find('input').get(0).props.name).toBe('nombre');
    expect(element.find('input').get(1).props.name).toBe('encargado');
    expect(element.find('input').get(2).props.name).toBe('sucursal');
    expect(element.find('input').get(3).props.name).toBe('direccion');
    expect(element.find('input').get(4).props.name).toBe('telefono');
    expect(element.find('input').get(5).props.type).toBe('submit');
});

test('AddTienda renders a snapshot properly', () => {
    const tree = renderer.create(<AddTienda/>).toJSON();
    expect(tree).toMatchSnapshot();
});
