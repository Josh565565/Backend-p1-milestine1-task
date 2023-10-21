from django.test import TestCase

from models import Continent, Country, State, City, MainObject


class MainObjectModelTest(TestCase):
    def setUp(self):
        # create a sample hierarchy of Location objects
        continent = Continent.objects.create(name="Test Continent")
        country = Country.objects.create(
            name="Test Country", continent=continent)
        state = State.objects.create(name="Test State", country=country)
        city = City.objects.create(name="Test City", state=state)

        # create a MainObject instance for testing
        self.main_object = MainObject.objects.create(
            name="Test Object",
            postcode="12345",
            city=city
        )

    def test_main_object_creation(self):
        main_object = MainObject.objects.get(name="Test Object")
        self.assertEqual(main_object.name, "Test Object")
        self.assertEqual(main_object.postcode, "12345")
        self.assertEqual(main_object.city.name, "Test City")
        self.assertEqual(main_object.city.state.name, "Test State")
        self.assertEqual(main_object.city.state.country.name, "Test Country")
        self.assertEqual(
            main_object.city.state.country.continent.name, "Test Continent")

    def test_main_object_str_method(self):
        main_object = MainObject.objects.get(name="Test Object")
        expected_str = "Test Object - 12345"
        self.assertEqual(str(main_object), expected_str)
