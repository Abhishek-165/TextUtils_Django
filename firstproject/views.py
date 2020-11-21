#created this file by me

from django.http import HttpResponse
from django.shortcuts import render            # templates

def index(request):    #default argument
    return render(request, 'index.html')
    #return HttpResponse("Hello world")


def filteredText(request):
    textData = request.POST.get('text','default')
    checkPunctuation = request.POST.get('punctuation','off')
    checkFullCaps = request.POST.get('fullcaps','off')
    checkRemoveNewLine = request.POST.get('newline','off')
    checkextraSpace = request.POST.get('extraSpace','off')
    checkCharCount =  request.POST.get('charCount','off')


    params={}

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzedPunctuations=""
    textCapital=""
    textWithoutLine=""
    extraSpaceRemoved=""
    charCounter=0
    if checkPunctuation=="on":
        for char in textData:
            if char not in punctuations:
                analyzedPunctuations = analyzedPunctuations + char
        params.update({'filteredPunctuations':analyzedPunctuations})
        
    if checkFullCaps == "on":
        textCapital = textData.upper()
        params.update({'textCapital':textCapital})
        
    if checkRemoveNewLine == 'on':
        for char in textData:
            if char!='\n':
                textWithoutLine =textWithoutLine+char
        params.update({'removeNewLine':textWithoutLine})
    if checkextraSpace == 'on':
        for index,char in enumerate(textData):
            if not(textData[index]==" " and textData[index+1]==" "):
                extraSpaceRemoved = extraSpaceRemoved + char
        params.update({'extraSpaceRemoved':extraSpaceRemoved})
        
    if checkCharCount == "on":
        charCounter = len(textData)
        params.update({'charCounter':charCounter})
        
    if checkCharCount=="off" and checkextraSpace == 'off' and checkFullCaps == 'off' and checkPunctuation =='off' and checkPunctuation == 'off':
        return HttpResponse("<center><h2>Please select an option....</h2></center>")
    #params={'filteredPunctuations':analyzedPunctuations,'textCapital':textCapital,'removeNewLine':textWithoutLine,'extraSpaceRemoved':extraSpaceRemoved,'charCounter':charCounter}
    return render(request,'analyze.html',params)