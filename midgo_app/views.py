from django.shortcuts import render
from .models import *
from django.conf import settings  
from pytz import timezone
import datetime
from django.http import JsonResponse
from django.shortcuts import redirect

# Create your views here.
def index(request) :

    user = request.user

    if not user.is_anonymous :

        context = { 'user' : user, 'login' : 'true' }

        return render(request, './index.html', context)
    
    else :

        context = { 'login' : 'false' }

        return render(request, './index.html', context)


def join(request) :

    return render(request, './join.html')

def main(request) :

    #notifications = Notification.objects.all()
    user = request.user
    print("main", user.username)

    if not user.is_anonymous :
        time_now = datetime.datetime.now()

        #user.check_notification = time_now
        #user.save()
        print(user.check_notification)

        # notifications = Notification.objects.filter(created_at__range=[user.check_notification, time_now])
        notifications = Notification.objects.filter(receiver = user)
        notifications_count = 0
        for notification in notifications :
            if not notification.is_checked :
                notifications_count += 1

        is_important = False
        for notification in notifications :
            if notification.category == 'reply' :
                is_important = True
                break
        print(notifications_count)

        user_list = User.objects.filter(is_recognized = 'recognized')

        context = { 'user_list' : user_list , 'notifications' : notifications , 'notifications_count' : notifications_count , 'is_important' : is_important , 'user' : user , 'login' : 'true' }

        return render(request, './main.html', context)

    else :

        return render(request, './main.html')

def check_notification(request, notification_id) :
    
    print(request.user)
    print(notification_id)

    user = request.user
    # time_now = datetime.datetime.now()
    # user.check_notification = time_now
    # user.save()
    checked_notification = Notification.objects.get(id=notification_id)
    checked_notification.is_checked = True
    checked_notification.save()

    result = { 'result' : 'true' }

    return JsonResponse(result)

def delete_notification(request, notification_id) :

    notification = Notification.objects.get(id=notification_id)
    notification.delete()

    result = { 'result' : 'true' }

    return JsonResponse(result)

def read_board(request, board_id) :

    article = Article.objects.get(id = board_id)

    context = { 'article' : article }

    return render(request, './readBoard.html', context)


def add_board(request) :

    #notifications = Notification.objects.all()
    user = request.user
    print(user.username)
    if not user.is_anonymous :
        time_now = datetime.datetime.now()

        #user.check_notification = time_now
        #user.save()
        print(user.check_notification)

        notifications = Notification.objects.filter(created_at__range=[user.check_notification, time_now])
        notifications_count = len(notifications)
        is_important = False
        for notification in notifications :
            if notification.category == 'reply' :
                is_important = True
                break
        print(notifications_count)



        context = { 'notifications' : notifications , 'notifications_count' : notifications_count , 'is_important' : is_important }

        return render(request, './addBoard.html', context)

    else :

        print("!!!!")

        return render(request, './addBoard.html')

def modify_article(request) :

    article = Article.objects.get(title = 'haha')

    context = { 'content' : article.content }

    return render(request, './summernote.html', context)

from bs4 import BeautifulSoup

def write_board(request) :

    if request.method == 'POST' :

        user = request.user

        print(request.POST['content'])
        title = request.POST['title']
        content = request.POST['content']
        soup = BeautifulSoup(content, 'html.parser') 

        print(soup.find_all('img'))

        new_article = Article.objects.create(
            creator = request.user,
            title = title,
            content = content,
        )
        new_article.save()

        for link in soup.find_all('img') :
            print(link.get('src'))
            summernoteImage = SummerNoteImage.objects.get(url = link.get('src'))
            print(summernoteImage)
            new_article_image = ArticleImage.objects.create(
                file = summernoteImage.file,
                article = new_article,
            )
            new_article_image.save()

        all_user = User.objects.all()
        for receive_user in all_user :
            new_notification = Notification.objects.create(
                creator = user,
                receiver = receive_user,
                category = 'notice',
                content = title,
                article = new_article,
            )
            new_notification.save()

        return redirect('/main/')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def summernote_uploadImage(request) :

    if request.method == 'POST' :

        print(request.FILES.getlist('uploadFile')[0])

        new_summernoteImage = SummerNoteImage.objects.create(
            file = request.FILES.getlist('uploadFile')[0],
        )
        new_summernoteImage.save()

        new_summernoteImage.url = new_summernoteImage.file.url
        new_summernoteImage.save()
        # result = { 'url' : url }
        result = { 'url' : new_summernoteImage.file.url }
        return JsonResponse(result)


def search_article(request, search_value) :

    print(search_value)
    
    articles = Article.objects.filter(title__icontains=search_value)

    print(articles)

    context = { 'articles' : articles }

    return render(request, './search_article.html', context)


