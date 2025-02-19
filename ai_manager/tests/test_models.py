from django.test import TestCase
from ai_manager.models import AIModel
from django.core.exceptions import ValidationError
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
            model.save()


    @patch("ai_manager.models.AIModel.get_random_author", return_value="Pepe Perez")
    def test_ai_model_creation_without_author_assigns_random_author(self, mock_get_author):
        model = AIModel.objects.create(name="GPT-5", description="Next-gen AI model")
        self.assertEqual(model.author, "Pepe Perez")        


    # Crea un test para comprobar el metodo __str__ del modelo
        

    # Crea un test para comprobar que pasa en caso de que la API https://randomuser.me/api/    
