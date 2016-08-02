var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Login = React.createClass({

    getInitialState:function(){
            loggedIn = JSON.parse(window.localStorage.getItem("userDetail"));
            if(loggedIn=== null || loggedIn=== undefined){
            return null;
            }else{
            if (loggedIn.success === true){
                if (loggedIn.data.interest.length >0)
                {
                window.location = "/dashboard";
                }
                else{
                window.location = "/interest";
                }
				}
                return null;
            }
		},
	getLogin : function(){


		var user = {'username':$('#usr_name').val(),'password':$('#password').val()};
        $.get("http://0.0.0.0:8889/login/"+user['username']+"/"+user['password'] , function (response) {
		 	response =JSON.parse(response);
		 	if (response['success']=== true){
		 	    window.localStorage.setItem("userDetail", JSON.stringify(response));
                if (response.data.interest.length >0)
                {
                window.location = "/dashboard";
                }
                else{
                window.location = "/interest";
                }
		 	}else
		 	{
		 	alert(response["messages"]);
		 	}

		});
	},
    getKeypress : function(e){
    if (e.charCode == 13) {
        this.getLogin();
      }
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
									<input type="text" name="usr_name" id="usr_name"  placeholder="Enter username..." /><br/>
  									<input type="password" name="password" id="password" onKeyPress={this.getKeypress} placeholder="Enter password..."/><br/>
  									<button onClick={this.getLogin}>Sign In</button>
  								</div>
							</div>
					</div>
				</div>
			)
	}
})

module.exports = Login;