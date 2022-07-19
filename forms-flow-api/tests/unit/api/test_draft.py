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

def test_draft_update_details_api(app, client, session, jwt):
    """Tests the draft update endpoint with valid payload."""
    token = get_token(jwt)
    headers = {
        "Authorization": f"Bearer {token}",
        "content-type": "application/json",
    }
    rv = client.post("/form", headers=headers, json=get_form_request_payload())
    assert rv.status_code == 201

    form_id = rv.json.get("formId")

    rv = client.post(
        "/application/create",
        headers=headers,
        json=get_application_create_payload(form_id),
    )
    assert rv.status_code == 201
    rv = client.post(
        "/draft",
        headers=headers,
        json=get_draft_create_payload(form_id),
    )
    assert rv.status_code == 201
    draft_id = rv.json.get("id")
    assert rv != {}

    rv = client.get(f"/draft/{draft_id}", headers=headers)
    payload = rv.json
    payload["data"] = "New"

    rv = client.put(f"/draft/{draft_id}", headers=headers, json=payload)
    assert rv.status_code == 200
    assert rv.json == "Updated successfully"
