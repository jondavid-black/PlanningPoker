from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField("User Name", max_length=100)
    color = models.CharField("User Preferred Color", max_length=100)
    
    def __str__(self):
        return f"{self.name}"

class Team(models.Model):
    name = models.CharField("Team Name", max_length=100)
    users = models.ManyToManyField(User, verbose_name="Users in Team")

    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    id = models.AutoField("Game ID", primary_key=True)
    name = models.CharField("Game Name", max_length=100)
    team = models.ForeignKey(Team, verbose_name="Game for Team", on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    visible = models.BooleanField("Visible", default=False)

    def __str__(self):
        return f"{self.name}"

class Card(models.Model):
    value = models.IntegerField("Card Value")
    user = models.ForeignKey(User, verbose_name="Card for User", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, verbose_name="Card in Game", on_delete=models.CASCADE)

    def __str__(self):
        return f"Card is {self.value} for {self.user} in {self.game}"
