import requests, pprint
r = requests.get('https://XYXYXYXYX.execute-api.us-east-1.amazonaws.com/dev/hello-world')
pprint.pprint(r.json())
