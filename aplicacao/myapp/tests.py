from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pessoa

class PessoaTests(APITestCase):
    # Todos os testes devem começar com test_
    def test_postando_pessoa(self):
        url = reverse('pessoa')
        data = {'username': 'Matheus', 'password': 'Roberto'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_postando_pessoa2(self):
        url = reverse('pessoa2')
        data = {'nome': 'Ronado', 'sobrenome': 'de Assis', 'nick':'ronaldinho10', 'senha':'saponalagoa'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Teste postando usuário sem senha, no qual é necessário pelos atributos do serializer  
    def test_postando_errado_pessoa2(self):
        url = reverse('pessoa2')
        data = {'nome': 'Ronado', 'sobrenome': 'de Assis', 'nick':'ronaldinho10'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)