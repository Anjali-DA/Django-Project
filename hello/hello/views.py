# created this view file
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("About Anjali")


def index(request):
    return render(request, "index.html")


def analyze(request):
    # get the text
    djtext = request.POST.get("text", "default")

    # check the check box value
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover= request.POST.get("extraspaceremover", "off")

    # check which check box is on

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Removed Punctuations", "analyzed_text": analyzed}
        # analyze the text
        djtext= analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Change to uppercase ", "analyzed_text": analyzed}
        # analyze the text
        djtext= analyzed


    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "Removed Newlines ", "analyzed_text": analyzed}
        # analyze the text
        djtext= analyzed


    if extraspaceremover=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char


        params = {"purpose": "Extra space remover ", "analyzed_text": analyzed}
        # analyze the text
        djtext= analyzed



    if(removepunc!="on" and extraspaceremover!="on" and newlineremover !="on" and fullcaps!="on"):
        return HttpResponse("Error!")



    return render(request, 'analyze.html', params)
