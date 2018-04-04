# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'coffee/index.html')

def beans(request):
	return render(request, 'coffee/beans.html')

def coffee(request):
	return render(request, 'coffee/coffee.html')

def about(request):
	return render(request, 'coffee/about.html')

def example(request):
	return render(request, 'coffee/example.html')