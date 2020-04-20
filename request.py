

import http.client
import json
from urllib.parse import urlparse
from slack_webhook import Slack


def http_client(url):
    get_url = urlparse(url)
    url = get_url.netloc
    path = get_url.path
    query = get_url.query
#     print(url)
#     print(path)
    conn = http.client.HTTPSConnection(url)
    conn.request("GET", path)
    response = conn.getresponse()
    print(response.status, response.reason)
    if response.status == "200" or 200:
       data = response.read()
       if isinstance(data, (bytes, bytearray)):
          data = data.decode()
          data_json = json.loads(data)
    else:
       print ("connection error"+" "+response.status+" "+response.reason)

    return data_json


gogo = http_client("https://jsonplaceholder.typicode.com/todos/1")

print(gogo["title"])


slack = Slack(url="https://hooks.slack.com/services/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")
slack.post(text=gogo["title"]+" "+str(gogo["id"])+" "+ "this is great!")