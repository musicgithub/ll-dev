from django.http import HttpReseponse


def index(request):
    return HttpResponse('index')
