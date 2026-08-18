import urllib.request
import json
import websocket
import threading
import logging
from config import signalk_host, signalk_port, dashboard

logger = logging.getLogger(__name__)
ws=None
wst=None

def get_state():
	url = 'http://{}:{}/signalk/v1/api/vessels/self/navigation/state/value'.format(signalk_host, signalk_port)
	req = urllib.request.Request(url)
	try:
		logger.info("Connecting to:" + url)
		r = urllib.request.urlopen(req).read()
		cont = json.loads(r.decode('utf-8'))
		logger.debug("Initial state {}".format(cont))
		return cont
	except:
		return None

def clean_up (ws, wst):
	#Check if there alreay is a running connection and thread
	if ws is not None:
		logger.debug("Cleanup found open websocket")
		ws.close()
		wst.end()

def connect(on_message, on_error, on_open, on_close):
	url = 'ws://{}:{}/signalk/v1/stream?subscribe=none'.format(signalk_host, signalk_port)
		
	ws = websocket.WebSocketApp(url,
		on_message = on_message,
		on_error = on_error,
		on_open = on_open,
		on_close = on_close)
	wst = threading.Thread(target=ws.run_forever)
	wst.start()

def subscribe(ws, pathlist):
	# First unsubscribe from previous
	ws.send(json.dumps({
		'context': '*',
		'unsubscribe': [
			{
				'path': '*'
			}
		]
	}))
 #   logger.debug('Subscribe: To start subscribe')
 
 # Then subscribe to feed
 # The data is to be sent every 85s second (twice per shortest refresh)
	subscribes = []
	for path in pathlist:
		subscribes.append({
			'path': str(path),
			'period': 85000,
			'format': 'delta',
			'policy': 'fixed'
		})
	
# Data thayt are to sent at higher interval (screen changes,alarms etc)
	sf_paths=[]
	sf_paths.append('navigation.state')
		
 # If alarmscreen add notifications, see draw line
	if dashboard['layout']['alarm_screen']:
		sf_paths.append('notifications.*')
	
	for path in sf_paths:
		subscribes.append({
			'path': str(path),
			'period': 3000,
			'format': 'delta',
			'policy': 'fixed'
		})

	logger.debug("Paths subscribed to: %s", subscribes)
	ws.send(json.dumps({
		 'context': 'vessels.self',
		 'subscribe': subscribes
	}))
