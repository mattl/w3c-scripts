import requests
import json

url = 'https://api.github.com/graphql'
query = { "query" : '{ repository(owner:"w3c", name:"wptdashboard") { issues(last:100,states:CLOSED,labels:"priority:urgent") {  edges { node { number title createdAt updatedAt }}}}}' }
api_token = ""
headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=query, headers=headers)

parsed = json.loads(r.text)
print json.dumps(parsed, indent=4, sort_keys=True)
