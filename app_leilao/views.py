from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import anexo, estado, leiloeiro, matricula


def home(request):
    leiloeiros = leiloeiro.objects.all()
    matriculas = matricula.objects.all()
    estados = estado.objects.all()
    return render (request, 'dashboard.html',{"leiloeiros": leiloeiros})


login_required
def dashboard(request):
    leiloeiros = request.user.leiloeiro
    anexos = anexo.objects.filter(leiloeiros = leiloeiro)
    return render(request, 'dashboard.html', {'anexos': anexos})