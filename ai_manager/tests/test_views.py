from django.test import TestCase
from django.urls import reverse
from ai_manager.models import AIModel
from django.core.management import call_command

class AIModelViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        call_command("loaddata", "authors.json")

    def test_api_ai_model_list(self):
        response = self.client.get(reverse('ai_model_list'), HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) == 3)


    # Crea un test que compruebe que crear un modelo funciona
    
    # Crea un test que compruebe que actualizar un modelo funciona

    # Crea un test que compruebe que borrar un modelo funciona   
