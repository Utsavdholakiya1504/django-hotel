from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from service.models import Register
from django.contrib import messages
# from django.contrib.auth import authenticate, login as auth_login 

# def index(request):
#     return HttpResponse("project run sucessfully...")

# def index(request):
#     return render(request,"index.html")

def index(request):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,"index.html")

def about(request):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,"about.html")

def booking(request):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,"booking.html")

def contact(request):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,"contact.html")

def room(request):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,"room.html")

def service(request):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,"service.html")

def team(request):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,"team.html")

def testimonial(request):
    if not request.session.get('username'):
        return redirect('/login/')
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
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        

#         try:
#             user = Register.objects.get(username=username, password=password)
#             return redirect('/')  # Replace 'home' with your homepage URL name
#         except Register.DoesNotExist:
#             return redirect('/login/')


#     return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        try:
            user = Register.objects.get(username=username, password=password)
            request.session['username'] = user.username
            return redirect('/')  # Replace 'home' with your homepage URL name
        except Register.DoesNotExist:
            return redirect('/login/')
            # return render(request, 'login.html', {'Fail': True})


    return render(request, 'login.html')


def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('/login/')