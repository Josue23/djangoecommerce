# coding=utf-8

from django.test import TestCase, Client
'''
chamo a função reverse para usar url nomeadas nos testes
	ex: response = self.client.get('/')
		response = self.client.get(self.url)
'''
from django.core.urlresolvers import reverse

# testes unitários na "/core/templates/index.html"
class IndexViewTestCase(TestCase):

	# método setUp vai ser executado para cada teste
	def setUp(self): # método executado toda vez que inicia o teste
		# aqui eu crio coisas
		self.client = Client()
		self.url = reverse('index')

	def tearDown(self): # método executado toda vez que termina o teste
		# aqui eu removo coisas após o teste
		pass


	# testar se o código http response é 200
	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	# testar se está usando o template index.html
	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'index.html')