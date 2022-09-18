from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post
from django.http import Http404
from django.http import HttpResponse


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostListHome(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'home.html'

class PostListInvite(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'invite.html'


class PostListAbout(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'about.html'


class PostListJoin(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'join.html'


class PostListVacancy(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'vacancy.html'


class PostListPrice(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'price.html'

class PostListDocs(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'docs.html'

class PostListUpload(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'upload.html'

#'blog.html', {'title': 'Хочу в IT · Блог', 'meta_1': 'Хочу в IT. Блог для IT-рекрутеров и не только.', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Блог, новости, истории и советы.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})




def post_spis(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
    return render(request, 'home.html', {'posts': posts, 'title': 'Хочу в IT · Рекрутинговое агентство', 'meta_1': 'Хочу в IT. Рекрутинговое агентство по подбору IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Мы соберем Вашу команду мечты! Работаем с применением различных техник в части поиска и подбора персонала, используем как классические инструменты, так и современные методики для оценки и поиска сотрудников.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})





def blog(request):
    posts = Post.objects.order_by('-created_on')
    return render(request, 'blog.html', {'posts': posts, 'title': 'Хочу в IT · Блог', 'meta_1': 'Хочу в IT. Блог для IT-рекрутеров и не только.', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Блог, новости, истории и советы.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def join(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'join.html', {'posts': posts, 'title': 'Хочу в IT · О нас', 'meta_1': 'Хочу в IT. О том, как найти IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. О компании, контакты, отзывы, партнеры.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def upload(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'upload.html', {'posts': posts, 'title': 'Хочу в IT · О нас', 'meta_1': 'Хочу в IT. О том, как найти IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. О компании, контакты, отзывы, партнеры.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def invite(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'invite.html', {'posts': posts, 'title': 'Хочу в IT · О нас', 'meta_1': 'Хочу в IT. О том, как найти IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. О компании, контакты, отзывы, партнеры.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def about(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'about.html', {'posts': posts, 'title': 'Хочу в IT · О нас', 'meta_1': 'Хочу в IT. О том, как найти IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. О компании, контакты, отзывы, партнеры.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def vacancy(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'vacancy.html', {'posts': posts, 'title': 'Хочу в IT · Вакансии', 'meta_1': 'Хочу в IT. Открытые вакансии для IT-специалистов и разработчиков', 'meta_2': 'Вакансии для IT-специалистов в рекрутинговом агентстве "Хочу в IT" (Want to IT). DevOps, SecOps, Python, Java, PHP, DBA, iOS, QA, Architect, System Administrator.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def price(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'price.html', {'posts': posts, 'title': 'Хочу в IT · Цены', 'meta_1': 'Хочу в IT. Как просто найти IT-специалистов. Самые низкие цены на рынке!', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Наши цены и возможности. Самые вкусные и выгодные предложения!', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def docs(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'docs.html', {'posts': posts, 'title': 'Хочу в IT · Документы', 'meta_1': 'Хочу в IT. Рекрутинговое агентство по подбору IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Мы соберем Вашу команду мечты! Работаем с применением различных техник в части поиска и подбора персонала, используем как классические инструменты, так и современные методики для оценки и поиска сотрудников.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})


