from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Service(models.Model):
    
    name = models.CharField(max_length=200)
    
    show_intro = models.BooleanField(default=True)
    intro = HTMLField()
    
    show_process = models.BooleanField(default=True)
    process = HTMLField()
    
    show_results = models.BooleanField(default=True)
    results = HTMLField()
    
    show_its_time = models.BooleanField(default=True)
    its_time = HTMLField()
    
    show_expert_advice = models.BooleanField(default=True)
    expert_advice = HTMLField()
    
    show_approach = models.BooleanField(default=True)
    approach = HTMLField()
    
    show_equipment = models.BooleanField(default=True)
    equipment = HTMLField()
    
    show_guarantee = models.BooleanField(default=True)
    guarantee = HTMLField()
    
    show_why_us = models.BooleanField(default=True)
    why_us = HTMLField()
    
    def __str__(self):
        return f"{self.name}"
