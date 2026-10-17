# 
# Class for fetching all data for self and can then return a subset
# based of paths. This mimics a the delta messages sent
#
import requests
import logging
from config import signalk_host, signalk_port

logger = logging.getLogger(__name__)

class SignalKClient: 
	def __init__(self): 
		self.url = "http://{signalk_host}:{signalk_port}/signalk/v1/api/vessels/self" 
		self.data = None 

	def refresh(self): 
	   # """Hämtar en ny snapshot från Signal K.""" 
		response = requests.get(self.url, timeout=5) 
		response.raise_for_status() 
		self.data = response.json()
		logger.debug("OTF got the data: %s", self.data)

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
			logger.debug("OTF got timestamp: %s", self.timestamp(path)	)
			values[path] = 	{
				'value' : self.value(path),
				'time': dt.datetime.fromisoformat(timestamp.replace("Z","+00:00")),
				'rendered': False
			}
			logger.debug("OTF updated the data: %s", values[path])

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
