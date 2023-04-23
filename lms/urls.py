from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('login/',views.login , name='login'),
    # path('signup/',views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('view_user_details/', views.view_user_details, name='view_user_details'),
    # path('add_books/', views.add_books, name='add_books'),
    # path('view_books_details/', views.view_books_details, name='view_books_details'),
    # path('update_books/<int:id>', views.update_books, name='update_books'),
    # path('delete_books/<int:id>', views.delete_books, name='delete_books'),

    # path('students_details/', views.students_details, name='students_details'),
    # path('delete_students/<int:id>', views.delete_students, name='delete_students'),

    path('show_books/',views.show_books,name='show_books'),


]
