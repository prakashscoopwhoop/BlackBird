var React = require('react');
var ReactDOM = require('react-dom');
var Slider = require('react-slick');
var $ = require("jquery");

var Interest = React.createClass({
getInitialState:function(){
			return{
					interests: ['a','b','c','d']
				}

		},
getMenu:function(){
    $(".dropdown-menu").toggle();
    },
	render: function(){
		
		var settings = {
	      infinite: false,
	      speed: 500,
	      slidesToShow: 10,
	      slidesToScroll: 5,
	      arrows: true,
	      initialSlide: 0
	    };

		return(
				<div>
            <div className="toolbar">
              <div className="inner-container">
                <div onClick={this.getMenu} className="menu">
                  <img src="https://nb9-stumbleupon.netdna-ssl.com/WcjiEMsHQiBUV9Q-ZK4lDg" />
                  <div className="name">mrigendra11</div>
                  <div className="fa fa-angle-down"></div>
                <div className="dropdown-menu">
                    <a className="dropdown-item" href="/discover/interests"><span className="menu-text">Edit Interests</span></a>
                    <a className="dropdown-item" href="/" ><span className="menu-text">Log Out</span></a>
                </div>
                </div>

              </div>
            </div>

					<div className="welcomeDiv">
							<h1>Welcome to Blackbird!!</h1>
							<p>&nbsp;</p>
							<h3>Please select your interests..</h3>
					</div>
					

					<div className="wrapper">
  						<ul className="navlist">
  						<Slider {...settings}>
  							<li className="nav_btns_list"><div className="click-target">Popular</div></li>
  							<li className="nav_btns_list"><div className="click-target">Arts</div></li>
  							<li className="nav_btns_list"><div className="click-target">Commerce</div></li>
  							<li className="nav_btns_list"><div className="click-target">Computers</div></li>
  							<li className="nav_btns_list"><div className="click-target">Health</div></li>
  							<li className="nav_btns_list"><div className="click-target">Hobbies</div></li>
  							<li className="nav_btns_list"><div className="click-target">Home/Living</div></li>
  							<li className="nav_btns_list"><div className="click-target">Media</div></li>
  							<li className="nav_btns_list"><div className="click-target">Music/Movies</div></li>
  							<li className="nav_btns_list"><div className="click-target">Outdoors</div></li>
  							<li className="nav_btns_list"><div className="click-target">Regional</div></li>
  							<li className="nav_btns_list"><div className="click-target">Religion</div></li>
  							<li className="nav_btns_list"><div className="click-target">Sci/Tech</div></li>
  							<li className="nav_btns_list"><div className="click-target">Society</div></li>
  							<li className="nav_btns_list"><div className="click-target">Sports</div></li>
  							</Slider>
  						</ul>
					</div>
		
					<div className="interest_container_outerdiv">

						<div className="interest_container_div" >
								<img src="https://nb9-stumbleupon.netdna-ssl.com/gvw-DEU9eQIy2hlYbZZiQA"></img>
  								<div className="name">Acting</div>
    					</div>

    					<div className="interest_container_div" >
								<img src="https://nb9-stumbleupon.netdna-ssl.com/gvw-DEU9eQIy2hlYbZZiQA"></img>
  								<div className="name">Music</div>
    					</div>

    					<div className="interest_container_div" >
								<img src="https://nb9-stumbleupon.netdna-ssl.com/gvw-DEU9eQIy2hlYbZZiQA"></img>
  								<div className="name">Logic</div>
    					</div>

    					<div className="interest_container_div" >
								<img src="https://nb9-stumbleupon.netdna-ssl.com/gvw-DEU9eQIy2hlYbZZiQA"></img>
  								<div className="name">Computers</div>
    					</div>

    					<div className="interest_container_div" >
								<img src="https://nb9-stumbleupon.netdna-ssl.com/gvw-DEU9eQIy2hlYbZZiQA"></img>
  								<div className="name">Society</div>
    					</div>

					</div>
				</div>
			)
	}
})

module.exports = Interest;


