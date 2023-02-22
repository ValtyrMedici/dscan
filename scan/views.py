from django.shortcuts import render, redirect
from .forms import ScanForm
from .models import *

from .scan_processor import *
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def view_dscan(request):

    return render(request, 'index.html')

def view_scan(request):
    #logger.info("invalid")
    if request.method == 'POST':
        form = ScanForm(request.POST)

        if form.is_valid():

            type = determine_type(form.cleaned_data['scan'])
            if type == 0:
                parse_dscan(form.cleaned_data['scan'])

            #print(form.cleaned_data)

        else:
            logger.info(form.errors)
        
    return redirect('dscan-home')
    