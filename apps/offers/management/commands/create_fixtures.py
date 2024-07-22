from django.core.management.base import BaseCommand, CommandError

from apps.locations.models import Location
from apps.offers.models import Option, Category, Offer, Calendar
from apps.offers.models.fixtures import options_data, categories_data, locations_data
from contrib.utils.gis import list_to_coords


class Command(BaseCommand):
    def add_arguments(self, parser):
        ...

    def create_locations(self):
        _categories = {x.name: x for x in Category.objects.all()}
        for location in locations_data:
            offers = location.pop("offers", [])
            location["coords"] = list_to_coords(location["coords"])
            location_obj, _ = self.update_or_create_object(Location, location)
            for offer in offers:
                categories = [category for x in offer.pop("categories", []) if (
                    category := _categories.get(x))]
                calendar = offer.pop("calendar", [])
                offer["location"] = location_obj
                offer_obj, _ = self.update_or_create_object(Offer, offer, keys=[
                    "location", "name", "description"])
                offer_obj.calendar.set([Calendar(**item) for item in calendar], bulk=False)
                offer_obj.categories.set(categories)

    def update_or_create_object(self, Model, item, keys=["name"]):
        values = [value for key in keys if (value := item.pop(key, None))]
        return Model.objects.update_or_create(**{
            **dict(zip(keys, values)), "defaults": item})


    def create_objects(self, Model, data, keys=["name"]):
        count = 0
        for item in data:
            instance, created = self.update_or_create_object(Model, item, keys)
            if created:
                count += 1
        return count

    def handle(self, *args, **kwargs):
        n = self.create_objects(Category, categories_data)
        print(f"Created {n} categories.")
        n = self.create_objects(Option, options_data)
        print(f"Created {n} options.")
        print("Done")
        self.create_locations()