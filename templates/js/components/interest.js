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
                                catDataLoded : false,
//                                myInterestExists: false
                                myInterestData: [],
                                myIntDataLoaded : false
                  			}

				            }else{
            				window.location = "/";
            				}
            }
  		},

    componentDidMount: function() {
      var that = this;
      var myInterestExists = false;
          $.get("http://0.0.0.0:8889/my_interest/"+loggedIn.data._id, function(result) {
                
                console.log(JSON.parse(result).data.length)
                if(JSON.parse(result).data.length>0){
                    myInterestExists = true;
                    $("#my_interest").show();
                    console.log("my interest exist")
                    that.loadMyInterest();
                }else{
                    myInterestExists = false;
                    $("#my_interest").hide();
              }
          }),


          $.get("http://0.0.0.0:8889/all_category", function(result) {
          console.log(result);
            if (this.isMounted()) {
                  this.setState({
                    intrestData  : JSON.parse(result).data,
                    intDataLoded : true
                  });
                  console.log("lfCat");
                  console.log(JSON.parse(result).data[0],myInterestExists);
                  if(myInterestExists == false){
                    that.loadCategory(JSON.parse(result).data[0],null);                      
                  }
                  
            }

          }.bind(this));        
    },

     loadCategory :function(cat, event){ 

//        for(i=0;i<event.currentTarget.parentNode.childNodes.length;i++){
//              if(event.currentTarget.parentNode.childNodes[i].children[0].className==="click-target" || event.currentTarget.parentNode.childNodes[i].children[0].className==="click-active"){
//                  event.currentTarget.parentNode.childNodes[i].children[0].className="click-target";
//              }
//        }
//
//        if(event.target.className==="click-target" || event.target.className==="click-active"){
//            event.target.className ="click-active";
//        }
        console.log(cat);
       $.get("http://0.0.0.0:8889/interest/"+cat._id, function(result) {

          if (this.isMounted()) {
                this.setState({
                  catData      : JSON.parse(result).data,
                  catDataLoded : true,
                  myIntDataLoaded : false
                });
              }
          }.bind(this)); 
     },

     loadMyInterest :function(){
            $.get("http://0.0.0.0:8889/my_interest/"+loggedIn.data._id, function(result) {
            console.log(JSON.parse(result).data);
            if (this.isMounted()) {
                  this.setState({
                    myInterestData  : JSON.parse(result).data,
                    myIntDataLoaded : true,
                    catDataLoded    : false
                  });
            }

          }.bind(this));
     },

    chooseInterest : function(id){

          console.log(id);
          console.log(loggedIn.data._id);

          var userId=loggedIn.data._id;
          var interestId=id;
          var ar = [];
          ar.push(id);


              $.ajax({
                   type: "PUT",
                   url: "http://0.0.0.0:8889/set_interest/"+loggedIn.data._id+"/"+ar,
                   contentType: "application/json; charset=utf-8",
                   dataType: "json",
                     success: function(data){
                         window.localStorage.setItem("userDetail", JSON.stringify(data));
                     },
                     failure: function(err) {
                         console.log(err);
                     }
            });
            },  

	render: function(){
		var that=this;
		var settings = {
	      initialSlide: 0,
          infinite: false,
          speed: 300,
          slidesToShow: 8,slidesToScroll: 3,
          variableWidth: true

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
            sliderData.push(<li key={i} className="nav_btns_list" id={item._id} onClick={that.loadCategory.bind(null,item)}><div className="click-target" id={'posts' +item._id} >{item.category}</div></li>)
          }) : null
         }
					<div className="wrapper">
  						<ul className="navlist">
  						<Slider {...settings}>
  							<li key='99' className="nav_btns_list" id="my_interest" onClick={this.loadMyInterest} ><div className="click-target" id="my_interest">My Interest</div></li>
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
                      <div className="check"><input type="checkbox" id={item._id} checked={that.state.complete} ref="complete" onChange={that.chooseInterest.bind(null,item._id)}/></div>
                    </div>
              )
            }):null
          }

          { this.state.myIntDataLoaded ? this.state.myInterestData.map(function(item, i){
              return (
                    <div key={i} className="interest_container_div" >
                      <img src={item.image}></img>
                      <div className="name">{item.interest}</div>

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


