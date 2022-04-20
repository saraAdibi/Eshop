from django.shortcuts import render
from eshop_sliders.models import Slider
from eshop_settings.models import SiteSetting


# header code behind
def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Footer.html', context)


# code behind
def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
        'sliders': sliders
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'about_page.html', context)