from collections import Counter
import math 
from pymongo import MongoClient
from app.service import StoryService



class Grouping:
    __story_service = StoryService()

    def get_cosine_similarity(self,vector1, vector2):
        '''
        calculate cosine distance between two lists of string
        '''
        vec1 = Counter(vector1)
        vec2 = Counter(vector2)
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator
        
    def get_smlr_category_score(self, categories_first = [], categories_second = [] ):
        '''
        Checks for similar category in both lists and 
        returns score accordingly  '''
         
        similar_category_score = 0.0
        if any(map(lambda v: v in categories_first, categories_second)):
            similar_category_score = 0.01
            return similar_category_score
        return similar_category_score
    
    def get_articles_for_grouping(self,gp_count):
        articles = self.__story_service.find_latest_stories()
        for article in articles :
            if "group" not in article:
                gp_count = gp_count +1
                self.process_grouping(article,gp_count)
                article["group"] = "group"+str(gp_count)
                stories.save(article)
            else:
                pass
        
    def process_grouping(self,p_article,gp_count):
        articles = self.__story_service.find_latest_stories()
        for article in articles:
            if article["_id"] != p_article["_id"]:
                article_cosine_smlr_score = self.get_cosine_similarity(p_article["created_keys"],article["created_keys"])
                if len(p_article) > 0 and len(article):
                    similar_category_score = self.get_smlr_category_score(p_article["category"], article["category"])
                    article_cosine_smlr_score = article_cosine_smlr_score + similar_category_score
                if article_cosine_smlr_score >= 0.4:
                    article["group"] = "group"+str(gp_count) 
                    stories.save(article)
                    
if __name__=="__main__":
    client = MongoClient()
    db = client.blackbird
    stories = db.stories
    gp_count = 0
    Grouping().get_articles_for_grouping(gp_count)