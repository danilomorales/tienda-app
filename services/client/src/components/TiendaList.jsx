import React from 'react';


const TiendaList = (props) => {
  return (
    <div>
      {
        props.tienda.map((tienda) => {
          return (
            <h4
              key={tienda.id}
              className="box title is-4"
            >{ tienda.nombre }
            </h4>
          )
        })
      }
    </div>
  )
};


export default TiendaList;