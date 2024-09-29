from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from lists.models import Item


def home_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        text = request.POST.get('item_text', '')
        Item.objects.create(text=text)
    else:
        text = ''

    return render(
        request,
        'home.html',
        {'new_item_text': text})
