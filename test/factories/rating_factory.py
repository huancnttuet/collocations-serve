import factory

from app import models


class RatingFactory(factory.Factory):
    class Meta:
        model = models.Rating

    product_id = factory.Faker('random_int', min=1, max=3)
    user_id = factory.Faker('random_int', min=1, max=3)
    client_id = factory.Faker('random_int', min=1, max=3)
    rating = factory.Faker('random_int', min=1, max=3)
