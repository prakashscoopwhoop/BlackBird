var React = require('react');
var ReactDOM = require('react-dom');
var Slider = require('react-slick');
var $ = require("jquery");
var Header = require('./header');


var Interest = React.createClass({

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

    componentDidMount: function() {
         
          $.get("http://0.0.0.0:8889/all_category", function(result) {
          
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

       $.get("http://0.0.0.0:8889/interest/"+cat._id, function(result) {

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

    choose_interest : function(id){

          console.log(id)
          console.log(loggedIn.data._id)

          var userId=loggedIn.data._id
          var interestId=id
         


              $.ajax({
                   type: "PUT",
                   url: "http://0.0.0.0:8889/set_interest/"+loggedIn.data._id+"/"+id,
                   contentType: "application/json; charset=utf-8",
                   dataType: "json",
                     success: function(data){
                         console.log(data);
                     },
                     failure: function(err) {
                         console.log(err);
                     }
            });

              // $.put("http://0.0.0.0:8889/set_interest/"+loggedIn.data._id+"/"+id, function(response) {

              //         console.log(response)
              //       });
           
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
            sliderData.push(<li key={i} className="nav_btns_list" id={item._id} onClick={that.loadCategory.bind(null,item)}><div className="click-target">{item.category}</div></li>)
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
                    <div key={i} className="interest_container_div" >
                      <img src={item.image}></img>
                      <div className="name">{item.interest}</div>
                      <div className="check"><input type="checkbox" id={item._id} checked={that.state.complete} ref="complete" onChange={that.choose_interest.bind(null,item._id)}/></div>
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


