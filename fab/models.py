from django.db import models

# Create your models here.
class FabWorkcenters(models.Model):
    workcenter = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Fab Workcenter'
        verbose_name_plural = 'Fab Workcenters'

    def __str__(self):
        return self.workcenter
