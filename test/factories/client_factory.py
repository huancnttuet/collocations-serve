import factory

from app import models


class ClientFactory(factory.Factory):
    class Meta:
        model = models.Client

    name = factory.Faker('name')
    active = factory.Faker('random_int', min=0, max=1)
