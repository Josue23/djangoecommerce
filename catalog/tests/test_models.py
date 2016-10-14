# coding=utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse

# model_mommy automatiza os testes
from model_mommy import mommy

from catalog.models import Category, Product


class CategoryTestCase(TestCase):

	def setUp(self):
		self.category = mommy.make('catalog.Category')

	# testar se o método get_absolute_url está funcionando
	def test_get_absolute_url(self):	
		self.assertEquals(
			self.category.get_absolute_url(),
			reverse('catalog:category', kwargs={'slug': self.category.slug})
		)

# testando com o model_mommy com apenas o slug obrigatorio, os outros campos são aleatorios
class ProductTestCase(TestCase):

	def setUp(self):
		self.product = mommy.make(Product, slug='produto')

	# testar se o método get_absolute_url está funcionando
	def test_get_absolute_url(self):	
		self.assertEquals(
			self.product.get_absolute_url(),
			reverse('catalog:product', kwargs={'slug': 'produto'})
		)