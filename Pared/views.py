from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from. models import User, Message, Comment


def login(request):
    return render(request, "index.html")


def create_user(request):
    register_user = User.objects.filter(email = request.POST['email'])

    if len(register_user) != 0:
        messages.error(request, "User with that email already exists!")
        return redirect('/')

    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        birthday = request.POST['birthday'],
        email = request.POST['email'],
        password = hashed_pw,
    )

    request.session['user_id'] = new_user.id

    return redirect('/pared')

def log_in(request):
    login_user = User.objects.filter(email = request.POST['email'])

    if len(login_user) == 0:
        messages.error(request, "Please check your email and password.")
        return redirect('/')

    user = login_user[0]

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Please check your email and password.")
        return redirect('/')

    request.session['user_id'] = user.id

    return redirect('/pared')


def pared(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'current_user': current_user,
        'messages' : Message.objects.all(),
        'comments' : Comment.objects.all(),
    }


    return render(request, "pared.html", context)



def post_message(request):
    
    if request.method == 'POST':
        new_message = Message.objects.create(
            message_text = request.POST['msg'],
            user = User.objects.get(id = request.session['user_id'])
        )
        new_message.save()
    return redirect('/pared')

def post_comment(request, msg_id):
   
    if request.method == 'POST':
        new_comment = Comment.objects.create(
            comment_text = request.POST['cmnt'],
            user = User.objects.get(id = request.session['user_id']),
            message = Message.objects.get(id = msg_id)
        )
        new_comment.save()
    return redirect('/pared')

def logout(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in!")
        return redirect('/')

    request.session.clear()

    return redirect('/')

