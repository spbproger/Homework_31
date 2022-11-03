import pytest


@pytest.fixture
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = "username"
    password = "password"

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role="admin",
        birth_date="2000-01-01",
        email="test@mail.ru"
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data["access"]