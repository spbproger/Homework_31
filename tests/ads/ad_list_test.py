import pytest

from tests.factories import AdFactory
from ads.serializer import AdListSerializer


@pytest.mark.django_db
def test_ad_list(client):
    ads = AdFactory.create_batch(5)

    expected_response = {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ads, many=True).data
    }

    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == expected_response