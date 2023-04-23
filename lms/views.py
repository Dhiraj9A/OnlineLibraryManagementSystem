from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

                     #.....................................Login...................................#
       
# @login_required(login_url='login')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None: 
            auth.login(request, user)
            return redirect("home")   
        else: 
            messages.info(request, "Username or password is incorrect")
            return redirect("login")
    else: 
        return render(request,'login.html')
#                     #.....................................SignUp...................................#
       
# def signup(request):
#     if request.method=='POST':
#         user_image=request.FILES['image']
#         user_name=request.POST['name']
#         user_email=request.POST['email']
#         user_mobile=request.POST['mobile']
#         user_address=request.POST['address']
#         user_password=request.POST['password']

#         user_data=UserRegistration(image=user_image,name=user_name,email=user_email,mobile=user_mobile,address=user_address,password=user_password)
#         user_data.save()
#         return render(request,'signup.html')
#     else:
#       return render(request,'signup.html')

                    #.....................................Home...................................#
# @login_required(login_url='login')
def index(request):
    return render(request,'index.html')
    # return HttpResponse('home')

                     #.....................................Contact...................................#
# def contact(request):
#     return render(request,'contact.html')

#                     #.....................................About-Us...................................#
# def about(request):
#     return render(request,'about.html')
#                      #.....................................user_details...................................#

# def view_user_details(request):
#     user_details=UserRegistration.objects.all()
#     return render(request,'view_user_details.html',{'user_details':user_details})


#                      #.....................................Add books...................................#

# def add_books(request):
#     if request.method=='POST':
#         books_image=request.FILES['image']
#         books_title=request.POST['title']
#         books_description=request.POST['description']

#         books_data=Books(image=books_image,title=books_title,description=books_description)
#         books_data.save()
#         return render(request,'add_books.html')
#     else:
#         return render(request,'add_books.html')

#                     #.....................................Show_books_details...................................#

def show_books(request):
    show_books_details=Books.objects.all()
    return render(request,'show_books.html',{'show_books_details':show_books_details})
    

#                     #.....................................Update_books.........................................#
# def update_books(request,id):
#     books_details=Books.objects.get(id=id)
#     if request.method=='POST':
#         books_image=request.FILES['image']
#         books_title=request.POST['title']
#         books_description=request.POST['description']

#         books_details.image=books_image
#         books_details.title=books_title
#         books_details.description=books_description
#         books_details.save()
#         return redirect('view_books_details')
#     else:
#         return render(request,'update_books.html',{'books_details':books_details})



#                     #.....................................delete_books...................................#
# def delete_books(request,id):
#     delete_books=Books.objects.get(id=id)
#     delete_books.delete()
#     return redirect('view_books_details')
            
        

#                      #.....................................View_student_details...................................#

# def students_details(request):
#     students_details=Student.objects.all()
#     return render(request,'view_students_details.html',{'students_details':students_details})

#                     #.....................................delete_students...................................#
# def delete_students(request,id):
#     delete_students=Student.objects.get(id=id)
#     delete_students.delete()
#     return redirect('students_details')
                    

                        #.....................................Logout...................................#
       
def logout(request):
    auth.logout(request)
    return redirect("home")
