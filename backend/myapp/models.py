from django.db import models

#sector model
class Sector(models.Model):
    sector=models.CharField(max_length=200)

    def __str__(self):
        return self.sector

#client model
class Client(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

#project model
class Project(models.Model):
    project_name=models.CharField(max_length=200)
    details=models.TextField()
    client_name=models.ForeignKey(Client, on_delete=models.CASCADE)
    sector=models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name