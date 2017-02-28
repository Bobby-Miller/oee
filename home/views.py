from fab.models import FabWorkcenters
from oee.settings.base import HQDB_URL
from django.shortcuts import render
import requests
from .forms import OEEFilterForm

def home_page(request):
    fab_wc = FabWorkcenters.objects.all().values_list('workcenter')
    fab_wc_list = [item[0] for item in fab_wc]
    # Access Syspro/SQL for additional info on WC.
    hqdb_wc_detail = requests.post(
        HQDB_URL + '/workcenter/',
        json={'workcenters': fab_wc_list}
        ).json()

    if request.method == 'POST':
        print(request.POST)
        form = OEEFilterForm(request.POST)

    else:
        form = OEEFilterForm()

    return render(
        request,
        'home/home_page.html',
        {
            'wc_detail': hqdb_wc_detail,
            'form': form,
        }
    )
