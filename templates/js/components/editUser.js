var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Login = React.createClass({
	
 	editUser : function(){
 		console.log('Edit user');
	},	

	render: function(){

		return(
				<div className="editUser">
						<div className="cUserText">Blackbird Edit user</div>

					<div className="editUserTable">
					<table>
					  <thead>
					  <tr>
					     <th>Firstname</th>
					    <th>Lastname</th>
					    <th>User ID</th>
					    <th>Password</th>
					    <th>Role</th>
					    <th></th>
					  </tr>
					  </thead>
					  
					  <tbody>
					  
					  <tr>
					     <td>&nbsp; </td>
					    <td>&nbsp; </td>
					    <td>&nbsp; </td>
					    <td>&nbsp; </td>
					    <td>&nbsp; </td>
					    <td><a href="#">Edit</a> / <a href="#">Delete</a> </td>

					  </tr>
					  </tbody>
					</table>


						
					</div>
				</div>
			)
	}
})

module.exports = Login;