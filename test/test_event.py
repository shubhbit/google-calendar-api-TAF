import pytest
from common.helper import generate_event_body_mandatory_only, Status, compare_response_json

import logger

log = logger.Logger(__name__).logger


class TestEvent:

    def test_create_event_valid_mandatory_fields(self):
        # try:
        log.info("TEST- create event with valid mandatory fields only starts")
        mandatory_fields_only = generate_event_body_mandatory_only(3, 4)
        log.info(
            "executing POST operation against events endpoint with body: {}".format(mandatory_fields_only))
        response = pytest.event.create_event(mandatory_fields_only)
        log.info("verifying response code")
        assert response.status_code == Status.OK, log.error("expected code: {0}, received: {1}".format(
            Status.OK, response.status_code))
        log.info("received correct response code: {}".format(
            response.status_code))
        assert compare_response_json(mandatory_fields_only, response.json(
        )), log.error("expected response: {0}, received: {1}".format(mandatory_fields_only, response.json()))
        log.info("received correct response json: {}".format(response.json()))
        # except AssertionError as e:
        #     log.error(e)
