import json

import pytest


@pytest.mark.django_db
def test_create_ad(client, user):

    data = {
        "name": 'testtesttest',
        "category": 1,
        "is_published": False,
        "price": 100,
        "author": user.id

    }

    response = client.post(
        '/ad/create/',
        data=json.dumps(data),
        content_type='application/json'
    )

    expected_response = response.json()

    assert response.status_code == 201
    assert response.data == expected_response