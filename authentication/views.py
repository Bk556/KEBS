from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

# Create your views here.
def Login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #import pdb;pdb.set_trace()

        if user is not None:
            login(request, user)
            request.session['firstname'] = user.first_name
            request.session['lastname'] = user.last_name
            request.session['email'] = user.email
            login(request, user)
            if user.groups.filter(name='client').exists():
                request.session['group'] = 'client'
                return render(request, "dashboard.html")
            elif user.groups.filter(name='membership_officer').exists():
                request.session['group'] = 'membership_officer'
                # return render(request, "membershipofficer dashboard.html")
                return redirect("dashboard:membershipofficer dashboard")

        else:
            return render(request, "Login.html")
            #return render(request, "dashboard.html")
        #else:
            #return render(request, "Login.html")

    return render(request, 'Login.html')

def Logout_view(request):
    logout(request)
    return redirect('authentication:Login')

def Register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email
        )
        try:
            newuser.save()

            # Assign user to a specific group
            group = Group.objects.get(name='client')
            newuser.groups.add(group)
            return render(request, 'Login.html')
        except:
            return HttpResponse("something went wrong")
    else:
        # form = UserForm()
        return render(request, 'registration.html')

# def signout(request):
#     logout(request)
#     return redirect('/')



    #return render(request,'registration.html')