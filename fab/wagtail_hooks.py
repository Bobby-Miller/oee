from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import FabWorkcenters
from . import models

class FabWorkcentersModelAdmin(ModelAdmin):
    model = FabWorkcenters
    menu_label = 'Fab Workcenter'

class FabCompositionModelAdmin(ModelAdmin):
    model = models.FabComposition
    menu_label = 'Fab Composition'

class FabProductTypeModelAdmin(ModelAdmin):
    model = models.FabProductType
    menu_label = 'Fab Product Types'

class FabModelAdminGroup(ModelAdminGroup):
    menu_label = 'Fab'
    items = (FabWorkcentersModelAdmin, FabCompositionModelAdmin, FabProductTypeModelAdmin)

modeladmin_register(FabModelAdminGroup)
