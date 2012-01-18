# -*- coding: utf-8 -*-

############################################################
## Analyzer pipelines - for analyzin' yur data            ##
############################################################
##                                                        ##
## Authors:                                               ##
##      - Alex Rosner (alex@momentum.io)                  ##
##      - Tyler Porras (tyler@momentum.io)                ##
##                                                        ##
## History:                                               ##
##   - Sam Gammon Tue. Jan. 17. 2012 11:46am              ##
##      - sat down with tyler and cleaned up summarizer/  ##
##        analyzer pipelines for first push to GAE        ##
##   - Tyler Porras Sat. Dec. 31. 2011 4:10pm             ##
##      - built ContentAction child pipeline shells       ##
##   - Tyler Porras Mon. Jan. 2. 2012 5:36 pm             ##
##      - Commit changes                                  ## 
##   -Tyler Porras/ Sam Gammon Sun. Jan. 8 2012           ##
##      - built VoteCounter                               ##
##   -Tyler Porras Mon. Jan. 9. 2012 10:26 am             ##
##      - built Topic/Comment/Star counters               ##
##   -Tyler Porras Sat. Jan. 14. 2012. 1:13 am            ##   
##      - trimmed up code, added comments.                ##
##                                                        ##
##                                                        ##
############################################################
from project.pipelines import OccupyPipeline
from project.models import ndb
from project.models.topic import Upvote, Downvote, Topic
from project.models.social import Comment, Star
from google.appengine.ext import ndb as nndb
from google.appengine.ext.ndb import tasklets, context, query, key
from google.appengine.datastore.datastore_query import Cursor
import random


class AnalyzerPipeline(OccupyPipeline):
    
    ''' Base for analyzer pipelines. '''


    def getCountForParent(self, query, stack=0):

        ''' function for counting queries for stats. '''
        
        count = query.count(500)
        
        if count < 500:
            return stack+count
        
        else:
            return self.getCountForParent(query.with_cursor(query.cursor_after()), stack=stack+500)


    def getKey(self, urlsafe):

        ''' converts a urlsafe'd key back into a key.Key '''

        return key.Key(urlsafe=urlsafe)
    
    query_options = query.QueryOptions(keys_only=True, limit=500, produce_cursors=True, batch_size=200)



#### +=+=+=+ Analyzer Pipelines +=+=+=+ ####
class SocialActionPipeline(AnalyzerPipeline):
    
    ''' Pipeline for social action (upvote, downvote, star, etc.) '''
    pass



class ContentActionPipeline(AnalyzerPipeline):
    
    ''' Pipeline for created content like comments, messages, pictures, etc. '''
    pass



#### +=+=+=+  Counter Pipelines  +=+=+=+ ####
class TopicCounter(ContentActionPipeline):

    ''' Pipeline used for counting topics via keys. '''
     
    def run(self, parent_key):        
        # returns a key
        return {'Topic': self.getCountForParent(topic.query(ancestor=self.getKey(parent_key), options=self.query_options))}




class CommentCounter(ContentActionPipeline):

    ''' Pipeline used for counting posted comments per topic. '''
     
    def run(self, parent_key):
        return {'Comment': self.getCountForParent(comment.query(ancestor=self.getKey(parent_key), options=self.query_options))}



class StarCounter(SocialActionPipeline):

    ''' Pipeline used for counting stars on comments and topics. '''
            
    def run(self, parent_key):
        return {'Star': self.getCountForParent(star.query(ancestor=self.getKey(parent_key), options=self.query_options))}



        
class VoteCounter(SocialActionPipeline):

    ''' Pipeline for up/down votes on topics AND comments, per topic and comment. '''


    def run(self, parent_key):
   
        ''' count & return upvotes and downvotes. '''  ## ToDo: include a sum of these in a future pipeline.
        vote_queries = []
        vote_types = [Upvote, Downvote]
        
        for vote_type in vote_types:
            vote_queries.append(vote_type, vote_type.query(ancestor=self.getKey(parent_key), options=self.query_options))
        
        results = {}
        for vote_type, query in vote_queries:
            results[vote_type] = self.getCountForParent(query)
        
        final_results = []
        for vote_type, vote_key in results.items():
            final_results.append((vote_type.kind(), v))
        
        return {'Vote': dict(final_result)}


