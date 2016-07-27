var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");


var EditInterestComponent = React.createClass({

	getInitialState: function() {
	    return {
	    	data_arr: [],
	    	imageValue: '',
	    	interestValue: '',
	    	idValue: '',
	    	optionValue: '',
	    	optionValue: '',
	    	cIdValue: '',
	    	curIndVal: 0
	    };
	  },
	
	componentDidMount: function(){
		var component = this;

		$.get("http://0.0.0.0:8889/all_interest", function(response){
		
			response=JSON.parse(response)

			component.setState({
				data_arr : response.data
			});

		})

	},

	interest_list_func : function(c){

		var that=this
		$.get("http://0.0.0.0:8889/all_category", function (data){
			
			response =JSON.parse(data);
			console.log(data)

			for (var i = 0; i < response.data.length; i++) { 
				
				
				if(response.data[i]._id==c){
					console.log("matched")
					that.setState({optionData: response.data[i].category});
					that.setState({optionValue: response.data[i]._id});

				}
		
 				$(".select_").append('<option value="'+response.data[i]._id+'">'+response.data[i].category+'</option>')
 			}
		})

	},

	editInterest: function(id,ind){
		var that = this;
		
		if(that.state.data_arr[ind]._id === id){
			this.setState({
				idValue: that.state.data_arr[ind]._id,
				imageValue: that.state.data_arr[ind].image,
				interestValue: that.state.data_arr[ind].interest,
				curIndVal: ind
			});	
		}else{
			console.log("id not matched");
			this.state.data_arr.map(function(item) {					
				if(item._id==id){
					console.log(item)
					console.log("edit matched");
					console.log(item.interest);
					this.setState({idValue: item._id});
					this.setState({imageValue: item.image});				
					this.setState({
						interestValue: item.interest,
						curIndVal:ind
					});					
				}
			}.bind(this));
		}
		
		$('.edit_interest_popup').show();
		return false;
	},
	

	editPopupClose : function(){
		$('.edit_interest_popup').hide();
		return false;
	},


	handleChange: function(event,cc) {
			// console.log(cc);
	    this.setState({
	    	cc: event.target.value
	    });
	  },


	editInterest_func: function(id_v){
		var that=this
		var editInterestData = {
			_id: id_v,
			image : $('#e_url').val(),
			interest: $('#e_name').val(),
			keywords: [],
			category_id: $('.select_').val()
		};

		console.log(editInterestData)
		$.ajax({
                   type: "PUT",
                   url: "http://0.0.0.0:8889/edit_interest_data/",
                   data: JSON.stringify(editInterestData),
                   contentType: "application/json; charset=utf-8",
                   dataType: "json",
                     success: function(data){
                         console.log("success")
                         
                         var dataArrVal = that.state.data_arr;  
                                              
                         dataArrVal[that.state.curIndVal] = data.data;
                         
                         that.setState({
                         	data_arr: dataArrVal
                         });
                         
                         that.editPopupClose();
                     },
                     failure: function() {
                         console.log("error");
                     }
		        });
    },

  onClick: function(iId,cId,ind){
  	
      this.editInterest(iId,ind);
      this.interest_list_func(cId);
  },

	render: function(){
        var component=this;
        var that = this;
		return(

			<div>

			<div className='edit_interest_popup'>
					<div className='edit_interest_content'>
					<img src='close-arrow.png' className='x' id='x' onClick={this.editPopupClose}/>
							<div className="editInterest errorMsg"></div>	
							<div className="editInterestText" >Blackbird Edit Interest</div>

								<div className="editInterestForm" id={this.state.idValue}>

									<label>Image:</label>
									<input type="text" id="e_url" value={this.state.imageValue} /><br/>

									<label>Interest:</label>
									<input type="text" id="e_name" value={this.state.interestValue} onChange={this.handleChange.bind(null,'e_name') }/><br/>

									<label>Category:</label>
									<div className="interest-select" onClick={this.interest_list_func} >
										
										<select className="select_">
												<option value={this.state.optionValue}>{this.state.optionData}</option>
										</select>
										
									</div>

  									<button onClick={this.editInterest_func.bind(null,this.state.idValue)}>Edit Interest</button>
  								</div>
					</div>
			</div>  


				<div className="all_interest_outerdiv">
				{
					
					this.state.data_arr.map(function(item,i) {
						// console.log(item)
          			return (
          				<div className="all_interest_div" id={item._id} key={i}>
          				   <img src={item.image}/>
          				   <div className="name">{item.interest}</div>
          				   <img className="editIcon" src="edit-xxl.png" onClick={that.onClick.bind(null,item._id,item.category_id,i)}/>
          				</div>
          				)
      		 		})
				}
				</div>

			</div>
				
			)
	}

})

module.exports = EditInterestComponent;