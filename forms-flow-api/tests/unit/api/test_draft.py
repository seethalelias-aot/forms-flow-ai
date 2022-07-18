"""Test suite for draft API endpoint."""

from tests.utilities.base_test import (
    get_draft_create_payload,
    get_token,
)

def test_draft_create_method(app, client, session, jwt):
    """Tests the draft create method with valid payload."""
    token = get_token(jwt)
    headers = {
        "Authorization": f"Bearer {token}",
        "content-type": "application/json",
    }
    rv = client.post("/draft", headers=headers, json=get_draft_create_payload())
    assert rv.status_code == 201


    # def test_draft_update_details_api(app, client, session, jwt):
    #     """Tests the draft update endpoint with valid payload."""
    #     token = get_token(jwt)
    #     headers = {
    #         "Authorization": f"Bearer {token}",
    #         "content-type": "application/json",
    #     }

    #     rv = client.post(
    #         "/draft",
    #         headers=headers,
    #         json=get_draft_create_payload(),
    #     )
    #     assert rv.status_code == 201
    #     draft_id = rv.json.get("id")
    #     assert rv != {}

    #     rv = client.get(f"/draft/{draft_id}", headers=headers)
    #     payload = rv.json
    #     payload["data"] = "New"

    #     rv = client.put(f"/draft/{draft_id}", headers=headers, json=payload)
    #     assert rv.status_code == 200
    #     assert rv.json == "Updated successfully"


