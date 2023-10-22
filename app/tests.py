from django.test import TestCase

from models import City, Continent, Country, MainObject, State
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


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


class ContinentModelTest(TestCase):
    def test_continent_creation(self):
        continent = Continent.objects.create(name="Test Continent")
        self.assertEqual(continent.name, "Test Continent")


class CountryModelTest(TestCase):
    def test_country_creation(self):
        continent = Continent.objects.create(name="Test Continent")
        country = Country.objects.create(
            name="Test Country", continent=continent)
        self.assertEqual(country.name, "Test Country")
        self.assertEqual(country.continent, continent)


class StateModelTest(TestCase):
    def test_state_creation(self):
        continent = Continent.objects.create(name="Test Continent")
        country = Country.objects.create(
            name="Test Country", continent=continent)
        state = State.objects.create(name="Test State", country=country)
        self.assertEqual(state.name, "Test State")
        self.assertEqual(state.country, country)


class CityModelTest(TestCase):
    def test_city_creation(self):
        continent = Continent.objects.create(name="Test Continent")
        country = Country.objects.create(
            name="Test Country", continent=continent)
        state = State.objects.create(name="Test State", country=country)
        city = City.objects.create(name="Test City", state=state)
        self.assertEqual(city.name, "Test City")
        self.assertEqual(city.state, state)


class YourAppViewsTest(TestCase):
    def setUp(self):
        # create sample MainObject instances for testing
        self.client = APIClient()
        self.main_object = MainObject.objects.create(
            name="Test Object", postcode="12345")

    def test_ping_view(self):
        response = self.client.get(reverse('ping'))
        self.assertEqual(response.status_code, 200)
        # check if 'Pong' is in the response content.
        self.assertContains(response, 'Pong')

    def test_main_object_search_view(self):
        response = self.client.get(reverse('main-object-search'))
        self.assertEqual(response.status_code, 200)

    def test_main_object_list_view(self):
        response = self.client.get(reverse('main-object-list'))
        self.assertEqual(response.status_code, 200)

    def test_main_object_detail_view(self):
        response = self.client.get(
            reverse('main-object-detail', args=[self.main_object.pk]))
        self.assertEqual(response.status_code, 200)
