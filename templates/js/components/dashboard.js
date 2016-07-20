var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Dashboard = React.createClass({
	

	render: function(){

		return(
			<div>


				<div className="dashboard">
						<div className="cUserText">Blackbird dashboard</div>
				</div>


				<div id="articles_container">

						<div className="article_div">
								<img src="http://static.digg.com/images/d5d47f7ccc80428a8e495a48b96ae3f8_29yWUPu_5_www_large_thumb.jpeg"></img>
								
								<h2 className="article_title"><a href="http://digg.com/">The Town Where Everyone Is Allergic To Life</a></h2>
								
								<span className="article_source"><a href="http://digg.com/">The New York Times</a></span>
								
								<div className="article_description">
								A small community in Arizona has retreated into the desert to escape modern life, but few medical professionals believe that their self-diagnosed illnesses are real.
								</div>

								<div className="shareIcons">
									<img src="fb-icon.png"/>
									<img src="twitter-icon.png"/>
									<img src="google_icon.png"/>
								</div>
						</div>


						<div className="article_div">
								<img src="http://static.digg.com/images/4680c447617742b18b574fbd9c731ef6_29U1w4Y_1_www_large_thumb.jpeg"></img>
								
								<h2 className="article_title"><a href="http://digg.com/">North Korea’s Anti-Smoking Campaign Is A Battle Of The Sexes</a></h2>
								
								<span className="article_source"><a href="http://digg.com/">The New York Times</a></span>
								
								<div className="article_description">						
										Smoking is oddly gendered in North Korea. More than half the men smoke  —
										resulting in one of the highest rates of lung cancer in the world  — while,
										allegedly at least, none of the women do. So the regime is turning to feminine
										scolding to try to fix the problem.                         
								</div>

								<div className="shareIcons">
									<img src="/Users/Yu/Documents/githubSW/blackbird/BlackBird/templates/images/fb-icon.png"/>
									<img src="/Users/Yu/Documents/githubSW/blackbird/BlackBird/templates/images/twitter-icon.png"/>
									<img src="/Users/Yu/Documents/githubSW/blackbird/BlackBird/templates/images/google_icon.png"/>
								</div>
						</div>
				</div>
			</div>
			)
	}
})

module.exports = Dashboard;