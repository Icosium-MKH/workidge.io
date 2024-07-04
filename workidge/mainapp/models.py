from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Person(AbstractBaseUser):
#set ID and Email as primary keys
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+xxxxxxxxxxx'. Up to 15 digits allowed."
    )
    
    pn = models.CharField(validators=[phone_regex], max_length=17)
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
       


    class Meta:
        unique_together = ('id', 'email')


    def has_perm(self, perm, obj=None):
        # Handle permissions here; currently, person has no permissions.
        return self.is_superuser

    def has_module_perms(self, app_label):
        # Handle module permissions here; currently, person has no permissions.
        return self.is_superuser
            
    def __str__(self):
        return f"{self.name} {self.surname}"
    
  



class Competence(models.Model):

    TYPE_CHOICES = [
        ('language','language'),
        ('library','library'),
        ('framework','framework'),
        ('soft_skill','soft_skill'),
        ('hard_skill','hard_skill'),
    ]

   

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    subskills = models.ManyToManyField('self', symmetrical=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('id', 'name')

    def __str__(self):
        return self.name


"""
class Subskill(models.Model):
    name = models.CharField(max_length=50)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='subskills')

    class Meta:
        unique_together = ('id', 'name')

    def __str__(self):
        return self.name
""" 

class Company(models.Model):

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+xxxxxxxxxxx'. Up to 15 digits allowed."
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = CountryField()
    pn = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    email = models.EmailField()
    activity_area = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id', 'name')

    def __str__(self):
        return self.name


class JobOffer(models.Model):    

    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='joboffers')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    required_skills = models.ManyToManyField(Competence, related_name='job_offers')


    class Meta:
        unique_together = ('id', 'company', 'title')


    def __str__(self):
        return f"{self.company} {self.title}"
    

class Developer(Person):
    skills = models.ManyToManyField(Competence, related_name='developers')
    class Meta:
        db_table = 'developers'


class Recruiter(Person):
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='recruiters',default="")
    class Meta:
        db_table = 'recruiters'