from django.db import models

# Create your models here.
                    #.................................UserRegistration..........................................#
class UserRegistration(models.Model):
    image=models.ImageField(blank=True,null=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    mobile=models.IntegerField()
    address=models.CharField(max_length=255)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.name

                #.................................Books..........................................#
class Books(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,null=True)

    def __str__(self) -> str:
        return self.title

                #.................................category..........................................#
class Category(models.Model):
    # add_books=models.OneToOneField(Books,on_delete=models.SET_NULL, null=True)
    pass

class Transation(models.Model):
    pass


                #.................................Student..........................................#
class Student(models.Model):
    add_Student=models.ForeignKey(UserRegistration,on_delete=models.CASCADE ,default=True)
    add_books =models.ForeignKey(Books,on_delete=models.CASCADE, default=True)
    issuedDate=models.DateField()
    returnDate=models.DateField()

    def __str__(self) -> str:
        return self.add_Student.name






