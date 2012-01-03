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
############################################################
from project.pipelines import OccupyPipeline
from google.appengine.ext import db
import random



class AnalyzerPipeline(OccupyPipeline):
	
	''' Empty shell for analyzer pipeline. '''
	
	def run(self):
		pass



#### +=+=+=+ Analyzer Pipelines +=+=+=+ ####
class SocialActionPipeline(AnalyzerPipeline):
	
	''' Pipeline for social action (upvote, downvote, like, etc.). '''
	
	def run(self):
		pass



class ContentActionPipeline(AnalyzerPipeline):
	
	''' Pipeline for created content like comments, messages, pictures etc. '''
	
	def run(self):
		pass



#### +=+=+=+  Counter Pipelines  +=+=+=+ ####
class TopicCounter(ContentActionPipeline):

	''' Pipeline used for counting topics '''

	def run(self):
		pass



class CommentCounter(ContentActionPipeline):

	''' Pipeline used for counting posted comments per topic. '''

	def run(self):
		pass



class StarCounter(ContentActionPipeline):

    ''' Pipeline used for counting stars on comments and topics. '''

    def run(self):
    	pass



class VoteCounter(ContentActionPipeline):

    ''' Pipeline for up/down votes on topics AND comments, per topic and comment. '''

	def run(self, *args):
		
		







