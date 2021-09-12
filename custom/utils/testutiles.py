from rest_framework.authtoken.models import Token
from modules.customers.models import Customer
from django.contrib.auth.models import User

class TestUtiles:

	_USER_USERNAME = 'test'
	_USER_EMAIL = 'test@test.com'
	_USER_PASSWORD = 'T3ST!'

	@staticmethod
	def create_customer_test(identification, name="TEST_CUSTOMER_NAME", address="TEST_CUSTOMER_ADDRESS"):
		customer = Customer()
		customer.identification = identification
		customer.name = name
		customer.address = address
		customer.save()

	@staticmethod
	def create_user_test():
		user = User.objects.create_user(
			TestUtiles._USER_USERNAME, TestUtiles._USER_EMAIL, TestUtiles._USER_PASSWORD)
		user.save()
		return user

	@staticmethod
	def create_token_test(user=None):
		if not user:
			user = TestUtiles.create_user_test()
		token, _ = Token.objects.get_or_create(user=user)
		return "Token " + token.key
