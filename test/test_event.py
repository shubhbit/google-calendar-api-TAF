import pytest
from common.helper import generate_event_body, Status, assert_response_json, assert_status_code

import logger

log = logger.Logger(__name__).logger


class TestEvent:

    @pytest.mark.positive
    def test_create_event_valid_mandatory_fields(self):
        """
        test which will be creating an event with only mandatory fields, will verify 
        event was created using get, and then delete it as cleanup step
        """
        log.info("TEST STARTS- create event with valid mandatory fields only starts")
        mandatory_fields_only = generate_event_body(3, 4)
        log.info(
            "executing POST operation against events endpoint with body: {}".format(mandatory_fields_only))
        response = pytest.event.create_event(mandatory_fields_only)
        log.info("verifying response code")
        assert_status_code(Status.OK, response, log)
        log.info("received correct response code: {}".format(
            response.status_code))
        assert_response_json(mandatory_fields_only, response.json(), log)
        log.info("received correct response json: {}".format(response.json()))
        log.info("getting event to make sure event was created")
        get_response = pytest.event.get_event(response.json()["id"])
        assert_status_code(Status.OK, get_response, log)
        delete_response = pytest.event.delete_event(response.json()["id"])
        log.info("deleted even as part of cleanup")
        assert_status_code(Status.OK_DELETE, delete_response, log)
        log.info("TEST ENDS- create event with valid mandatory fields only ends")

    @pytest.mark.positive
    def test_create_event_with_optional_fields(self):
        """
        test which will be creating an event with mandatory+some optional fields, will verify 
        event was created using get, and then delete it as cleanup step
        """
        log.info(
            "TEST STARTS- create event with valid mandatory+optional fields only starts")
        event_with_optional_fields = generate_event_body(5, 7, optional=True)
        log.info(
            "executing POST operation against events endpoint with body: {}".format(event_with_optional_fields))
        response = pytest.event.create_event(event_with_optional_fields)
        log.info("verifying response code")
        assert_status_code(Status.OK, response, log)
        log.info("received correct response code: {}".format(
            response.status_code))
        assert_response_json(event_with_optional_fields, response.json(), log)
        log.info("received correct response json: {}".format(response.json()))
        log.info("getting event to make sure event was created")
        get_response = pytest.event.get_event(response.json()["id"])
        assert_status_code(Status.OK, get_response, log)
        delete_response = pytest.event.delete_event(response.json()["id"])
        log.info("deleted even as part of cleanup")
        assert_status_code(Status.OK_DELETE, delete_response, log)
        log.info(
            "TEST ENDS- create event with valid mandatory+optional fields only ends")

    @pytest.mark.negative
    @pytest.mark.parametrize("key,value", [("start", "invalid-datetime"), ("end", "")])
    def test_invalid_fields_create_event(self, key, value):
        """
        test will try to verify that even can not be created with invalid fields and gets
        graceful errors
        """
        log.info(
            "TEST STARTS- try to create event with invalid fields and expect errors")
        event_with_optional_fields = generate_event_body(5, 7, optional=True)
        event_with_optional_fields[key] = value
        log.info(
            "executing POST operation against events endpoint with body: {}".format(event_with_optional_fields))
        response = pytest.event.create_event(event_with_optional_fields)
        log.info("verifying response code")
        assert_status_code(Status.INVALID_FIELD, response, log)
        log.info("received correct response code: {}".format(
            response.status_code))
        log.info(
            "TEST ENDS- try to create event with invalid fields and expect errors")

    @pytest.mark.negative
    @pytest.mark.security
    def test_create_event_with_invalid_token(self, invalidate_access_token):
        """
        test to verify that invalid access token can't be used to access APIs
        """
        log.info(
            "TEST STARTS- try to call create event API with invalid access token and expect errors")
        mandatory_fields_only = generate_event_body(3, 4)
        log.info(
            "executing POST operation against events endpoint with body: {}".format(mandatory_fields_only))
        response = pytest.event.create_event(mandatory_fields_only)
        log.info("verifying response code")
        assert_status_code(Status.AUTH_FAILED, response, log)
        log.info("received correct response code: {}".format(
            response.status_code))
        log.info(
            "TEST ENDS- try to call create event API with invalid access token and expect errors")

    @pytest.mark.positive
    def test_update_event_valid_fields(self):
        """
        test to verify that events can be modified
        """
        log.info(
            "TEST STARTS- update event with valid mandatory+optional fields only starts")
        event_with_optional_fields = generate_event_body(5, 7, optional=True)
        log.info(
            "executing PATCH operation against events endpoint with body: {}".format(event_with_optional_fields))
        response = pytest.event.create_event(event_with_optional_fields)
        log.info("verifying response code")
        assert_status_code(Status.OK, response, log)
        log.info("received correct response code: {}".format(
            response.status_code))
        event_with_optional_fields["summary"] = "Sample Event - Updated"
        event_id = response.json()["id"]
        log.info("updating summary field of event: {}".format(event_id))
        update_res = pytest.event.update_event(
            event_id, event_with_optional_fields)
        assert_status_code(Status.OK, update_res, log)
        log.info("received correct response code: {}".format(
            update_res.status_code))
        assert_response_json(event_with_optional_fields,
                             update_res.json(), log)
        log.info("received correct response json: {}".format(update_res.json()))
        log.info("getting event to make sure event was created")
        get_response = pytest.event.get_event(event_id)
        assert_status_code(Status.OK, get_response, log)
        assert_response_json(event_with_optional_fields,
                             get_response.json(), log)
        log.info("received correct response json: {}".format(get_response.json()))
        delete_response = pytest.event.delete_event(event_id)
        log.info("deleted even as part of cleanup")
        assert_status_code(Status.OK_DELETE, delete_response, log)
        log.info(
            "TEST ENDS- update event with valid mandatory+optional fields only ends")
