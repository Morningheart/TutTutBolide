from django.db import models
    
class Range(models.Model):
    best = models.IntegerField()
    worst = models.IntegerField()
    def __str__(self):
        return self.best + " " + self.worst

class Connector(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField()
    def __str__(self):
        return self.name + " " + self.time

class Voiture(models.Model):
    idBDD = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    modelName = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    range = models.ForeignKey(
        Range, related_name="voiture", on_delete=models.CASCADE
    )
    connectors = models.ForeignKey(
        Connector, related_name="voiture", on_delete=models.CASCADE
    )
    def __str__(self):
        return self.make + " " + self.model + " " + self.version

    