import jsonpickle
import json

tweets = list(open('/home/vedang/Desktop/LSDP/Project/tweets1.json','rt'))

for t in tweets:
	t = json.loads(t)
	try:
		if len(t['entities']['hashtags']) != 0:
			for h in t['entities']['hashtags']:
				print(h['text'].encode('utf8'))
	except KeyError:
		pass
