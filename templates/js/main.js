
var React = require('react');
var ReactDOM = require('react-dom');
var Header = require('./components/header');
var Login = require('./components/login');
var Interest = require('./components/interest');
var CreateUser = require('./components/createUser');
var EditUser = require('./components/editUser');
var Dashboard = require('./components/dashboard');
var Error = require('./components/error');
var CreateInterest = require('./components/createInterest');
var EditInterest = require('./components/editInterest');

// console.log(state)
switch(state){

	case "header" 		  : loadHeaderScreen();
				  		  break;

	case "login" 		  : loadLoginScreen();
				  		  break;

	case "interest" 	  : loadInterestScreen();
				  		  break;
	case "createUser" 	  : loadCreateUserScreen();
				  		  break;	
	case "editUser" 	  : loadEditUserScreen();
				  		  break;
	case "dashboard"	  : loadDashboardScreen();
						  break;			  		  				  		  		  		  			  		  
    case "error" 	  	  : loadErrorScreen();
						  break;
	case "createInterest" : LoadCreateInterestScreen();
						  break;
	case "editInterest"   : LoadEditInterestScreen();
							break;

	default				  : break;
				  
}


function loadHeaderScreen(){
	var HeaderScreen = React.createClass({
		render : function(){
			return(
				<Header/>
			);
		}
	});

	ReactDOM.render(<LoginScreen/>, document.getElementById("logindiv"));

}


function loadLoginScreen(){
	var LoginScreen = React.createClass({
		render : function(){
			return(
				<Login/>
			);
		}
	});

	ReactDOM.render(<LoginScreen/>, document.getElementById("logindiv"));

}




function loadInterestScreen(){
	var InterestScreen  = React.createClass({
		render : function(){
			return(
				<Interest/>
			);
		}
	});


	ReactDOM.render(<InterestScreen/>, document.getElementById("interestdiv"));
}

function loadCreateUserScreen(){
	var CreateUserScreen= React.createClass({
		render : function(){
			return(
				<div>
				 <Header />
				<CreateUser />
				</div>
			);
		}
	});
	ReactDOM.render(<CreateUserScreen/>, document.getElementById("createUser"));
}

function loadEditUserScreen(){
	var EditUserScreen= React.createClass({
		render : function(){
			return(
				<div>
				 <Header />
				<EditUser />
				</div>
			);
		}
	});
	ReactDOM.render(<EditUserScreen/>, document.getElementById("editUser"));
}

function loadDashboardScreen(){
	var DashboardScreen= React.createClass({
		render : function(){
			return(
			<div>
				 <Header />
				<Dashboard />
			</div>	
			);
		}
	});
	ReactDOM.render(<DashboardScreen />, document.getElementById("dashboard"));
}

function loadErrorScreen(){
	var ErrorScreen= React.createClass({
		render : function(){
			return(
			<div>
				<Error />
			</div>
			);
		}
	});
	ReactDOM.render(<ErrorScreen />, document.getElementById("error"));
}



function LoadCreateInterestScreen(){
	var CreateInterestScreen= React.createClass({
		render : function(){
			return(
			<div>
			 <Header />
				<CreateInterest />
			</div>
			);
		}
	});
	ReactDOM.render(<CreateInterestScreen />, document.getElementById("createInterest"));
}


function LoadEditInterestScreen(){

	var EditInterestScreen= React.createClass({
		render :function(){
			return(
					<div>
						<Header />
						<EditInterest />
					</div>
				)
		}
	});
	ReactDOM.render(<EditInterestScreen />, document.getElementById("editInterest"));
}




