from datetime import datetime, timedelta

def get_reset():
    utc_now = datetime.utcnow()
    utc_reset = utc_now.replace(hour=0, minute=0, second=0, microsecond=0)
    td = timedelta(seconds=(utc_reset-utc_now).seconds)
    td_str = str(td).split(':')
    return '```%s hours, %s minutes, %s seconds until reset```' %  (td_str[0], td_str[1], td_str[2])