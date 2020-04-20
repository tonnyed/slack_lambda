
import http.client
import json
from urllib.parse import urlparse
from slack_webhook import Slack
from email_client import email_client
#
# def http_client(url):
#     get_url = urlparse(url)
#     url = get_url.netloc
#     path = get_url.path
#     query = get_url.query
#     conn = http.client.HTTPSConnection(url)
#     conn.request("GET", path)
#     response = conn.getresponse()
#     print(response.status, response.reason)
#     if response.status == "200" or 200:
#        data = response.read()
#        if isinstance(data, (bytes, bytearray)):
#           data = data.decode()
#           data_json = json.loads(data)
#     else:
#        print ("connection error"+" "+response.status+" "+response.reason)
#
#     return data_json



charset = "UTF-8"
sender = "tonnyed87@gmail.com"
to_add = "tonnyed@hotmail.com"
body = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>
            """

email_client(sender, to_add, body, message, charset)
def lambda_handler(event, context):
    gogo = http_client("https://jsonplaceholder.typicode.com/todos/1")

    print(gogo["title"])

    message = ("Daily Stats\r\n"
                 "Today Value is:"+""+gogo["title"]
                 "Today Id is:"+""+gogo["id"]
                )
    email_client(sender, to_add, body, message, charset)

    slack = Slack(url="https://hooks.slack.com/services/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")
    slack.post(text=gogo["title"]+" "+str(gogo["id"])+" "+ "this is great!")

    return "Completed"