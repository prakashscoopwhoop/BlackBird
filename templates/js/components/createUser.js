var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Login = React.createClass({
	


	getInitialState: function(){
		return {
			errorMsg: false,
			loadGifC: false,
		}
		

	},

 	createUser : function(){

 		var component = this;
 		this.setState({loadGifC: true})
 		
 		function valPassword() {
	        var password = document.getElementById("fPassword").value;
	        var confirmPassword = document.getElementById("rPassword").value;
	        if (password != confirmPassword) {
	            // alert("Passwords do not match.");
	            return false;
	        }
	        return true;
    	}

		console.log(valPassword());

		var newUser = {
			first_name : $('#fName').val(),
			last_name : $('#lName').val(),
			username   : $('#uName').val(),
			password : $('#fPassword').val(),
			interest : [],
			role	 : 'member'
		
		}

		console.log(newUser);
 		
 		$.post("http://0.0.0.0:8889/save_user/"+ JSON.stringify(newUser), function (response) {

	  		

			response =JSON.parse(response);
			console.log(response);
			console.log(response.messages);

			 	if (response.success){
			 		console.log('welcome');
			 		component.setState({loadGifC: false})

			 		// window.localStorage.setItem("userDetail",response.data);
	                window.location = "/editUser";
			 	}else{
				       		component.setState({
				       			errorMsg: true,
				       			loadGifC: false

				       		})
				       		
				       }

		});
	},	

	render: function(){

		return(
					<div className="cUser">
						{this.state.errorMsg ? <div className="cUserText errorMsg">Error: Try again</div> :null}
						{this.state.loadGifC ? <div className="loadingDiv"><img src="loading.gif" /></div> : null}
						<div className="cUserText">Create User</div>
								<div className="cUserForm">

									<label>First Name:</label>
									<input type="text" name="fName" id="fName" placeholder="Enter First Name" required/><br/>

									<label>Last Name:</label>
									<input type="text" name="lName" id="lName" placeholder="Enter Last Name" required/><br/>

									<label>User ID:</label>
									<input type="text" name="uName" id="uName" placeholder="Enter User ID" required/><br/>

									<label>password:</label>
									<input type="password" name="fPassword" id="fPassword" placeholder="Enter Password" required/><br/>

									<label>Confirm Password:</label>
									<input type="password" name="rPassword" id="rPassword" placeholder="Retype Password" /><br/>


  									<button onClick={this.createUser}>Create User</button>
  								</div>
					</div>
			)
	}
})

module.exports = Login;