from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import FabWorkcenters

class FabWorkcentersModelAdmin(ModelAdmin):
    model = FabWorkcenters
    menu_label = 'Fab Workcenter'

modeladmin_register(FabWorkcentersModelAdmin)
