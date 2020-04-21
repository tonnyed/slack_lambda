from datetime import datetime


def daily_logic():
    day_logic = int(datetime.now().strftime("%d")) - 1
    day_logic = str(day_logic)
    yesterday = datetime.now().strftime("%Y-%m-{}") .format(day_logic)
    today = datetime.now().strftime("%Y-%m-%d")
    return {'today': today,
            'yesterday': yesterday}

daily = daily_logic()
today = daily['today']
yesterday = daily['yesterday']
