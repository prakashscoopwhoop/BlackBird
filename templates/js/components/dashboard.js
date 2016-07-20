var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Dashboard = React.createClass({
	
	render: function(){

		return(
			<div>
					<div className="styled-select ">
							
							<select>
							  <option value="volvo">Sports</option>
							  <option value="saab">Music</option>
							  <option value="opel">Books</option>
							  <option value="audi">News</option>
							</select>
							
						</div>

				<div className="dashboard">

						<div className="cUserText">Blackbird Dashboard</div>
				</div>
				


				<div id="trends_div">
						<span>Trends</span>

						<div className="trends_inner_div">
						<ul>

							<li><a href="http://digg.com/">#CiscoDigitizingIndia</a></li>
							<li><a href="http://digg.com/">#rise</a></li>
							<li><a href="http://digg.com/">#makeme</a></li>
							<li><a href="http://digg.com/">#girlstalk</a></li>
							<li><a href="http://digg.com/">darjeeling</a></li>
							<li><a href="http://digg.com/">afterallthistime</a></li>

						</ul>
						</div>

				</div>


				<div className="feature_article_div">
						<img src="http://static.digg.com/images/f5a2f442a7ac49f38d87e8713d4f6a21_29PKgLF_1_www_large_thumb.jpeg"></img>
						
						<h2 className="article_title"><a href="http://digg.com/">Our Fancy Foods, Ourselves</a></h2>
						
						<span className="article_source"><a href="http://digg.com/">The New York Times</a></span>
						
						<div className="article_description">
							Three days at the worlds greatest assemblage of exotic, expensive, absurd, and occasionally delicious snacks
						</div>

						<div className="shareIcons">
							<img src="facebook_share.png"/>
							<img src="twitter_share.png"/>
							<img src="gplus_share.png"/>
						</div>
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
									<img src="facebook_share.png"/>
									<img src="twitter_share.png"/>
									<img src="gplus_share.png"/>
								</div>
						</div>


						<div className="article_div">
								<img src="http://static.digg.com/images/4680c447617742b18b574fbd9c731ef6_29U1w4Y_1_www_large_thumb.jpeg"></img>
								
								<h2 className="article_title"><a href="http://digg.com/">North Koreas Anti-Smoking Campaign Is A Battle Of The Sexes</a></h2>
								
								<span className="article_source"><a href="http://digg.com/">The New York Times</a></span>
								
								<div className="article_description">						
										Smoking is oddly gendered  North Korea. More than half the men smoke
										resulting  one of the highest rates of lung cancer  the worl
										allegedly at least, none of the womenSo the regime is turning to feminine
										scolding to  to fix the problem.                         
								</div>

								<div className="shareIcons">
									<img src="facebook_share.png"/>
									<img src="twitter_share.png"/>
									<img src="gplus_share.png"/>
								</div>
						</div>


						<div className="article_div">
								<img src="http://static.digg.com/images/fd258a4cf9fc45ed96cb6b72f1ce6ae1_63d1a54af55c67de6166431468a4f5b7_1_www_large_thumb.jpeg"></img>
								
								<h2 className="article_title"><a href="http://digg.com/">The Social And Economic Impact Of 'Pokémon Go'</a></h2>
								
								<span className="article_source"><a href="http://digg.com/">The New York Times</a></span>
								
								<div className="article_description">						
										
								Its only been out for five days and, yet, the popular game is still
								managing to impact markets and the ways we relate to one another.
								</div>

								<div className="shareIcons">
									<img src="facebook_share.png"/>
									<img src="twitter_share.png"/>
									<img src="gplus_share.png"/>
								</div>
						</div>
				</div>
			</div>
			)
	}
})

module.exports = Dashboard;
