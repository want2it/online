from django.utils import timezone
from blog.models import Post
from django.shortcuts import get_object_or_404, render

from .models import Question

# Функция формы обратной связи
def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            soname = form.cleaned_data['soname']
            name = form.cleaned_data['name']
            telegram = form.cleaned_data['telegram']
            email = form.cleaned_data['email']
            partner = form.cleaned_data['partner']
            country = form.cleaned_data['country']
            phone = form.cleaned_data['phone']
            tarif = form.cleaned_data['tarif']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['want2it@outlook.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(email)
            try:
                send_mail(tarif, soname, name, partner, country, phone, 'https://t.me/'telegram, message, 'myemail@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'index/formamodal.html', {'form': form, 'username': auth.get_user(reguest).username})

def thanks(reguest):
    thanks = 'Мы получили Ваш запрос и уже обрабатываем его! Спасибо, что выбрали нас!'
    return render(reguest, 'index/thanks.html', {'thanks': thanks})




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request, 'index/menudinamic.html', {'posts': posts})



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'index/error-404.html', {'question': question})


