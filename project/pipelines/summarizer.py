import logging

from project.models import ndb

from project.pipelines import analyzer
from project.pipelines import OccupyPipeline

from google.appengine.ext import ndb as nndb
from google.appengine.ext.ndb import key as nkey, query as nquery

from project.models.topic import Topic
from project.models.social import Star
from project.models.social import Comment
from project.models.occupier import Occupier
from project.models.movement import Movement


#~ ~ ~ tier ~ 1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #

class SummarizerPipeline(OccupyPipeline): 

	''' base for summarizer pipelines. '''

	models = {
		
		'Topic': Topic,
		'Comment': Comment,
		'Movement': Movement,
		'Occupier': Occupier

	}

	def run(self, key_list):

		routines = []
		for key in key_list:
			k = nkey.Key(urlsafe=key)

			if k.kind() in self.models.keys():

				if k.kind() == 'Topic':
					pass

				elif k.kind() == 'Movement':
					pass

				elif k.kind() == 'Occupier':
					pass

				elif k.kind() == 'Comment':
					pass


			else:
				return False, 'Unsupported model kind.'



		topic_summary = yield TopicSummarizer(key)
		comment_summary = yield CommentSummarizer(key)
		occupier_summary = yield OccupierSuumarizer(key)
		movement_summary = yield MovementSummarizer(key)

		all_counts = yield PrepareReport([topic_summary])
		
		return results



class PrepareReport(OccupyPipeline):

	''' Pipeline used to prepare results for export. '''

	def run(self, operations):
        results = {}
		for blob in operations:
			if isinstance(blob, dict):
				for k, v in blob.items():
					results[k] = v
		return results

	

#~ ~ ~ tier ~ 2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #

class TopicSummarizer(SummarizerPipeline):

	''' pipeline for: summarizing comments, stars, votes under a topic  '''

	# Yields results from Counters, passes those results to PrepareReport, then returns those results to its parent.
	def run(self, *args):

		operations = yield CommentCounter(key), StarCounter(key), VoteCounter(key)
		report = yield PrepareReport(operations)
		return report


class CommentSummarizer(SummarizerPipeline):

	''' Pipeline for summarizing stars and votes under a comment. '''

	def run(self, *args):
		
		operations = yield StarCounter(key), Votecounter(key)
		report = yield PrepareReport(operations)
		return report




class OccupierSummarizer(SummarizerPipeline):

	''' Pipeline for summarizing user's topics, comments, stars, votes. '''

	def run(self, *args):
		operations = yield TopicCounter(key), CommentCounter(key), Starounter(key), VoteCounter(key)
		report = yield PrepareReport(operations)
		return report



class MovementSummarizer(SummarizerPipeline):

	''' Pipeline for summarizing topics, occupiers, stars under a movement. '''

	def run(self, *args):
		operations = yield TopicCounter(key), StarCounter(key)
		report = yield PrepareReport(operations)
		return report