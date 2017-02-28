from django.db import models

# Create your models here.
class FabWorkcenters(models.Model):
    workcenter = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Fab Workcenter'
        verbose_name_plural = 'Fab Workcenters'

    def __str__(self):
        return self.workcenter

class FabComposition(models.Model):
    composition = models.CharField(max_length=4)
    primary_material = models.CharField(max_length=16)
    primary_stabilizer = models.CharField(max_length=16)

    class Meta:
        verbose_name = 'Fab Composition'
        verbose_name_plural = 'Fab Compositions'

    def __str__(self):
        return self.composition

class FabProductType(models.Model):
    product_type = models.CharField(max_length=4)

    def __str__(self):
        return self.product_type