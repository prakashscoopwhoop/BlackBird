var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var EditUser = React.createClass({
	getInitialState:function(){
            loggedIn = JSON.parse(window.localStorage.getItem("userDetail"));
            if(loggedIn=== null || loggedIn=== undefined){
            window.location = "/";
            }else{
            if (loggedIn.success === true){
			return{
				      allUser  : [],
                      allUserLoded : false,
                      user : {},
                      username : '',
                      fName : '',
                      lName : '',
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
        $.get("http://0.0.0.0:8889/all_users", function(result) {
          // console.log(result);
        console.log(JSON.parse(result).data);
        if (this.isMounted()) {
              this.setState({
                allUser  : JSON.parse(result).data,
                allUserLoded : true
              });
            }
        }.bind(this));        
     },
	
 	editUser : function(user){
 		console.log(user);
 		console.log('Edit user');
 		this.setState({
 			user : user,
 			username : user.username,
 			fName : user.first_name,
 			lName : user.last_name
 		})
 		$('.popup').show();
		return false;
	},	
	updateUser : function(){
		var that=this;
		var updatedUser = {
			first_name : $('#fName').val(),
			last_name  : $('#lName').val(),
			_id 	   : this.state.user._id 	
		}
		console.log(updatedUser);
		var url="http://0.0.0.0:8889/update_user/"+ JSON.stringify(updatedUser);
		$.post(url, function (response) {
		 	response =JSON.parse(response);
		 	// console.log(response);
		 	if (response.success){
		 		console.log('welcome');
		 		that.popupClose();
		 		 that.componentDidMount();
		 	}else
		 	{
		 	$('.errorMsg').text(response.messages);
// 
		 	}

		});
	},
	deleteUser : function(userId){
		console.log("Delete this id : "+userId);
		$.ajax({
                   type: "DELETE",
                   url: "http://0.0.0.0:8889/remove_user/"+userId,
                   contentType: "application/json; charset=utf-8",
                   dataType: "json",
                     success: function(data){
                         console.log(data);
//                         componentDidMount();
                     },
                     failure: function(err) {
                         console.log(err);
                     }
            });
	},
	popupClose : function(){
		console.log('popup close');
		$('.popup').hide();
		return false;
	},
	handleChange: function(event,cc) {
		// console.log(cc);
    this.setState({
    	cc: event.target.value
    });
  },
	render: function(){
		var that=this;
		// console.log(this.state.editUser);
		return(
			
				<div className="editUser">
<div className='popup'>
<div className='content'>
<img src='close-arrow.png' className='x' id='x' onClick={this.popupClose}/>
						<div className="cUserText errorMsg"></div>	
						<div className="cUserText">Blackbird Create User</div>
								<div className="cUserForm">

									<label>User ID:</label>
									<input type="text" name="uName" id="uName" placeholder="Enter User ID" value={this.state.username} /><br/>

									<label>First Name:</label>
									<input type="text" name="fName" id="fName" placeholder="Enter First Name" value={this.state.fName} onChange={this.handleChange.bind(null,'fName') } /><br/>

									<label>Last Name:</label>
									<input type="text" name="lName" id="lName" placeholder="Enter Last Name" value={this.state.lName} onChange={this.handleChange.bind(null, 'lName')} /><br/>


  									<button onClick={this.updateUser}>Update User</button>
  								</div>
</div>
</div>  
						<div className="cUserText">Blackbird Edit user</div>

					<div className="editUserTable">
					<table>
					<thead>
					  <tr>
					     <th>Firstname</th>
					    <th>Lastname</th>
					    <th>User ID</th>
					    <th></th>
					  </tr>
					  </thead>
					  
					  <tbody>
					 {
          this.state.allUserLoded ? this.state.allUser.map(function(item,i){
          			 return( <tr key={i}>
          			 	<td>{item.first_name}</td>
					    <td>{item.last_name}</td>					    
					    <td>{item.username}</td>
					    <td><a onClick={that.editUser.bind(null, item) } >Edit</a> / <a id={item._id} onClick={that.deleteUser.bind(null, item._id) } >Delete</a> </td>

					  </tr>)
					  
					}) : null
					}
					</tbody>
					</table>

						
					</div>
				</div>
			)
	}
})

module.exports = EditUser;