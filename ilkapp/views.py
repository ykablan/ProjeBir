from django.shortcuts import render, HttpResponse

def anaSayfa(request):
    return HttpResponse("Merhaba, Django!")