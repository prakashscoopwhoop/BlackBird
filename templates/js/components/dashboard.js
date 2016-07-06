var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Dashboard = React.createClass({
	

	render: function(){

		return(
				<div className="dashboard">
						<div className="cUserText">Blackbird dashboard</div>
						<div>
						<ul className="menu">
						  <li><a href="">Home</a></li>
						  <li className="dropdown">
						    <a href="">Service</a>
						    <ul className="submenu">
						      <li>
						        <a href="">submenu 1</a>
						      </li>      
						      <li>
						        <a href="">submenu 2</a>
						      </li>
						    </ul>
						  </li>
						  <li><a href="">Other</a></li>
						</ul>
						</div>
				</div>
			)
	}
})

module.exports = Dashboard;