var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Login = React.createClass({


	getLogin : function(){


		var user = {'username':$('#usr_name').val(),'password':$('#password').val()};
        $.get("http://0.0.0.0:8889/login/"+user['username']+"/"+user['password'] , function (response) {
		 	response =JSON.parse(response);
		 	if (response['success']=== true){
                window.location = "http://0.0.0.0:8889/interest";
		 	}else
		 	{
		 	alert(response["messages"]);
		 	}

		});
	},	

	render: function(){

		return(
				<div>
					<div className="loginMainDiv">
						<div className="loginWelcomeText">Blackbird</div>
						<div className="logoDiv"><a href="#"></a></div>
							<div className="loginFormOuterDiv">
								<div className="loginFormDiv">
									<label>Sign in<br/>to your account</label>
									<input type="text" name="usr_name" id="usr_name" placeholder="Enter username..." /><br/>
  									<input type="text" name="password" id="password" placeholder="Enter password..."/><br/>
  									<button onClick={this.getLogin}>Sign In</button>
  								</div>
							</div>
					</div>
				</div>
			)
	}
})

module.exports = Login;