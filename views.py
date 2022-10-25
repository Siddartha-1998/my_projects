
from cgitb import html
from distutils.log import ERROR
import http
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
import os
import json


class Test(APIView):
    def post(self,res):
        with open("data.json",mode = "w") as f:
            json.dump(res.data,f)
        return HttpResponse("data taken")

    def get(self,res):
        with open("data.json",mode = "r") as f:
            main = json.load(f)
            main_1 = main
            print(main)
        return HttpResponse(json.dumps(main_1), content_type="application/json")

           
        
    























    #     html = """
    #     /
    #     <html>
    #     <head>
    #     <body>
    #     <h>web page is working </h>
    #     </body>
    #     </head>
    #     </html>
    # /

    # """
    #     with open('temp1.html', mode = 'w') as f:
    #         f.write(html)
    #     return render(request,'temp1.html',html)
   
        
    


