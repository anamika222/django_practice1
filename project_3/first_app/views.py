from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author': "Rahim", 'age' :20, 'lst':['python','is','best  '], 'birthday' : datetime.datetime.now(), 'val' :' ', 'courses':[
        {
        'id' : 1,
        'name' : 'Python',
        'fees' : 10000
        },
       
         {
        'id' : 2,
        'name' : 'Django',
        'fees' : 20000
        },

         {
        'id' : 3,
        'name' : 'c',
        'fees' : 30000
        }
    ]}
    return render(request,'home.html', d)