"""Test suite for draft API endpoint."""

from tests.utilities.base_test import get_draft_create_payload, get_token, get_application_create_payload, get_form_request_payload


def test_draft_create_method(app, client, session, jwt):
    """Tests the draft create method with valid payload."""
    token = get_token(jwt)
    headers = {"Authorization": f"Bearer {token}", "content-type": "application/json"}
    rv = client.post("/form", headers=headers, json=get_form_request_payload())
    assert rv.status_code == 201

    form_id = rv.json.get("formId")

    rv = client.post(
        "/application/create",
        headers=headers,
        json=get_application_create_payload(form_id),
    )
    assert rv.status_code == 201
    response = client.post("/draft", headers=headers, json=get_draft_create_payload(form_id))
    print(response.json)
    assert response.status_code == 201
    assert response.json.get("id") is not None
