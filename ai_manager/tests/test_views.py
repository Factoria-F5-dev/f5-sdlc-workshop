from django.test import TestCase
from django.urls import reverse
from ai_manager.models import AIModel
from django.core.management import call_command

class AIModelViewTests(TestCase):

    @classmethod
    def setUp(cls): # Se ejecuta antes de los tests
        call_command("flush", "--noinput") # Limpiar la base de datos
        call_command("loaddata", "authors.json") # Cargar datos de prueba

    def test_api_ai_model_list(self):
        response = self.client.get(reverse('ai_model_list'), HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) == 3)


    # Crea un test que compruebe que crear un modelo funciona
    def test_ai_model_create_api_response(self):
        response = self.client.post(
            reverse('ai_model_create'),
            {"name": "GPT-5", "description": "Next-gen AI", "author": "Pepe Perez"},
            HTTP_ACCEPT='application/json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response.json()["name"], "GPT-5")

    # Crea un test que compruebe que actualizar un modelo funciona
    def test_ai_model_update_api_response(self):
        response = self.client.post(
            reverse('ai_model_update', args=[1]),
            {"name": "THE NEW GPT-5", "author": "Laura Garcia", "description": "Updated AI Model"},
            HTTP_ACCEPT='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response.json()["name"], "THE NEW GPT-5")

        # El modelo tambien se actualizado en la BD
        updated_model = AIModel.objects.get(id=1)
        self.assertEqual(updated_model.name, "THE NEW GPT-5")
        self.assertEqual(updated_model.author, "Laura Garcia")
        self.assertEqual(updated_model.description, "Updated AI Model")

    # Crea un test que compruebe que borrar un modelo funciona   
    def test_ai_model_delete_api_response(self):
        call_command("flush", "--noinput")

        model = AIModel.objects.create(name="Custom Model", description="Different Data", author="Special User")
        self.assertEqual(AIModel.objects.count(), 1)

        response = self.client.post(
            reverse('ai_model_delete', args=[model.id]),
            HTTP_ACCEPT='application/json'
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(AIModel.objects.count(), 0)

