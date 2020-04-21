
import http.client
import json
from urllib.parse import urlparse
from slack_webhook import Slack
from email_client import email_client
from datetime import datetime





def daily_logic():
    day_logic = int(datetime.now().strftime("%d")) - 1
    day_logic = str(day_logic)
    yesterday = datetime.now().strftime("%Y-%m-{}") .format(day_logic)
    today = datetime.now().strftime("%Y-%m-%d")
    return {'today': today,
            'yesterday': yesterday}



def http_client(url):
    get_url = urlparse(url)
    url = get_url.netloc
    path = get_url.path
    query = get_url.query
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



def lambda_handler(event, context):
    daily = daily_logic()
    today = daily['today']
    yesterday = daily['yesterday']
    sender = "tonnyed87@gmail.com"
    to_add = "tonnyed@hotmail.com"





    gogo = http_client("https://jsonplaceholder.typicode.com/todos/1")

    print(gogo["title"])
    stats = gogo["title"]

    value_one = " Hello Tony Team, \n \n Daily Stats: \n \n From: {today} Time: 17:01 \n To: {yesterday} Time: 17:00 \n \n Value: {stats} \n \n King Regards \n \n Tony Bots :)" .format(today = today, yesterday = yesterday, stats = stats)


    message = str(value_one)
    email_client(sender, to_add,message)

    slack = Slack(url={slack_api})
    slack.post(text = value_one )

    return "Completed"