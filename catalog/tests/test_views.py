# coding=utf-8

# Client simula o browser
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy

from catalog.models import Category, Product

# testar a view inicial que lista todos os produtos
class ProductListTestCase(TestCase):

	def setUp(self):
		self.url = reverse('catalog:product_list')
		self.client = Client()

		# criando dez produtos para teste
		self.products = mommy.make('catalog.Product', _quantity=10)

	def tearDown(self):
		# remove todos os produtos
		Product.objects.all().delete()

	# teste de status code do template
	def test_view_ok(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'catalog/product_list.html')

	# testar o que tem no context
	# no context tem que ter o product_list que são todos os meus produtos
	def test_context(self):
		# esse response tem um context embutido que renderiza o template
		response = self.client.get(self.url)

		# testando se tem o product_list
		self.assertTrue('product_list' in response.context)

		# testando se tem dez produtos
		product_list = response.context['product_list']
		self.assertEquals(product_list.count(), 10)

