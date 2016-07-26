var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Header = React.createClass({
    getInitialState:function(){

          loggedIn = JSON.parse(window.localStorage.getItem("userDetail"));

          complete: (!!this.props.complete) || false
              if(loggedIn=== null || loggedIn=== undefined){
                  window.location = "/";
              }else{

                    if (loggedIn.success === true){

                        return{
                  				intrestData  : [],
                          intDataLoded : false,
                          catData      : [],
                          catDataLoded : false
                  			}

				            }else{
            				window.location = "/";
            				}
            }
  		},
 	getHMenu: function(){
        $(".side-menu").toggle();
    },
    getMenu:function(){
        $(".dropdown-menu").toggle();
    },
    logOut:function(){
        window.localStorage.removeItem("userDetail");
        window.location = "/";
    },

	render: function(){
    console.log("check")

		return(
				<div>
                    <div className="toolbar">
                        <div className="inner-container">
                            <div onClick={this.getHMenu} className="menu_"><img src="menu-icon.png"/></div>
                                <div className="side-menu">
                                    <a className="side-dropdown-item" href="/dashboard" data-track="menu-addinterests">
                                        <span className="menu-text">Dashboard</span>
                                    </a>
                                    <a className="side-dropdown-item" href="/createUser" data-track="menu-addinterests">
                                        <span className="menu-text">Create User</span>
                                    </a>

                                    <a className="side-dropdown-item" href="/editUser" data-track="menu-addinterests">
                                        <span className="menu-text">Edit User</span>
                                    </a>

                                    <a className="side-dropdown-item" href="/createInterest" data-track="menu-addinterests">
                                        <span className="menu-text">Create Interest</span>
                                    </a>

                                    <a className="side-dropdown-item" href="/editInterest" data-track="menu-addinterests">
                                        <span className="menu-text">Edit Interest</span>
                                    </a>

                                </div>
                                <div onClick={this.getMenu} className="menu">
                                    <img src="profile.png" />
                                    <div className="name">{loggedIn.data.first_name}</div>
                                    <div><img className="dropdown-img" src="drop-down-arrow.png"/></div>
                                    
                                    <div className="dropdown-menu">
                                        <a className="dropdown-item" href="/interest"><span className="menu-text">My Interests</span></a>
                                        <a className="dropdown-item" href="/" ><span onClick={this.logOut} className="menu-text">Log Out</span></a>
                                    </div>
                                </div>
                            </div>
                        </div>
				            </div>
			)
	}
})

module.exports = Header;
