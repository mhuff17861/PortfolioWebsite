from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.db.models import F
from .models import Visual_Poetry
#from .models import Project, Page_Header, CV_Category
import logging

logger = logging.getLogger(__name__)

# Create your views here.
# Views
def writing(request):
    """
        Returns the writing landing page
    """
    logger.debug(f'Retrieving writing view.')

    context = {}

    return render(request, 'writing/landing.html', context)

def visual_poetry(request, poem_id):
    logger.debug(f'Retrieving visual poetry view')

    try:
        poem = Visual_Poetry.objects.get(pk=poem_id)
    except Visual_Poetry.DoesNotExist:
        raise Http404("Poem does not exist")

    title_file_formatted = poem.title.lower().replace(' ', '_')

    context = {
        'poem': poem,
    }

    return render(request, 'writing/visual_poetry.html', context)