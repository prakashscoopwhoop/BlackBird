var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var CreateInterest = React.createClass({


	getInitialState: function(){

		return{
				loadGif: false,
				errMsg: false
		}
	},

	createInterest_func : function(){

		this.setState({loadGif: true})
		var component=this

		var newInterest = {
			image : $('#i_url').val(),
			interest: $('#i_name').val(),
			keywords: [],
			category_id: $('.select_').val()
		};
		console.log(newInterest);


		$.ajax({
			   type: "POST",
			   url: "http://0.0.0.0:8889/add_interest/",
			   data: JSON.stringify(newInterest),
			   contentType: "application/json; charset=utf-8",
			   dataType: "json",
				   success: function(data){
				       console.log(data);
				       console.log("success")
				       component.setState({loadGif: false})
				       if(data.success==true){
				       	window.location = "/editInterest"
				       }
				       else{
				       		component.setState({errMsg: true})
				       }

				   },
				   error: function(err) {
				   		console.log("err")
				       console.log(err);
				   }
				});
	},	
	

	interest_list_func : function(){

		$.get("http://0.0.0.0:8889/all_category", function (data){
			
			response =JSON.parse(data);

			for (var i = 0; i < response.data.length; i++) { 
		
 				$(".select_").append('<option value="'+response.data[i]._id+'">'+response.data[i].category+'</option>')
 			}
		})

	},
	
	render: function(){

		return(
				<div className="cInterest">
					{this.state.loadGif ? <div className="loadingDiv"><img src="loading.gif" /></div> : null}
						{this.state.errMsg ? <div className="cUserText errorMsg">ERROR: Try Again..</div> : null}
						<div className="cInterestText">Create Interest</div>
								<div className="cInterestForm">

									<label>Category:</label>
									<div className="interest-select" onClick={this.interest_list_func}>
										
										<select className="select_">
												<option value="null">-----select-----</option>
										</select>
										
									</div>

									<label>Interest:</label>
									<input type="text" name="i_name" id="i_name" placeholder="Enter Interest Name" required/><br/>

									<label>Image:</label>
									<input type="text" name="i_url" id="i_url" placeholder="Enter Image Url" required/><br/>

  									<button onClick={this.createInterest_func}>Create</button>
  								</div>
					</div>

					)
	}
})

module.exports = CreateInterest;
