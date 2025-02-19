import requests
from django.db import models

class AIModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.author:
            self.author = self.get_random_author()
        super().save(*args, **kwargs)

    @staticmethod
    def get_random_author():
        try:
            response = requests.get("https://randomuser.me/api/")
            response.raise_for_status() 
            data = response.json()
            user = data["results"][0]
            return f"{user['name']['first']} {user['name']['last']}"
        except requests.RequestException:
            return "Unknown Author"

    def __str__(self):
        return f"{self.name} by {self.author}"
