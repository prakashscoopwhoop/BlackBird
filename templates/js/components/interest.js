var React = require('react');
var ReactDOM = require('react-dom');
var Slider = require('react-slick');
var $ = require("jquery");
var Header = require('./header');




var Interest = React.createClass({

getInitialState:function(){
            loggedIn = JSON.parse(window.localStorage.getItem("userDetail"));
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
				}
				else{
				window.location = "/";
				}
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
 loadCategory :function(cat, event){
    for(i=0;i<event.currentTarget.parentNode.childNodes.length;i++){
        if(event.currentTarget.parentNode.childNodes[i].children[0].className==="click-target" || event.currentTarget.parentNode.childNodes[i].children[0].className==="click-active"){
        event.currentTarget.parentNode.childNodes[i].children[0].className="click-target";
        }
    }
    if(event.target.className==="click-target" || event.target.className==="click-active"){
    event.target.className ="click-active";
    }

//      var abc=cat.replace('/','-');
//      console.log(abc);
      $.get("http://0.0.0.0:8889/interest/"+cat._id, function(result) {
          console.log(result);
//          console.log(JSON.parse(result).data);
        if (this.isMounted()) {
              this.setState({
                catData      : JSON.parse(result).data,
                catDataLoded : true
              });
            }
        }.bind(this)); 
     },
     logout :function(){
        console.log($(this));
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
                    <Header />

					<div className="welcomeDiv">
							<h1>Welcome to Blackbird!!</h1>
							<p>&nbsp;</p>
							<h3>Please select your interests..</h3>
					</div>
					
          {
          this.state.intDataLoded ? this.state.intrestData.map(function(item,i){
            sliderData.push(<li className="nav_btns_list" id={item._id} onClick={that.loadCategory.bind(null,item)}><div className="click-target">{item.category}</div></li>)
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
                      <div id={item._id} className="check"><input type="checkbox"></input></div>
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


