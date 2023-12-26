from .models import Home, Shop


def home(request):
    items = Home.objects.filter(is_visible=True)
    return {'items': items}


def shop(request):
    items = Shop.objects.filter(is_visible=True)
    return {'shop': items}
