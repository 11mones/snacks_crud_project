from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse


class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random',
            email='random@random.com',
            password='random@12345'
        )
        self.snack = Snack.objects.create(
            name='test',
            Autpurchaser=self.user,
            desc='momomo'
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'test')

    def test_detail_view(self):
        url = reverse('snack_details', args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_details.html')

    def test_create_view(self):
        url = reverse('snack_create')
        data = {
            "name": "test_2",
            "Autpurchaser": self.user.id,
            "desc": "mamamamama"
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_details.html')
        self.assertEqual(len(Snack.objects.all()), 2)
        self.assertRedirects(response, reverse('snack_details', args=[2]))

    def test_update_view(self):
        url = reverse('snack_update', args=[self.snack.id])
        data = {
            "name": "updated snack",
            "Autpurchaser": self.user.id,
            "desc": "updated description"
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertEqual(len(Snack.objects.all()), 1)  # Updated Snack, so the count should remain 1
        self.assertRedirects(response, reverse('snacks'))


    def test_delete_view(self):
        url = reverse('snack_delete', args=[self.snack.id])
        response = self.client.post(path=url, follow=True)
        self.assertEqual(len(Snack.objects.all()), 0)
        self.assertRedirects(response, reverse('snacks'))  # Assuming 'home' is the name of the home page URL

