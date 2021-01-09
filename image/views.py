from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
# Create your views here.

def welcome(request):
    return HttpResponse('Hey you! Welcome to my Image-Gallery')

def image(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)