from django.db import models

# Create your models here.
class CodeSubmission(models.Model):
    language=models.CharField(max_length=10)
    input_data=models.TextField(null=True,blank=True)
    output_data=models.TextField(null=True,blank=True)
    code=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
