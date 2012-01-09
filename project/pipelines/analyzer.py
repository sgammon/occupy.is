# -*- coding: utf-8 -*-

############################################################
## Analyzer pipelines - for analyzin' yur data			  ##
############################################################
##                                                        ##
## Authors:                                               ##
##		- Alex Rosner (alex@momentum.io)                  ##
##		- Tyler Porras (tyler@momentum.io)                ##
##                                                        ##
## History:                                               ##
## 	 - Tyler Porras Sat. Dec. 31. 2011 4:10pm             ##
##		- built ContentAction child pipeline shells       ##
##   - Tyler Porras Mon. Jan. 2. 2012 5:36 pm             ##
##      - Commit changes                                  ## 
##   -Tyler Porras/ Sam Gammon Sun. Jan. 8 2012           ##
##      - built VoteCounter                               ##
##   -Tyler Porras Mon. Jan. 9. 2012 10:26 am             ##
##      - built Topic/Comment/Star counters               ##
##                                                        ##
##   -Tyler Porras Mon. Jan. 9. 2012 1:26 pm              ##
##      - edited pipelines                                ##              
############################################################
from project.pipelines import OccupyPipeline
from project.models import ndb
from project.models.topic import Upvote, Downvote
from project.models.social import Comment, Star
from google.appengine.ext import ndb as nndb
from google.appengine.ext.ndb import tasklets, context, query
from google.appengine.datastore.datastore_query import Cursor
import random




class AnalyzerPipeline(OccupyPipeline):
	
	''' Base for analyzer pipelines. '''
	

	def getCountForParent(self, query, stack=0):
    	count = query.count(500)
    	if count < 500:
    		return stack+count
    	else:
    		return self.getCountForParent(query.with_cursor(query.cursor_after()), stack=stack+500)
    		
    query_options = query.QueryOptions(keys_only=True, limit=500, produce_cursors=True, batch_size=200)

	
	def run(self):
		pass



#### +=+=+=+ Analyzer Pipelines +=+=+=+ ####
class SocialActionPipeline(AnalyzerPipeline):
	
	''' Pipeline for social action (upvote, downvote, star, etc.) '''
	
	def run(self):
		pass



class ContentActionPipeline(AnalyzerPipeline):
	
	''' Pipeline for created content like comments, messages, pictures, etc. '''

	def run(self):
		pass



#### +=+=+=+  Counter Pipelines  +=+=+=+ ####
class TopicCounter(ContentActionPipeline):

	''' Pipeline used for counting topics '''

	def run(self, parent_key=parent_key):
		
		try:
			parent_k = nndb.key.Key(urlsafe=str(parent_key)) # parent should be a Movement, Profile Page, etc
            parent = parent_k.get()
        except Exception, e:
        	self.log.error('Invalid parent key: '+str(e))
        	raise
        	return False
        
        topic_queries = []
        topics = [Topic]

        for topic in topics:
        	topic_queries.append((topic, topic.query(ancestor=parent, options=query_options)))
        
        results = {}
        for topic, query in query_options:
            results[topic] = self.getCountForParent(query)
        
        return dict([k.kind(, v for k, v in results.items())])




class CommentCounter(ContentActionPipeline):

	''' Pipeline used for counting posted comments per topic. '''

	def run(self,parent_key=parent_key):

		try: 
		    parent_k = nndb.key.Key(urlsafe=str(parent_key)) # should be a topic
		    parent = parent_k.get()
		
	    except Exception, e:
			self.log.error('Invalid parent key: '+str(e))
			raise
			return False
		
		comment_queries = []
		comments = [Comment]

        for comment in comments:
        	comment_queries.append((comment, comment.query(ancestor=parent, options=query_options)))

        results = {}
        for comment, query in query_options:
        	results[comment] = self.getCountForParent(query)

        return dict([k.kind(), v for k, v in results.items()])




class StarCounter(SocialActionPipeline):

    ''' Pipeline used for counting stars on comments and topics. '''
    		
    def run(self, parent_key=parent_key):
        
        try:
			parent_k = nndb.key.Key(urlsafe=str(parent_key)) # should either be a topic or a comment
			parent = parent_k.get()
		except Exception, e:
			self.log.error('Invalid parent key: '+str(e))
			raise
			return False 

		star_queries = []
		stars = [Star]

		for star in stars:
			star_queries.append((star, star.query(ancestor=parent, options=query_options)))
		
		results = {}
		for star, query in query_options:
			results[star] = self.getCountForParent(query)
		
		return dict([k.kind(), v for k, v in results.items()])



    	
class VoteCounter(SocialActionPipeline):

    ''' Pipeline for up/down votes on topics AND comments, per topic and comment. '''


	def run(self, parent_key=parent_key):

		try:
			parent_k = nndb.key.Key(urlsafe=str(parent_key)) # should either be a topic or a comment
			parent = parent_k.get()
		except Exception, e:
			self.log.error('Invalid parent key: '+str(e))
			raise
			return False
		
		vote_queries = []
		vote_types = [Upvote, Downvote]
		
		for vote_type in vote_types:
			vote_queries.append((vote_type, vote_type.query(ancestor=parent, options=query_options)))

		results = {}
		for vote_type, query in vote_queries:
			results[vote_type] = self.getCountForParent(query)

		return dict([k.kind(), v for k, v in results.items()])