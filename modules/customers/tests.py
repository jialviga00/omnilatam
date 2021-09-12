from custom.utils.testutiles import TestUtiles
from modules.customers.models import Customer
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase


class CustomerModelTest(TestCase):

	
	def test_create_customer(self):
		"""
			validate create customer
		"""
		TestUtiles.create_customer_test('123456789')
		self.assertIs(Customer.objects.all().count() > 0, True)


	def test_get_token_by_api(self):
		"""
			validate get token by API
		"""
		
		TestUtiles.create_user_test()
		client = APIClient()
		
		response = client.post('/signin/', {'username': 'test', 'password': 'T3ST!!!'})
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_401_UNAUTHORIZED)
		self.assertFalse(response_data.get('authenticated', None))
		
		response = client.post('/signin/', {'username': 'test', 'password': 'T3ST!'})
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertTrue(response_data.get('authenticated', None))
		self.assertContains(response, "Token")



	def test_create_customer_by_api(self):
		"""
			validate create customer by API
		"""
		
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)

		response = client.post(
			'/customers/',
			{
				'identification': '12345', 
				'name': 'TEST_CUSTOMER_NAME_API',
				'address': 'TEST_CUSTOMER_ADDRESS_API',
			}
		)
		self.assertIs(response.status_code, status.HTTP_201_CREATED)
		self.assertIs(Customer.objects.all().count() > 0, True)

	def test_list_customer_by_api(self):
		"""
			validate list customer by API
		"""
		
		TestUtiles.create_customer_test('111111111')
		TestUtiles.create_customer_test('222222222')
		TestUtiles.create_customer_test('333333333')
		TestUtiles.create_customer_test('444444444')
		
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)
		
		response = client.get('/customers/', {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/customers/")
		self.assertIsNone(response_data.get('previous', False))

		response = client.get(response_data.get('next'), {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/customers/")
		self.assertIsNone(response_data.get('next', False))

