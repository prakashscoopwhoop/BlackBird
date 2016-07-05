var React = require('react');
var ReactDOM = require('react-dom');
var Slider = require('react-slick');
var $ = require("jquery");




var Interest = React.createClass({
getInitialState:function(){
			return{
					intrestData  : [],
          intDataLoded : false,
          catData      : [],
          catDataLoded : false 

				}

		},
componentDidMount: function() {
      // var url=rootApi+"all_category";
      // console.log(url);
        $.get("http://0.0.0.0:8889/all_category", function(result) {
          console.log(result);
          console.log(JSON.parse(result).data);
        if (this.isMounted()) {
              this.setState({
                intrestData  : JSON.parse(result).data,
                intDataLoded : true
              });
            }
        }.bind(this));        
     },
 loadCategory :function(cat){
      console.log('sss'+cat)
      var abc=cat.replace('/','-');
      console.log(abc);
      $.get("http://0.0.0.0:8889/interest/"+abc, function(result) {
          console.log(result);
          console.log(JSON.parse(result).data);
        if (this.isMounted()) {
              this.setState({
                catData      : JSON.parse(result).data,
                catDataLoded : true
              });
            }
        }.bind(this)); 
     },

getHMenu: function(){
$(".side-menu").toggle();
},
getMenu:function(){
    $(".dropdown-menu").toggle();
    },
	render: function(){
		var that=this;
		var settings = {
	      infinite: false,
	      speed: 500,
	      slidesToShow: 10,
	      slidesToScroll: 5,
	      arrows: true,
	      initialSlide: 0
	    };
      var sliderData = [];


		return(
				<div>
            <div className="toolbar">
              <div className="inner-container">
              <div onClick={this.getHMenu} className="menu_">&#9776;</div>
              <div className="side-menu">
              </div>
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
					
          {
          this.state.intDataLoded ? this.state.intrestData.map(function(item,i){
            sliderData.push(<li className="nav_btns_list" id={i} onClick={that.loadCategory.bind(null,item)}><div className="click-target">{item}</div></li>)
          }) : null
         }
					<div className="wrapper">
  						<ul className="navlist">
  						<Slider {...settings}>
  							
                  {sliderData}
                                
                              
  							</Slider>
  						</ul>
					</div>
		
					<div className="interest_container_outerdiv">

            { this.state.catDataLoded ? this.state.catData.map(function(item, i){
              return (
                    <div className="interest_container_div" >
                      <img src={item.image}></img>
                      <div className="name">{item.sub_category}</div>
                    </div>
              )
            }):null
          } 

						

    					

					</div>
				</div>
			)
	}
})

module.exports = Interest;


