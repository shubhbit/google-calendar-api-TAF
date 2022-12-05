from datetime import datetime, timedelta


def get_start_end_dateTime(start_hour, end_hour):
    date = datetime.now().date()
    today = datetime(date.year, date.month, date.day,
                     start_hour) + timedelta(days=0)
    start = today.isoformat()
    end = (today + timedelta(hours=end_hour-start_hour)).isoformat()
    return start, end


def generate_event_body_mandatory_only(start_hour, end_hour):
    event_timings = get_start_end_dateTime(start_hour, end_hour)
    data = {"start": {"dateTime": event_timings[0]+"+05:30", "timeZone": Timezone.IST},
            "end": {"dateTime": event_timings[1]+"+05:30", "timeZone": Timezone.IST}, }
    return data


def compare_response_json(input_json, response_json):
    matched = True
    for key in input_json:
        if input_json.get(key) != response_json.get(key):
            matched = False
            break
    return matched



class Timezone:
    IST = 'Asia/Kolkata'


class Status:
    OK = 200
    OK_DELETE = 204
