var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Header = React.createClass({
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

		return(
				<div>
                    <div className="toolbar">
                      <div className="inner-container">
                      <div onClick={this.getHMenu} className="menu_">&#9776;</div>
                      <div className="side-menu">
                      <a className="side-dropdown-item" href="/createUser" data-track="menu-addinterests">
                        <span className="menu-text">Create User</span></a>

                      <a className="side-dropdown-item" href="/editUser" data-track="menu-addinterests">
                        <span className="menu-text">Edit User</span></a>
                      </div>
                        <div onClick={this.getMenu} className="menu">
                          <img src="https://nb9-stumbleupon.netdna-ssl.com/WcjiEMsHQiBUV9Q-ZK4lDg" />
                          <div className="name">mrigendra11</div>
                          <div className="fa fa-angle-down"></div>
                        <div className="dropdown-menu">
                            <a className="dropdown-item" href="/interest"><span className="menu-text">Edit Interests</span></a>
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