from django.shortcuts import render,redirect
from .forms import creat_ac,forget_pass,change_password
from django.contrib import messages
from .models import formregister
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login  as auth_login
User = get_user_model()

# Create your views here.
def base(req):
    return render(req,'app1/home.html')

# register -->create account
def Register(req):
    if req.method == 'POST':
        form=creat_ac(req.POST)
        if form.is_valid():
            
            form.save()
            
            return redirect('todo')

    else:
        form=creat_ac()
    return render(req,'app1/register.html',{'form':form})
# login



from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        login_input = request.POST['email']
        password = request.POST['password']

        try:
            user = formregister.objects.get(email=login_input, password=password)
            # Set session or do your custom login logic
            request.session['user_id'] = user.id
            return redirect('todo')
        except formregister.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'app1/login.html')




# logout
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, "You have been logged out.")
    return redirect('login')
    # if request.method == "POST":
    #     username= request.POST['username']
        
    #     try:
    #         u=formregister.objects.get(name=username)
    #         messages.success(request,'You are logged out successfully!')
              
    #         return redirect("login")
    #     except:
    #         messages.error(request,'User not Found!')
    #         return redirect('logout')

    return render(request,'app1/logout.html')

# delete
def delete_view(request):
    if request.method == "POST":

        username=request.POST['username']
        try:
            u = formregister.objects.get(name=username)
            
            u.delete()
            messages.success(request, "The user is deleted")
            return redirect('home')
        except:
            messages.error(request, "The user not found")    
            return redirect('delete_account')
       

    return render(request,'app1/delete.html')
# change password
def forget_password(request):
    if request.method  == "POST":
        user_email=request.POST['email']

        try:
            id=formregister.objects.get(email=user_email)
            return redirect('change_password')
       
        except:
           messages.error(request,'Plese Enter a correct !')
           return redirect('forget')
    return render(request,'app1/forget_pass.html')

def change_pass(request):
    if request.method == 'POST':
        username=request.GET['username']
        user_email=request.POST['email']
        new_pass=request.POST['new_pass']
        confirm_pass=request.POST['confirm_pass']

        if new_pass != confirm_pass:
            messages.error(request,'no match password')
            print(new_pass,confirm_pass)
            return redirect("change_password")
        return redirect('todo')

            

    return render(request,'app1/change_pass.html')

def todo(req):
    return render(req,'app1/todo.html')