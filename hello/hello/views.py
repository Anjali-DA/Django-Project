# created this view file
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("About Anjali")


def index(request):
    return render(request, "index.html")


def analyze(request):
    # get the text
    djtext = request.GET.get("text", "default")

    #check the check box value
    removepunc = request.GET.get("removepunc", "off")
    fullcaps = request.GET.get("fullcaps", "off")

    #check which check box is on

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Removed Punctuations", "analyzed_text": analyzed}
        # analyze the text
        return render(request, "analyze.html", params)
    elif(fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed= analyzed+char.upper()
        params = {"purpose": "Change to uppercase ", "analyzed_text": analyzed}
        # analyze the text
        return render(request, "analyze.html", params)


    else:
        return HttpResponse("Error!")



