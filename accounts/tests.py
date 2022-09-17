from django.test import TestCase
from .models import User

# Create your tests here.


class UserModelTestCase(TestCase):
    def test_create_user_when_valid(self):
        email = "qwer@qwer.com"
        password = "password"

        user = User.objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_user_when_email_not_given_raises_error(self):
        email = None
        password = "password"

        self.assertRaises(
            ValueError, User.objects.create_user, email=email, password=password
        )

    def test_create_user_when_valid(self):
        email = "qwer@qwer.com"
        password = "password"

        user = User.objects.create_superuser(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_superuser_when_email_not_given_raises_error(self):
        email = None
        password = "password"

        self.assertRaises(
            ValueError, User.objects.create_superuser, email=email, password=password
        )

    def test_create_superuser_when_is_staff_is_false_raises_error(self):
        email = "s@wp.pl"
        password = "password"

        self.assertRaises(
            ValueError,
            User.objects.create_superuser,
            email=email,
            password=password,
            is_staff=False,
        )

    def test_create_superuser_when_is_superuser_is_false_raises_error(self):
        email = "s@wp.pl"
        password = "password"

        self.assertRaises(
            ValueError,
            User.objects.create_superuser,
            email=email,
            password=password,
            is_superuser=False,
        )
