"""Test suite for draft API endpoint."""

from tests.utilities.base_test import get_draft_create_payload, get_token


def test_draft_create_method(app, client, session, jwt):
    """Tests the draft create method with valid payload."""
    token = get_token(jwt)
    headers = {"Authorization": f"Bearer {token}", "content-type": "application/json"}
    response = client.post("/draft", headers=headers, json=get_draft_create_payload())
    assert response.status_code == 201
    assert response.json.get("id") is not None
