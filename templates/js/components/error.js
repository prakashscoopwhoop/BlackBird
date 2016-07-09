var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Error = React.createClass({


	render: function(){

		return(
			<div>
                <div className="errorContainer">
                    <img className="errorimg" src="error404.jpg"></img>
                </div>
			</div>
			)
	}
})

module.exports = Error;