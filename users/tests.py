from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import UserCreationForm




class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='bogususer', email='normal@user.com', password='AbCd1@3$')
        self.assertEqual(user.username, 'bogususer')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='', password="AbCd1@3$")
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='normal@user.com', password="AbCd1@3$")

    def test_create_user_duplicate_email_fails(self):
        User = get_user_model()
        user1 = User.objects.create_user(username='bogususer', email='normal@user.com', password='AbCd1@3$')
        self.assertEqual(user1.email, 'normal@user.com')

        # The following should fail, but does not; the second user with the same email still passes!
        
        # try:
        with self.assertRaises(Exception) as err:
            user2 = User.objects.create_user(username='copycatuser', email='normal@user.com', password='Zzzz09876')
            print(err)
        # except AssertionError:
        #     pass
        # self.assertIsNone(user2.username)  # FAILS - "is not None"
        self.assertEqual(user1.email, 'normal@user.com')
        self.assertEqual(user1.username, 'bogususer')
        self.assertEqual(user2.email, 'normal@user.com')
        self.assertEqual(user2.username, 'copycatuser')


# Helper methods - - - - - - - - - - - - - - - - - - - -

    def helper_page_status_200(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def helper_page_template_check(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, f'{url_name}.html')

# Tests - - - - - - - - - - - - - - - - - - - - - - - - -

    def test_home_page_status_pass(self):
        self.helper_page_status_200('home')

    def test_home_page_status_fail(self):
        response = self.client.get('fred')
        self.assertEqual(response.status_code, 404)

    def test_home_page_template(self):
        self.helper_page_template_check('home')

    def test_signup_page_status_pass(self):
        self.helper_page_status_200('signup')

    def test_login_page_status_pass(self):
        self.helper_page_status_200('login')


