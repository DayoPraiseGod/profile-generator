from django.db import models

class Portfolio(models.Model):
    CATEGORY = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Fullstack', 'Fullstack'),
    ]
    LANGUAGES = [
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript', 'JavaScript'),
    ]
    full_name = models.CharField(max_length=200, blank=True, null=True)
    developer = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    languages1 =  models.CharField(max_length=200, blank=True, null=True, choices=LANGUAGES)
    languages2 =  models.CharField(max_length=200, blank=True, null=True, choices=LANGUAGES)
    languages3 =  models.CharField(max_length=200, blank=True, null=True, choices=LANGUAGES)
    what_you_do = models.TextField(null=True, blank=True)
    project = models.ImageField(null=True, blank=True)
    project_title = models.CharField(max_length=200, blank=True, null=True)
    project_description = models.TextField(null=True, blank=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    linkin = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return (self.full_name).upper()

    @property
    def profile_picURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url
    
    
    


