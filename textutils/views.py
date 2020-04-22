# I have created this file - Rittwick
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    #GET the text
    djtext = request.POST.get('text','default')
    rmvpun = request.POST.get('rmvpun','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremover = request.POST.get('newlineremover','off')
    slimmer = request.POST.get('slimmer','off')
    charcounter = request.POST.get('charcounter','off')

    analyzed = ""
    purpose = ['No action selected']

    # Removal of PUNCTUATIONS
    punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
    if(rmvpun=='on'):
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        purpose.append('Remove Punctuation')
    else:
        analyzed = djtext
    
    #UPPERCASE ing code
    analyzed2 = ''
    if(uppercase=='on'):
        for char in analyzed:
            analyzed2 += char.upper()
        analyzed = analyzed2
        purpose.append('Uppercase')

    analyzed2 = ''
    mystry = []


    # Newline remover
    count = 0
    if(newlineremover=='on'):
        for char in analyzed:
            if char != '\n':
                mystry.append(char)
            else:
                count = count + 1
        
        analyzed = ''.join(mystry)
        mystry = []
        for char in analyzed:
            if char != '\r':
                mystry.append(char)
            else:
                count = count + 1
        
        analyzed = ''.join(mystry)
        purpose.append('New line eliminated')
    

    # Removing extra spaces
    analyzed2 =''
    if(slimmer=='on'):
        for index, char in enumerate(analyzed):
            if(index+1<len(analyzed) and analyzed[index]==' ' and analyzed[index+1]==' '):
                pass
            else:
                analyzed2 += char
        analyzed = analyzed2
        purpose.append('Extra space removed')
    
    if(charcounter=='on'):
        purpose.append(f"Total Characters({len(analyzed)})")

    if('No action selected' in purpose and len(purpose)>1): purpose.remove('No action selected')
    params = {'purpose':', '.join(purpose), 'analyzed_text':analyzed}
    return render(request,'analyze.html',params)