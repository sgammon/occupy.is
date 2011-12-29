# -*- coding: utf-8 -*-

###### ====== Shortcuts ====== ######
from apptools.model import db, ndb
from apptools.model import NDBModel
from apptools.model import NDBExpando

###### ====== Model Mixins ====== ######
from project.core.data import mixins
from project.core.data.mixins import IndexerMixin, AnalysisMixin
from project.core.data.mixins import UserAuditMixin, CreatedModifiedMixin
from project.core.data.mixins import MessageConverterMixin, SimpleStructConverterMixin


class OccupyModel(NDBModel, CreatedModifiedMixin, MessageConverterMixin):

	''' Top-level model class for all Occupy schema classes. '''

	pass


class OccupyExpando(NDBExpando, CreatedModifiedMixin):

	''' Top-level model class for all Occupy schema-less classes. '''

	pass