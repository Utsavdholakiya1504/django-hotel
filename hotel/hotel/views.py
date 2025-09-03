from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from service.models import Register
from django.contrib import messages
from django.contrib.auth import authenticate, login
 
# def index(request):
#     return HttpResponse("project run sucessfully...")

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def booking(request):
    return render(request,"booking.html")

def contact(request):
    return render(request,"contact.html")

def room(request):
    return render(request,"room.html")

def service(request):
    return render(request,"service.html")

def team(request):
    return render(request,"team.html")

def testimonial(request):
    return render(request,"testimonial.html")

def header(request):
    return render(request,"header.html")

# def login(request):
#     return render(request,"login.html")




  
def register(request):
    
    try: 
        # Get form data
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        a1 = Register(username=username,email=email,password=password)
        a1.save()

       
        # Check if passwords match

        # if password == confirm_password:
        #     a1 = Register(username=username,email=email,password=password)
        #     a1.save()
        #     return redirect('/user/')

        # else:
        #     return render(request, 'register.html', {'password': True})
        

        # Print form data to terminal
        # print("Form submitted:")
        # print("Username: ",username)
        # print("Email: ",email)
        # print("Password: ",password)
        # print("Confirm Password: ",confirm_password)
        

        # Redirect to success page
        return redirect('/user/')
    
        # Render success page
        return render(request, 'register.html', {'success': True})

        # messages.success(request, "Registration successful!")
        # return redirect('/user/')
 
    except:pass
    
    return render(request, 'register.html')
 

def user(request):
    data = Register.objects.all()
    a1={"data":data}
    return render(request,"user.html",a1)



def delete(request,id):
    data=Register.objects.get(id=id)
    # print(data)
    data.delete()
    return redirect("/user/")


def update(request,id):
    data=Register.objects.get(id=id)

    if request.method == "POST":
        data.username=request.POST.get("username")
        data.email=request.POST.get("email")
        data.password=request.POST.get("password")
        data.save()
        return redirect("/user/")

    return render(request,"update.html",{"data":data})


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f'Welcome, {username}!')
#                 return redirect('home') # Redirect to a success page like 'home'
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             form = LoginForm()
#     return render(request, 'registration/login.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('home')  # Replace 'home' with your homepage URL name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')