from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import links_left
import os
#import secret
from django.conf import settings


def eco_landing_redirect(request):
    return redirect('/ubertool')

def qed_landing_page(request):
    #if settings.MACHINE_ID == secret.MACHINE_ID_PUBLIC:
    #    html = render_to_string('00landing_page_qed_slides_public.html', {'title': 'Ubertool'})
    #else:
    #    html = render_to_string('00landing_page_qed_slides.html', {'title': 'Ubertool'})

    html = render_to_string('00landing_page_qed_slides.html', {'title': 'qed'})

    response = HttpResponse()
    response.write(html)

    return response
