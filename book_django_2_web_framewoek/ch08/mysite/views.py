from django.shortcuts import render

# Create your views here.
def index(request):
    years = range(1960,2021)
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        uryear = request.GET['byear']
        urfcolor = request.GET.getlist('fcolor')
    except:
        urid = None
    
    if urid != None and urpass == '12345':
        verified = True 
    else:
        verified = False
    return render(request, 'index.html', locals())