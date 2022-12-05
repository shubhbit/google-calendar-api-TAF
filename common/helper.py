from datetime import datetime, timedelta


def get_start_end_dateTime(start_hour, end_hour):
    date = datetime.now().date()
    today = datetime(date.year, date.month, date.day,
                     start_hour) + timedelta(days=0)
    start = today.isoformat()
    end = (today + timedelta(hours=end_hour-start_hour)).isoformat()
    return start, end


def generate_event_body(start_hour, end_hour, optional=False):
    event_timings = get_start_end_dateTime(start_hour, end_hour)
    data = {"start": {"dateTime": event_timings[0]+"+05:30", "timeZone": Timezone.IST},
            "end": {"dateTime": event_timings[1]+"+05:30", "timeZone": Timezone.IST}, }
    if optional:
        data["summary"] = "Sample Event"
        data["description"] = "This is a sample test event"
    return data


def compare_response_json(input_json, response_json):
    matched = True
    for key in input_json:
        if input_json.get(key) != response_json.get(key):
            matched = False
            break
    return matched


def assert_status_code(expected, received, logger):
    assert received.status_code == expected, logger.error("expected code: {0}, received code: {1}, error: {2}".format(
        expected, received.status_code, received.text))


def assert_response_json(expected, received, logger):
    assert compare_response_json(expected, received), logger.error(
        "expected response: {0}, received: {1}".format(expected, received))


class Timezone:
    IST = 'Asia/Kolkata'


class Status:
    OK = 200
    OK_DELETE = 204
    INVALID_FIELD = 400
    AUTH_FAILED = 401
    NOT_FOUND = 404
