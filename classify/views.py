from django.http import HttpResponse
from django.shortcuts import render


def classify_req(request, file_path):
    return HttpResponse(file_path)