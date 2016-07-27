var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var CreateInterest = React.createClass({


	createInterest_func : function(){

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
				   },
				   failure: function(err) {
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
						<div className="cUserText errorMsg"></div>
						<div className="cInterestText">Create Interest</div>
								<div className="cInterestForm">

									<label>Image:</label>
									<input type="text" name="i_url" id="i_url" placeholder="Enter Image Url" required/><br/>

									<label>Interest:</label>
									<input type="text" name="i_name" id="i_name" placeholder="Enter Interest Name" required/><br/>

									<label>Category:</label>
									<div className="interest-select" onClick={this.interest_list_func}>
										
										<select className="select_">
												<option value="null">-----select-----</option>
										</select>
										
									</div>


  									<button onClick={this.createInterest_func}>Create Interest</button>
  								</div>
					</div>

					)
	}
})

module.exports = CreateInterest;
