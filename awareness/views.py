from django.shortcuts import render


def awareness_page(request):
    return render(request, "awareness.html")
