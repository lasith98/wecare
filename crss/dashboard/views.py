from django.shortcuts import render


# Create your views here.

def dashboard(request):
    return render(request, 'layout/dashboard-layout.html')


def test(request):
    return render(request, 'vv.html')


def patient_reg(request):
    return render(request, 'patient-reg.html')
