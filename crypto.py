from websocket import create_connection
import simplejson as json
ws = create_connection("wss://api.tiingo.com/crypto")

subscribe = {
        'eventName':'subscribe',
        'authorization':'4cfa58d4f6f34accc555e25d9bff0f16cfc99930',
        'eventData': {
            'thresholdLevel': 5
    }
}

ws.send(json.dumps(subscribe))
while True:
    print(ws.recv())