def check_join(request) :

    if request.method == 'POST' :

        owner_id = request.POST['owner_id']
        owner_password = request.POST['owner_password']
        owner_name = request.POST['owner_name']
        owner_phone = request.POST['owner_phonenum']
        owner_addr = request.POST['owner_address']
        owner_email = request.POST['owner_email']

        new_user = User.objects.create(
            username = owner_id,
            password = owner_password,
            addr = owner_addr,
            phone = owner_phone,
            name = owner_name,
            email = owner_email,
        )
        new_user.set_password(owner_password)
        new_user.save()
        #print(new_user)

        #owner_password = request.POST['password']
        print(request.POST)
        print(request.FILES)
        images = request.FILES.getlist('cat_img')
        print(images)

        print(request.POST.getlist('cat_name'))

        for idx,image in enumerate(images) :
            new_cat = Cat.objects.create(
                image = image,
                name = request.POST.getlist('cat_name')[idx],
                gender = request.POST['cat_gender' + str(idx+1)],
                birth = request.POST.getlist('cat_birth')[idx],
                breed = request.POST.getlist('cat_breed')[idx],
                owner = new_user,
                eatinghabit = request.POST.getlist('cat_eatinghabit' + str(idx+1)),
                health = request.POST.getlist('cat_health' + str(idx+1)),
                route = request.POST.getlist('cat_route')[idx],
                meet = request.POST.getlist('cat_meet')[idx],
            )
            new_cat.save()

        return redirect('/main/')

def delete_checked_notification(request) :

    user = request.user
    checked_notifications = Notification.objects.filter(receiver = user, is_checked=True)
    for checked_notification in checked_notifications :
        checked_notification.delete()

    result = { "result" : "true" }

    return JsonResponse(result)

def delete_all_notification(request) :

    user = request.user

    my_notifications = Notification.objects.filter(receiver = user.username)
    for my_notification in my_notifications :
        my_notification.delete()

    result = { "result" : "true" }

    return JsonResponse(result)

"""
int a;

"""

def show_unrecognized_users(request) :

    unrecognized_users = User.objects.filter(is_recognized = 'in_progress')
    # for idx,uu in enumerate(unrecognized_users) :
    #     print(uu.username)
    #     print(uu.cats.all())

    # u = User.objects.get(username='junsik')
    # print(u.cats.all())

    context = { 'unrecognized_users' : unrecognized_users }

    print(context)

    return render(request, './recognizeUserList.html', context)

def recognize_user(request, user_id) :

    user = User.objects.get(username = user_id)

    user_cats = user.cats.all()
    cats_num = len(user_cats)

    cats = [None] * 3

    for i in range(len(user_cats)) :
        cats[i] = user_cats[i]

    print(cats)
    print(cats[0].image.url)

    context = { 'user' : user , 'cat1' : cats[0] , 'cat2' : cats[1] , 'cat3' : cats[2], 'cats_num' : cats_num}

    return render(request, './recognizeUser.html', context)

def recognize(request, user_id, user_grade) :

    recognized_user = User.objects.get(username = user_id)
    recognized_user.is_recognized = 'recognized'
    recognized_user.grade = user_grade
    recognized_user.save()

    recognized_cats = recognized_user.cats.all()

    for cat in recognized_cats :
        cat.is_recognized = 'recognized'
        cat.save()
    
    return redirect('/recognizeUserList/')

def unrecognize(request, user_id) :

    unrecognized_user = User.objects.get(username = user_id)
    unrecognized_user.is_recognized = 'unrecognized'
    unrecognized_user.save()

    unrecognized_cats = unrecognized_user.cats.all()

    for cat in unrecognized_cats :
        cat.is_recognized = 'unrecognized'
        cat.save()

    return redirect('/recognizeUserList/')

from django.contrib.auth import authenticate, login

@csrf_exempt
def login_check(request) :

    if request.method == 'POST' :
        # username = request.POST['username']
        # password = request.POST['password']
        print(request.POST)
        username = request.POST['user_id']
        password = request.POST['user_password']
        print(username, password)
        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None :
            print(user.is_recognized)
            if user.is_recognized == 'unrecognized' :
                print("승인이 반려된 사용자입니다.")

                result = { "result" : "unrecognized" }
                return JsonResponse(result)

            elif user.is_recognized == 'recognized' :
                print("승인 완료된 사용자입니다.")
                login(request, user)
                print(request.user)

                result = { "result" : "recognized" }
                return JsonResponse(result)

            elif user.is_recognized == 'in_progress' :
                print("심사 중인 사용자입니다.")

                result = { "result" : "in_progress" }
                return JsonResponse(result)

        else :

            result = { "result" : "failed" }
            return JsonResponse(result)

    # return redirect('/main/')


def login_page(request) :

    return render(request, './login.html')

from django.contrib.auth import logout

def logout_page(request) :

    logout(request)

    return redirect('/main/')
    
@csrf_exempt
def join_check_id(request) :

    if request.method == 'POST' :

        user_id = request.POST['user_id']

        try :
            user = User.objects.get(username = user_id)
            result = { "result" : "failed" }
        except :    
            result = { "result" : "success" }

        return JsonResponse(result)