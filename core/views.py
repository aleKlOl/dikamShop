from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from hitcount.views import HitCountMixin
from hitcount.models import HitCount

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    hit_count = HitCount.objects.get_for_object(request.user)
    HitCountMixin.hit_count(request, hit_count)

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'hit_count': hit_count.hits
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
