from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product, Feedback, Contact
from .forms import ContactForm, EmailForm
from .forms import UserRegistrationForm, UserAuthenticationForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView




# --------------------REGISTER------------------------
def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = UserRegistrationForm()
    return render(request, 'product/register.html', {'register_form': form})


# --------------------LOGIN------------------------
def loginUser(request):
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему')
            return redirect('index')
    else:
        form = UserAuthenticationForm()
    return render(request, 'product/login.html', {'login_form':form})


# --------------------LOGOUT------------------------
def logoutUser(request):
    logout(request)
    return redirect('login')

# --------------------READ(view)------------------------
# def index(request):
#     feedback_temp = Feedback.objects.all()
#     context = {
#         'feedback_tmp': feedback_temp
#     }
#     return render(
#         request,
#         'product/index.html',
#         context
#     )
class HomeView(ListView):
    model = Feedback
    template_name = 'product/index.html'
    context_object_name = 'feedback_tmp'




# def about(request):
#     return render(
#         request,
#         'product/about.html'
#     )

class AboutView(ListView):
    template_name = 'product/about.html'

def gallery(request):
    products = Product.objects.all()
    return render(
        request,
        'product/gallery.html',
        {'products' : products}
    )

def testimonial(request):
    feedback_temp = Feedback.objects.all()
    context = {
        'feedback_tmp': feedback_temp
    }
    return render(request, 'product/testimonial.html', context)

def search(request):
    search = request.GET.get('search')

    if search.isdigit():
        info = Product.objects.filter(price=search)
    else:
        info = Product.objects.filter(title__contains=search)

    return render(request, 'base.html', {'products': info})


# --------------------CREATE------------------------
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             data = form.save()
#             # data = Feedback.objects.create(**form.cleaned_data)
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     context = {
#         'form_for_temp': form,
#     }
#     return render(request, 'product/contact.html', context)

class ContactView(CreateView):
    model = Contact
    fields = ('name', 'email', 'phone', 'massage')
    template_name = 'product/contact.html'




def send_message_smtp(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],
                             form.cleaned_data['content'],
                             '9pedobear@gmail.com',
                             ['kayratsagynbekov@gmail.com'],
                             fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('.')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = EmailForm()
    return render(request, 'product/email.html', {"form": form})


