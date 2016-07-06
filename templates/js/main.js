
var React = require('react');
var ReactDOM = require('react-dom');
var Header = require('./components/header');
var Login = require('./components/login');
var Interest = require('./components/interest');
var CreateUser = require('./components/createUser');
var EditUser = require('./components/editUser');
var Dashboard = require('./components/dashboard');





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
