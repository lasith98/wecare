from datetime import datetime

import pdfkit as pdfkit
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.
from clinical.models import ClinicalBook


class ExportClinicalBook(DetailView):
    model = ClinicalBook
    template_name = 'export/clinical-book-export.html'


def generate_view(request, id, view):
    if settings.PDF_KIT_BIN:

        projectUrl = request.get_host() + '/export/clinical/book/{}'.format(id)
        print(projectUrl)
        pdf = pdfkit.from_url("http://127.0.0.1:8000/export/clinical/book/4", False, configuration=pdfkit.configuration(
            wkhtmltopdf=settings.PDF_KIT_BIN), options={'encoding': "UTF-8", 'quiet': ''})
        # Generate download
        response = HttpResponse(pdf, content_type='application/pdf')
        if settings.PDF_KIT_DOWNLOAD:
            response['Content-Disposition'] = 'attachment; filename="{0}-{1}.pdf"'.format(
                datetime.now().strftime("%m-%d-%Y"), id)

        return response

    return HttpResponse('No Config')


def dddd(request):
    return render(request, '')
