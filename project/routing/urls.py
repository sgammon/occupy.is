# -*- coding: utf-8 -*-
"""URL definitions."""
from webapp2 import Route

from webapp2_extras.routes import DomainRoute
from webapp2_extras.routes import NamePrefixRoute
from webapp2_extras.routes import PathPrefixRoute
from webapp2_extras.routes import HandlerPrefixRoute

rules = [

	HandlerPrefixRoute('project.handlers.', [	

		
		## == Scope: Global == ##
		DomainRoute('occupy.*', [

			
			## === Main URLs === ##
			HandlerPrefixRoute('main.', [
				NamePrefixRoute('main-', [

					Route('/', name='landing', handler='landing.Landing'),
					Route('/offline', name='offline', handler='util.Offline')

				])
			]),

			
			## === Security URLs === ##
			HandlerPrefixRoute('security.', [
				NamePrefixRoute('security-', [

					Route('/login', name='auth/login', handler='Login'),
					Route('/logout', name='auth/logout', handler='Logout'),
					Route('/register', name='auth/register', handler='Register'),

				])
			]),


			## === Occupier URLs === ##
			HandlerPrefixRoute('occupiers.', [
				NamePrefixRoute('occupiers-', [

					Route('/people', name='landing', handler='Occupiers'),
					PathPrefixRoute('/people', [
							
						Route('/world', name='world', handler='Occupiers'),
						Route('/<username>', name='profile', handler='Occupier'),

					])

				])
			]),

		
		]),
		

		## == Scope: Movement == ##
		DomainRoute('<movement>.occupy.*', [


			## == Movement URLs == ##
			HandlerPrefixRoute('movements.', [
				NamePrefixRoute('movement-', [

					Route('/', name='landing', handler='Movement'),
					Route('/trends', name='trends', handler='Trends'),
					Route('/occupiers', name='members', handler='Members')

				])
			]),

		]),


		## == All Scopes: Topic URLs == ##
		HandlerPrefixRoute('topics.', [
			NamePrefixRoute('topic-', [

				Route('/<topic>', name='view', handler='Topic'),
				Route('/<topic>/trends', name='trends', handler='Trends')

			])
		])
	
	])
]