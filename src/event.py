import requests
import pytest


class Event(object):
    def __init__(self, token):
        self.event_url = (pytest.config['EVENT_URL']).replace("\n", "")
        self._access_token = token

    @property
    def header(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(self._access_token)}

    def get_event(self, event_id):
        get_event_url = "{0}/{1}".format(self.event_url, event_id)
        get_response = requests.get(get_event_url, headers=self.header)
        return get_response

    def list_all_events(self):
        list_event_res = requests.get(self.event_url, headers=self.header)
        return list_event_res

    def create_event(self, data):
        create_event_response = requests.post(
            self.event_url, json=data, headers=self.header)
        return create_event_response

    def update_event(self, event_id, data):
        update_event_url = "{0}/{1}".format(self.event_url, event_id)
        update_event_response = requests.patch(
            update_event_url, json=data, headers=self.header)
        return update_event_response

    def delete_event(self, event_id):
        delete_event_url = "{0}/{1}".format(self.event_url, event_id)
        delete_response = requests.delete(
            delete_event_url, headers=self.header)
        return delete_response
