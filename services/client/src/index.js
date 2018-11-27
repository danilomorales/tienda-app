import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios'; //nuevo
import TiendaList from './components/TiendaList';
import AddTienda from './components/AddTienda';

//nuevo
class App extends Component {

	constructor(){
		super();
		this.state ={
			tienda: [],
			nombre: '',
			encargado: '',
			sucursal: '',
			direccion: '',
			telefono: '',
		};
		this.addTienda = this.addTienda.bind(this);
		this.handleChange = this.handleChange.bind(this);
	};

    //new
	componentDidMount() {
		this.getTienda();
	};

	// nuevo
	getTienda() {
		console.log(`${process.env.REACT_APP_TIENDA_SERVICE_URL}/tienda`);
		axios.get(`${process.env.REACT_APP_TIENDA_SERVICE_URL}/tienda`)
		.then((res) => { this.setState({ tienda: res.data.data.tienda }); }) 
		.catch((err) => { console.log(err); });
	}

	addTienda(event) {
		event.preventDefault();
		const data = {
			nombre: this.state.nombre,
			encargado: this.state.encargado,
			sucursal: this.state.sucursal,
			direccion: this.state.direccion,
			telefono: this.state.telefono
		};
		axios.post(`${process.env.REACT_APP_TIENDA_SERVICE_URL}/tienda`,data)
		.then((res) => { 
			this.getTienda();
			this.setState({ 
				nombre: '', 
				encargado: '', 
				sucursal: '', 
				direccion: '', 
				telefono: ''});
		 })
		.catch((err) => { console.log(err); });
	};

	handleChange(event){
		const obj = {};
		obj[event.target.name] = event.target.value;
		this.setState(obj);
	};

	render(){
		return (
			<section className="section">
			<div className="container">
			<div className="columns">
			<div className="column is-one-third">
			<br/>
			<h1 className="title is-1">Todos los Tiendas</h1>
			<hr/><br/>
			<AddTienda
			nombre={this.state.nombre} 
			encargado={this.state.encargado} 
			sucursal={this.state.sucursal} 
			direccion={this.state.direccion} 
			telefono={this.state.telefono} 
			addTienda={this.addTienda} 
			handleChange={this.handleChange}
			/>
			<hr/><br/>
			<TiendaList tienda={this.state.tienda}/>
			</div>
			</div>
			</div>
			</section>
		)
	}
}


ReactDOM.render(
	<App />,
	document.getElementById('root')
);
