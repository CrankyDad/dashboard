# 
# Class for fetching all data for self and can then return a subset
# based of paths. This mimics a the delta messages sent
#
import requests
import logging
import datetime as dt
from config import signalk_host, signalk_port

logger = logging.getLogger(__name__)

class SignalkOTF:
	
	def __init__(self): 
		self.url = 'http://{}:{}/signalk/v1/api/vessels/self'.format(signalk_host, signalk_port)
		self.data = None 
	
	def refresh(self): 
	   # """Hämtar en ny snapshot från Signal K.""" 
		logger.debug("signalk_otf.refresh: OTF to the data")
		response = requests.get(self.url, timeout=5) 
		response.raise_for_status() 
		data = response.json()
		logger.debug("signalk_otf.refresh:OTF got the data: %s", data)
	
	def get(self, path, default=None): 
	#        """Returnerar hela objektet för en Signal K-path.""" 
		obj = self.data 
	
		for key in path.split("."): 
			if not isinstance(obj, dict): 
				return default 
			obj = obj.get(key) 
			if obj is None: 
				return default 
		return obj 
	
	def value(self, path, default=None): 
	#        """Returnerar endast value.""" 
		item = self.get(path) 
		if isinstance(item, dict): 
			return item.get("value", default) 
		return default 
		
	def update_values(self, values, paths):
		self.refresh
		
		for path in paths:
			logger.debug("signalk_otf.update_values:OTF got timestamp: %s", self.timestamp(path)	)
			values[path] = 	{
				'value' : self.value(path),
				'time': dt.datetime.fromisoformat(self.timestamp(path).replace("Z","+00:00")),
				'rendered': False
			}
			logger.debug("signalk_otf.update_values:OTF updated the data: %s", values[path])
	
	def timestamp(self, path):
		item = self.get(path) 
		if isinstance(item, dict): 
			return item.get("timestamp") 
		return None 
	
	def source(self, path): 
		item = self.get(path) 
		if isinstance(item, dict): 
			return item.get("$source") 
		return None 
	
	def values(self, paths): 
	#       """Returnerar en dictionary med value för flera paths.""" 
		result = {} 
	
		for path in paths: 
			result[path] = self.value(path) 
		return result 
	
