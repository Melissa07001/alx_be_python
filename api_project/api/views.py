from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def book_list(request):
    books = [
        {"id": 1, "title": "Book 1", "author": "Author A"},
        {"id": 2, "title": "Book 2", "author": "Author B"},
    ]
    return JsonResponse(books, safe=False)
