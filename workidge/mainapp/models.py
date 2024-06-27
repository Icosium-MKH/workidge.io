from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

# Create your models here.
class Person(models.Model):
#set ID and Email as primary keys

    email = models.EmailField()
    name = models.CharField(max_length=20)    
    surname = models.CharField(max_length=20)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+xxxxxxxxxxx'. Up to 15 digits allowed."
    )
    
    pn = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    title = models.CharField(max_length=50)
    created = models.DateTimeField()
    modified = models.DateTimeField()


    class Meta:
        unique_together = ('id', 'email')
        abstract = True

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Competence(models.Model):

    TYPE_CHOICES = [
        ('language','language'),
        ('library','library'),
        ('framework','framework'),
        ('soft_skill','soft_skill'),
        ('hard_skill','hard_skill'),
    ]

    LEVEL_CHOICES = [
        ('notions','notions'),
        ('beginner','beginner'),
        ('intermediate','intermediate'),
        ('advanced','advanced'),
    ]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    level = models.CharField(max_length=15, choices=TYPE_CHOICES)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        unique_together = ('id', 'name')

    def __str__(self):
        return self.name


class Subskill(models.Model):
    name = models.CharField(max_length=50)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='subskills')

    class Meta:
        unique_together = ('id', 'name')

    def __str__(self):
        return self.name
    

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
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        unique_together = ('id', 'name')

    def __str__(self):
        return self.name


class JobOffer(models.Model):    

    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='joboffers')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    created = models.DateTimeField()
    modified = models.DateTimeField()


    class Meta:
        unique_together = ('id', 'company', 'title')


    def __str__(self):
        return f"{self.company} {self.title}"
    

class Developer(Person):
    class Meta:
        db_table = 'developers'


class Recruiter(Person):
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='recruiters',default="")
    class Meta:
        db_table = 'recruiters'