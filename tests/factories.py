import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    username = factory.Faker('name')
    first_name = 'test1'
    last_name = 'test2'
    password = 'password'
    role = 'admin'
    email = factory.Faker('email')
    birth_date = factory.Faker('date_object')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'ads.Ad'

    name = 'Ad'
    price = 100
    author = factory.SubFactory(UserFactory)