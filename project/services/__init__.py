# -*- coding: utf-8 -*-

from apptools import BaseService
from apptools.core import _apibridge, _extbridge, _utilbridge

import protorpc
from protorpc import remote
from protorpc import messages
from protorpc import message_types


class RemoteService(BaseService):
	
	api = _apibridge
	ext = _extbridge
	util = _utilbridge

