from django.db import models

# Create your models here.

class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    matn = models.TextField()
    rasm = models.FileField(null=True, blank=True)
    korish_soni = models.PositiveSmallIntegerField(default=0)
    def __str__(self) -> str:
        return self.sarlavha[:20]
