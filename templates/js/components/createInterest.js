var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var CreateInterest = React.createClass({


	createInterest_func : function(){

		var newInterest = {
			sub_category image : $('#i_url').val(),
			category_id: $('#i_name').val(),
			sub_categories: $('#i_category').val(),
			
		
		}
		
  $.post("http://0.0.0.0:8889/save_user/"+ JSON.stringify(newUser), function (response) {
		 	response =JSON.parse(response);
		 	console.log(response);
		 	console.log(response.messages);
		 	if (response.success){
		 		console.log('welcome');
		 		// window.localStorage.setItem("userDetail",response.data);
                window.location = "/dashboard";
		 	}else
		 	{
		 	$('.errorMsg').text(response.messages);

		 	}

		});
	},	
	
	render: function(){

		return(
				<div className="cInterest">
						<div className="cUserText errorMsg"></div>
						<div className="cInterestText">Blackbird Create Interest</div>
								<div className="cInterestForm">

									<label>Image:</label>
									<input type="text" name="i_url" id="i_url" placeholder="Enter Image Url" required/><br/>

									<label>Interest:</label>
									<input type="text" name="i_name" id="i_name" placeholder="Enter Interest Name" required/><br/>

									<label>Category:</label>
									<input type="text" name="i_category" id="i_category" placeholder="Enter Interest Category" required/><br/>


  									<button onClick={this.createInterest_func}>Create Interest</button>
  								</div>
					</div>


					)
	}
})

module.exports = CreateInterest;