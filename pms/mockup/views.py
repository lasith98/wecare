from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def mockup_lab_report(request):
    lab_report = {
        "name": ''
    }

    return JsonResponse({
        next(val for key, val in lab_report.items() if request.POST.get("q", "") in key)
    })
