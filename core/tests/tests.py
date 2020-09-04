from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class ModelTests(TestCase):
    def testuserwithemail(self):
        email = 'pankajshindegmail.com'
        password = '12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password

        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))

    def invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(None, 'password123')

    def usersuperuser(self):
        user=get_user_model().object.create_superuser(
            email='pankajshindegmail.com',
           password= '12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
