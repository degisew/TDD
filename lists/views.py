from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        text = request.POST.get('item_text', '')
        Item.objects.create(text=text)
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
