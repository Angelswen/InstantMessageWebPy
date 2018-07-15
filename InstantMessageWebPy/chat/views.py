from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json
from app1.models import User
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib.auth.decorators import login_required


def function(fun):
    def inner():
        pass
    return inner


#@function
def login(request):

    return render(request, 'chat/login.html', {})


@csrf_exempt
def loginVerify(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #sql查询验证
        users = User.objects.all()

        for user in users:
            if user.username == username and user.password == password:
                user.status = 1
                user.loginTime = datetime.datetime.now()
                user.save()
                users_online = User.objects.filter(status=1)
                users_offline = User.objects.filter(status=0)

                # request.session['users_online'] = users_online
                # request.session['users_offline'] = users_offline
                request.session['username'] = username

                # print(request.session['users_offline'])

                return render(request, 'chat/index23.html', {
                    'username': username,
                    'users_online': users_online,
                    'users_offline': users_offline
                })
            else:
                continue
        return render(request, 'chat/login.html', {'error': 1})

    else:
        return render(request, 'chat/login.html', {'error': 2})
        #return render(request, 'chat/login.html', {})


def register(request):
    return render(request, 'chat/register.html', {})


@csrf_exempt
def regverify(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        users = User.objects.all()
        #注册验证
        for user in users:
            if user.username==username:
                return render(request, 'chat/register.html', {'error': 1})
        if username and email and password:
            u1 = User()
            u1.username = username
            u1.email = email
            u1.password = password
            u1.createTime = datetime.datetime.now()
            u1.save()
            #redis
            return render(request, 'chat/login.html', {})
        else:
            return render(request, 'chat/register.html', {'error': 2})
    else:
        return render(request, 'chat/login.html', {})


@login_required
def index(request):
    return render(request, 'chat/index23.html', {})


@csrf_exempt
def profile(request):
    return render(request, 'chat/profile.html', {})


@csrf_exempt
def contacts(request):
    return render(request, 'chat/contacts.html', {})


@csrf_exempt
def chat_view(request):
    username = request.session['username']
    # users_online = request.session['users_online']
    # users_offline = request.session['users_online']
    # print(users_online)
    return render(request, 'chat/chat_index.html', {
        'username': username,
        # 'users_online': users_online,
        # 'users_offline': users_offline
    })


@csrf_exempt
def changepsw(request):
    username = request.session['username']
    return render(request, 'chat/changepsw.html', {'username': username})


def index24(request):
    return render(request, 'chat/index24.html', {})


def room(request, room_name, user_name):
    room_name_json = mark_safe(json.dumps(room_name))
    user_name_json = mark_safe(json.dumps(user_name))

    users_online = User.objects.filter(status=1)
    users_offline = User.objects.filter(status=0)
    return render(request, 'chat/room.html', {
        'room_name_json': room_name_json,
        'user_name_json': user_name_json,
        'roomname': room_name,
        'username': user_name,
        'users_online': users_online,
        'users_offline': users_offline,
    })


@csrf_exempt
def change_pass(request):
    if request.method == 'POST':
        username = request.POST['username']
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        users = User.objects.all()
        print(users.count())
        for user in users:
            if user.username == username and user.password==oldpassword:
                user.password = newpassword
                user.save()
                return render(request, 'chat/changepsw.html', {'success': 1, 'username': username})
            else:
                continue

        return render(request, 'chat/changepsw.html', {'success': 0, 'username': username})
    else:
        return render(request, 'chat/changepsw.html', {})


def logout(request):
    username = request.session['username']
    users = User.objects.all()
    for user in users:
        if user.username == username:
            user.status = 0
            user.logoutTime = datetime.datetime.now()
            user.save()
        else:
            continue
    return render(request, 'chat/login.html', {})


def userprofile(request, username):
    if request.method == 'POST':
        users_online = User.objects.filter(status=1)
        users_offline = User.objects.filter(status=0)

        email = request.POST.get('email')
        user_obj = User.objects.get(email=email)

        re_password = request.POST.get('re_pwd')
        re_password_2 = request.POST.get('re_pwd_2')

        if re_password == re_password_2:
            user_obj.password = re_password
            user_obj.save()
            message = '密码修改成功'
        else:
            message = '两次密码不一致，修改密码失败'
        return render(request, 'user/userprofile.html', {
            'user_obj': user_obj,
            'users_online': users_online,
            'users_offline': users_offline,
            'message': message,
        })
    if request.method == 'GET':
        try:
            user_obj = User.objects.get(username=username)
        except:
            return redirect('/')

        users_online = User.objects.filter(status=1)
        users_offline = User.objects.filter(status=0)
        return render(request, 'user/userprofile.html', {
            'user_obj': user_obj,
            'users_online': users_online,
            'users_offline': users_offline,
        })


def back2chat(request, username):
    users_online = User.objects.filter(status=1)
    users_offline = User.objects.filter(status=0)
    return render(request, 'chat/index.html', {
        'username': username,
        'users_online': users_online,
        'users_offline': users_offline,
    })


def friendprofile(request, username, friendname):
    user_obj = User.objects.get(username=username)
    fri_obj = User.objects.get(username=friendname)

    users_online = User.objects.filter(status=1)
    users_offline = User.objects.filter(status=0)
    return render(request, 'user/friendprofile.html', {
        'user_obj': user_obj,
        'fri_obj': fri_obj,
        'users_online': users_online,
        'users_offline': users_offline,
    })


def logout_chat(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user_obj = User.objects.get(username=username)
        user_obj.is_login = 0
        user_obj.save()
        return render(request, 'chat/chat_index.html')


@csrf_exempt
def mailbox(request):
    return render(request, 'chat/mailbox.html', {})


@csrf_exempt
def mail_detail(request):
    return render(request, 'chat/mail_detail.html', {})


@csrf_exempt
def mail_compose(request):
    return render(request, 'chat/mail_compose.html', {})


@csrf_exempt
def graph_echarts(request):
    return render(request, 'chat/graph_echarts.html', {})
