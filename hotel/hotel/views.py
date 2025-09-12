import os  
from django.conf import settings
from service.models import Register
from django.shortcuts import render ,redirect ,get_object_or_404

# def index(request):
#     return HttpResponse("project run sucessfully...")

# def index(request):
#     return render(request,"index.html")

def page(request,template,a1=None):
    if not request.session.get('username'):
        return redirect('/login/')
    return render(request,template,a1)



def index(request):
    # if not request.session.get('username'):
    #     return redirect('/login/')
    return page(request,"index.html")


def about(request):
     return page(request,"about.html")

def booking(request):
     return page(request,"booking.html")

def contact(request):
     return page(request,"contact.html")

def room(request):
     return page(request,"room.html")

def service(request):
     return page(request,"service.html")

def team(request):
     return page(request,"team.html")

def testimonial(request):
     return page(request,"testimonial.html")

def header(request):
    return page(request,"header.html")

 


  
def register(request):
    
    try: 
        # Get form data
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        file = request.FILES.get("file")
        a1 = Register(username=username,email=email,password=password,file=file)
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
    return page(request,"user.html",a1)



def delete(request,id):
    data=Register.objects.get(id=id)
    data.delete()
    # print(data)
    if data.file:
        file_path = os.path.join(settings.MEDIA_ROOT, str(data.file))
        if os.path.isfile(file_path):
            os.remove(file_path)
     
    return redirect("/user/")


def update(request,id):
    data=Register.objects.get(id=id)

    if request.method == "POST":
        data.username=request.POST.get("username")
        data.email=request.POST.get("email")
        data.password=request.POST.get("password")
 
        obj = get_object_or_404(Register, pk=id)
        if request.POST.get("remove_image") == "1":
            if obj.file:
                # delete file from storage AND clear DB field
                obj.file.delete(save=False)
                obj.file = None 



        new_file = request.FILES.get("file")
        
        if new_file:
            # Delete old file if it exists
            if data.file:
                old_file_path = os.path.join(settings.MEDIA_ROOT, str(data.file))
                if os.path.isfile(old_file_path):
                    os.remove(old_file_path)
            # Set new file
            data.file = new_file
            
        data.save()
        return redirect("/user/")

    return render(request,"update.html",{"data":data})



def login(request):

    if request.session.get('username'):
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        try:
            user = Register.objects.get(username=username, password=password)
            request.session['username'] = user.username
            return redirect('/')   
        except Register.DoesNotExist:
            return redirect('/login/')
            # return render(request, 'login.html', {'Fail': True})


    return render(request, 'login.html')


def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('/login/')

def fileupload(request):
     return redirect('/login/')