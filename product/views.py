from django.shortcuts import render, redirect
from .models import Feedback, Product
from .forms import FeedbackForm, SearchForm
from django.db.models import Q

# --------------------READ(view)------------------------
def index(request):
    return render(
        request,
        'product/index.html'
    )

def about(request):
    return render(
        request,
        'product/about.html'
    )

def gallery(request):
    products = Product.objects.all()
    return render(
        request,
        'product/gallery.html',
        {'products' : products}
    )

def testimonial(request):
    return render(
        request,
        'product/testimonial.html'
    )

# def search(request):
#     search = request.GET.get('search')
#
#     if search.isdigit():
#         info = Product.objects.filter(price=search)
#     else:
#         info = Product.objects.filter(title__contains=search)
#
#     return render(request, 'base.html', {'products': info})


# --------------------CREATE------------------------
def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.save()
            # data = Feedback.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = FeedbackForm()
    context = {
        'form_for_temp': form,
    }
    return render(request, 'product/contact.html', context)







