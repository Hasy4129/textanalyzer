from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'title': 'Home New',
        'Bdata': 'This comes from Dictionary',
        'books': ['Php', 'Java', 'C#'],
        'record': [
            {'name': 'M Hasnain Raza', 'phone': 923182445696},
            {'name': 'Shehryar Raza', 'phone': 923275135835}
        ]
    }
    return render(request, 'home.html', data)

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def analyze(request):
    dtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == 'on':
        punctuations = '''.,:;!?'\"‘’“”()[]{}––—_/|@#$%^&*+=~`<>…°§¡¿·•∙˙¨˜ˆ´`¨¸ˇ^~¯ˉ_‐‐⁃₋₌₍₎‒––―−⁻₋₌⸗⸘⸛⸚'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        dtext = analyzed
    if fullcaps == 'on':
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        dtext = analyzed
    if newlineremove == 'on':
        analyzed = ""
        for char in dtext:
            if char != "\n" and char != "\r":
                analyzed += char
            else:
                print("no")
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        dtext = analyzed 
    if spaceremove == 'on':
        analyzed = ""
        previous_char_was_space = False

        for char in dtext:
            if char == ' ':
                if not previous_char_was_space:
                    analyzed += char
                    previous_char_was_space = True
            else:
                analyzed += char
                previous_char_was_space = False

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        dtext = analyzed

    if charcount == 'on':
        analyzed = 0
        for char in dtext:
            if not char == " ":
                analyzed = analyzed+1
        params = {'purpose': 'Length of Characters', 'analyzed_text': analyzed}
        dtext = analyzed
    if(removepunc != 'on' and newlineremove != 'on' and spaceremove != 'on' and fullcaps != 'on' and charcount != 'on'):
        params1 = {'purpose': 'Error', 'analyzed_text': 'You have not select Analyzer Type... Please Try Again!!'}
        return render(request, 'analyzeerror.html', params1)
    
    return render(request, 'analyze.html', params)