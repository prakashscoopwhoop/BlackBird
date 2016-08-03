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
                    articleLoaded : false,
                    trendBtn :true,
                    twitterBtn :false,
                    toptweetBtn : false,
                    trendsData: [],
                    }
                }
				}
            }
            return null;
		},

		renderArticle(interests) {
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
            }else if(JSON.parse(result).data.length<1){
            this.setState({
                    featuredArticleLoaded : false,
                    articleLoaded : false,
                    featuredArticleData  : [],
                    articleData : []
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
        var interests = [];
        for(i=0; i< this.state.interestData.length; i++){
        if(clicked==="all"){
            interests.push(this.state.interestData[i].interest);
        }if(clicked===this.state.interestData[i]._id){
            interests.push(this.state.interestData[i].interest);
        }
        }
            this.renderArticle(interests);
		},

        trendsFunc:function(){
            var component = this
            this.setState({
                trendBtn: true,
                twitterBtn: false,
                toptweetBtn: false
            })
            console.log("trends")

            $.get('http://0.0.0.0:8889/group', function(data){

                console.log(data)
               
                component.setState({
                    trendsData :JSON.parse(data).data
                })


            })
        },

        twitterFunc:function(){

            this.setState({
                twitterBtn: true,
                trendBtn: false,
                toptweetBtn: false
            })
            console.log("twitter")
        },

        toptweetFunc:function(){

            this.setState({
                toptweetBtn:true,
                trendBtn: false,
                twitterBtn: false
            })
        },

        groupFunc:function(g_id){
            console.log(g_id)

$.get(" http://0.0.0.0:8889/group/"+g_id, function(data){

console.log(data)
})

            
        },

	componentDidMount: function() {

          $.get("http://0.0.0.0:8889/my_interest/"+loggedIn.data._id, function(result) {
          var interests = [];
            console.log(JSON.parse(result).data);
            if (this.isMounted()) {
                  this.setState({
                    interestData  : JSON.parse(result).data,
                    intDataLoaded : true
                  });
            }
            for(i=0;i<JSON.parse(result).data.length; i++){
            interests.push(JSON.parse(result).data[i].interest);
            }
           this.renderArticle(interests);
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
				

                <div className="top-container">


 {
          this.state.featuredArticleLoaded ? this.state.featuredArticleData.map(function(item,i){
          			 
                     return(

				<div key={i} className="feature">
						<div className="feature-left">
						<img src={item.feature_image}></img>
                        </div>
                        <div className="feature-right">
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
				</div>
                )
                }) : null
                }

                <div id="trends_div">
						
                        <div className="span_div">
                            <span id="trending" onClick={this.trendsFunc}>Trending</span>
                            <span id="twitter" onClick={this.twitterFunc}>Twitter</span>
                            <span id="topTweets" onClick={this.toptweetFunc}>TopTweets</span>
                        </div>




{
        this.state.trendBtn ? this.state.trendsData.map(function(item,i){
            // console.log(item)
            return(<div className="trends_inner_div" key={i}>

                <ul>
                        <li id={item._id} onClick={that.groupFunc.bind(null, item._id)}><img className="trending" src="trending_up.png"></img>{item.passphrase[0]}</li>
                </ul>

            </div>
            )
            
        }):(this.state.twitterBtn ?   <div className="twitter_inner_div">
                        <ul>
                            <li><img className="trending" src="trending_up.png"></img><a href="http://digg.com/">abcdefgh</a></li>
                            <li><img className="trending" src="trending_up.png"></img><a href="http://digg.com/">abcdefgh</a></li>
                            <li><img className="trending" src="trending_up.png"></img><a href="http://digg.com/">abcdefgh</a></li>
                            <li><img className="trending" src="trending_up.png"></img><a href="http://digg.com/">abcdefgh</a></li>
                            <li><img className="trending" src="trending_up.png"></img><a href="http://digg.com/">abcdefgh</a></li>
                            <li><img className="trending" src="trending_up.png"></img><a href="http://digg.com/">abcdefgh</a></li>
                        </ul>
                        </div> 
                    : <div>helloworld</div>
        )
                                


 }



				</div>
                </div>
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
