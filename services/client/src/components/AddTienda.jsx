import React from 'react';
const AddTienda= (props) => {
    return (
    <form onSubmit={(event) => props.addTienda(event)}>
        <div className="field">
        <input
        name="nombre"
        className="input is-large"
        type="text"
        placeholder="Enter a nombre"
        required
        value={props.nombre}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="encargado"
        className="input is-large"
        type="text"
        placeholder="Enter encargado"
        required
        value={props.encargado}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="sucursal"
        className="input is-large"
        type="text"
        placeholder="Enter sucursal"
        required
        value={props.sucursal}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="direccion"
        className="input is-large"
        type="text"
        placeholder="Enter direccion"
        required
        value={props.direccion}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="telefono"

        className="input is-large"
        type="text"
        placeholder="Enter telefono"
        required
        value={props.telefono}
        onChange={props.handleChange}
        />
        </div>
        <input
        type="submit"
        className="button is-primary is-large is-fullwidth"
        value="Submit"
        />
        </form>
        )
    };

export default AddTienda;