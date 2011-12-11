# -*- coding: utf-8 -*-

###### ====== Shortcuts ====== ######
from apptools.model import db, ndb
from apptools.model import Polymodel
from apptools.model import Model, NDBModel
from apptools.model import Expando, NDBExpando


class OccupyModel(NDBModel):

	''' Top-level model class for all Occupy schema classes. '''

	pass


class OccupyExpando(NDBExpando):

	''' Top-level model class for all Occupy schema-less classes. '''

	pass