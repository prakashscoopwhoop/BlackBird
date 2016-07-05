var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Login = React.createClass({

    getInitialState:function(){
            loggedIn = JSON.parse(window.localStorage.getItem("userDetail"));
            if(loggedIn=== null || loggedIn=== undefined){
            return null;
//            window.location = "/";
            }else{
            if (loggedIn.success === true){
                window.location = "/interest";
				}
				else{
//				window.location = "/";
				}
            }
		},
	getLogin : function(){


		var user = {'username':$('#usr_name').val(),'password':$('#password').val()};
        $.get("http://0.0.0.0:8889/login/"+user['username']+"/"+user['password'] , function (response) {
		 	response =JSON.parse(response);
		 	if (response['success']=== true){
		 	    window.localStorage.setItem("userDetail", JSON.stringify(response));
//		 	    console.log(JSON.parse(window.localStorage.getItem("userDetail")));
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
  									<input type="password" name="password" id="password" placeholder="Enter password..."/><br/>
  									<button onClick={this.getLogin}>Sign In</button>
  								</div>
							</div>
					</div>
				</div>
			)
	}
})

module.exports = Login;