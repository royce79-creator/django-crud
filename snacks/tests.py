from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
from django.contrib.auth.signals import user_logged_in

class SnacksTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username ='test',
      email ='test@email.com',
      password ='password',
    )
    self.snack = Snack.objects.create(
      title='Lays',
      purchaser= self.user,
      description = 'This snack is salty'
    )
  
  def test_string_representation(self):
    self.assertEqual(str(self.snack), 'Lays')
  
  def test_snack_name(self):
    self.assertEqual(f'{self.snack.title}', 'Lays')
  
  def test_model_to_setup(self):
    self.assertEqual(self.snack.title, 'Lays')
    self.assertEqual(str(self.snack.purchaser), 'test')
    self.assertEqual(self.snack.description, 'This snack is salty')

# Test for ListView
  def test_snack_list_view(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Lays')
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')

# Test for DetailView
  def test_snack_detail_view(self):
    url = reverse('snack_detail', args='1')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'This snack is salty')
    self.assertTemplateUsed('snack_detail.html')
    self.assertTemplateUsed(response, 'base.html')

# Test for CreateView
  def test_snack_create_view(self):
    response = self.client.post(reverse('snack_create'),
    {
      'title': 'Chicken',
      'purchaser': self.user.id,
      'description': 'This is not a snack.'
    }, follow = True
    )

    self.assertRedirects(response, reverse('snack_detail', args='2'))
    self.assertContains(response, 'This is not a snack.')
    self.assertTemplateUsed(response, 'snack_detail.html')

# Test for UpdateView
  def test_snack_update_view(self):
    response = self.client.post(reverse('snack_update', args='1'),
    {
      'title': 'Chicken Updated',
      'purchaser': self.user.id,
      'description': 'This is a snack to some.'
    }, follow = True
    )

    self.assertRedirects(response, reverse('snack_detail', args='1'))

# Test for DeleteView
  def test_snack_delete_view(self):
    response = self.client.post(reverse('snack_delete', args='1'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, ' snack_delete.html')

    response = self.client.post(reverse('snack_delete', args='1', follow=True))
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertNotContains(response, 'Lays')
