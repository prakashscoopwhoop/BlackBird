var React = require('react');
var ReactDOM = require('react-dom');
var $ = require("jquery");

var Dashboard = React.createClass({

    getInitialState:function(){
            loggedIn = JSON.parse(window.localStorage.getItem("userDetail"));
            if(loggedIn=== null || loggedIn=== undefined){
            return null;
            }else{
            if (loggedIn.success === true){
                if (loggedIn.data.interest.length <=0)
                {
                window.location = "/interest";
                }
                else{
                return{
                    interestData  : [],
                    intDataLoaded : false,
                    featuredArticleData  : [],
                    featuredArticleLoaded : false,
                    articleData  : [],
                    articleLoaded : false
                    }
                }
				}
            }
            return null;
		},

		renderArticle(interestList) {
        console.log(interestList);
        var interests = [];
        for(i=0; i<interestList.length; i++){
            interests.push(interestList[i].interest);
        }
        $.get("http://0.0.0.0:8889/get_article/"+interests, function(result) {
            console.log(JSON.parse(result).data);
            var featureItem = [], restItem = [];
            if(JSON.parse(result).data.length===1){
                this.setState({
                    featuredArticleLoaded : true,
                    articleLoaded : false
                  });
            }
            else if(JSON.parse(result).data.length>1){
                this.setState({
                    featuredArticleLoaded : true,
                    articleLoaded : true
                  });
            }else{
            this.setState({
                    featuredArticleLoaded : false,
                    articleLoaded : false
                  });
            }
            for(i=0; i<JSON.parse(result).data.length; i++){
                if(i===0){
                    featureItem.push(JSON.parse(result).data[i]);
                }else{
                    restItem.push(JSON.parse(result).data[i]);
                }

            }

            if (this.isMounted()) {
                  this.setState({
                    featuredArticleData  : featureItem,
                    featuredArticleLoaded : true,
                    articleData  : restItem,
                    articleLoaded : true
                  });
            }
        }.bind(this));
    },
    change:function(event){
        var clicked = event.target.value;
        if (clicked === "all"){
        this.renderArticle(this.state.interestData);

        }
        else{
            for(i=0; i< this.state.interestData.length; i++){
            if(clicked===this.state.interestData[i]._id){
//            this.renderArticle(this.state.interestData[i]);
                console.log(this.renderArticle([this.state.interestData[i]]),this.state.interestData[i]._id);
            }
            }
        }

		},
	componentDidMount: function() {

          $.get("http://0.0.0.0:8889/my_interest/"+loggedIn.data._id, function(result) {
            console.log(JSON.parse(result).data);
            if (this.isMounted()) {
                  this.setState({
                    interestData  : JSON.parse(result).data,
                    intDataLoaded : true
                  });
            }
           this.renderArticle(JSON.parse(result).data);
          }.bind(this));
    },
	render: function(){
	var that = this;
        var optionList = [];
		return(
			<div>
					<div className="styled-select">

                            {
                                  this.state.intDataLoaded ? this.state.interestData.map(function(item,i){
                                    optionList.push(<option key={i} id={item._id} value={item._id}  >{item.interest}</option>)
                                  }) : null
                                 }
                            <select onChange={this.change} value={this.state.value}>
                            <option id="all" value="all" >all</option>
                                {optionList}
							</select>


						</div>

				<div className="dashboard">

						<div className="cUserText">Dashboard</div>
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

                {
          this.state.featuredArticleLoaded ? this.state.featuredArticleData.map(function(item,i){
          			 return(

				<div key={i} className="feature_article_div">
						<img src={item.feature_image}></img>

						<h2 className="article_title"><a href={item.url}>{item.title}</a></h2>

						<span className="article_source"><a href={item.url}>{item.publisher}</a></span>

						<div className="article_description">
							{item.description}
						</div>

						<div className="shareIcons">
							<img src="facebook_share.png"/>
							<img src="twitter_share.png"/>
							<img src="gplus_share.png"/>
						</div>
				</div>
                )
                }) : null
                }

				<div id="articles_container">
                        {
          this.state.articleLoaded ? this.state.articleData.map(function(item,i){
          			 return(

						<div key={i} className="article_div">
								<img src={item.feature_image}></img>

								<h2 className="article_title"><a href={item.url}>{item.title}</a></h2>

								<span className="article_source"><a href={item.url}>{item.publisher}</a></span>

								<div className="article_description">
								{item.description}
								</div>

								<div className="shareIcons">
									<img src="facebook_share.png"/>
									<img src="twitter_share.png"/>
									<img src="gplus_share.png"/>
								</div>
						</div>

						)

					}) : null
					}



				</div>
			</div>
			)
	}
})

module.exports = Dashboard;
