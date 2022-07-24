from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from accounts.utils import  matric_no
from django.core.validators import RegexValidator

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username,phone_number, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_number=phone_number,
            # matric_no=matric_no
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number,email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            phone_number=phone_number,
            # matric_no=matric_no
        )
        # user.matric_no = matric_no
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")

# user model 
class User(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50,validators=[phone_validator])
    matric_no = models.CharField(default=matric_no(),max_length=50,unique=True)
    
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    # User role 
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phone_number']

    objects = MyAccountManager()

# review name
    def full_name(self):
        return f'{self.first_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class  College(models.Model):

    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = 'college'
        verbose_name_plural = 'colleges'
class Department(models.Model):
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.id} - {self.college.name} -{self.name}'

    class Meta:
        
        verbose_name = 'department'
        verbose_name_plural = 'departments'


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department  = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    
    
    USERNAME_FIELD = 'matric_no'
 

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'