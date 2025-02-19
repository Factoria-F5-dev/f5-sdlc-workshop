from django.test import TestCase
from ai_manager.models import AIModel
from django.core.exceptions import ValidationError
import requests
from unittest.mock import patch

class AIModelTest(TestCase):
    
    def test_ai_model_creation_requires_name_and_description(self):
        # Creamos una instancia del model
        model = AIModel(name="GPT-5", description="Next-gen AI model")

        # Guardamos la instancia
        model.save()

        # Comprobamos que la información esta en su sitio
        self.assertIsNotNone(model.name)
        self.assertIsNotNone(model.description)  
        self.assertEqual(model.name, "GPT-5")
        self.assertEqual(model.description, "Next-gen AI model")    

    def test_ai_model_creation_fails_without_name(self):
        # Creamos un model sin nombre
        model = AIModel(name="", description="A powerful AI model")

        # Comprobamos que fallaria en tal caso
        with self.assertRaises(ValidationError):
            model.full_clean()


    @patch("ai_manager.models.AIModel.get_random_author", return_value="Pepe Perez")
    def test_ai_model_creation_without_author_assigns_random_author(self, mock_get_author):
        model = AIModel.objects.create(name="GPT-5", description="Next-gen AI model")
        self.assertEqual(model.author, "Pepe Perez")        


    # Crea un test para comprobar el metodo __str__ del modelo
    def test_ai_model_string_representation(self):
        model = AIModel.objects.create(name="GPT-5", description="Next-gen AI", author="John Doe")
        self.assertEqual(str(model), "GPT-5 by John Doe")    

    # Crea un test para comprobar que pasa en caso de que la API https://randomuser.me/api/    
    @patch("ai_manager.models.requests.get")
    def test_ai_model_get_random_author_handles_api_failure(self, mock_requests_get):
        mock_requests_get.side_effect = requests.RequestException("API request failed")
        author = AIModel.get_random_author()
        self.assertEqual(author, "Unknown Author")
