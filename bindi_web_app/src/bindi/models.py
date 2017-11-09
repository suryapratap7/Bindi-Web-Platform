from django.db import models
from django.utils import timezone

# models.ForeignKey('auth.User')
class Colleges(models.Model):
    college_id = models.CharField(max_length=10)
    college_name = models.CharField(max_length=500)
    college_short = models.CharField(max_length=10)

class Programs(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    length = models.IntegerField()
    career = models.IntegerField()
    delivery = models.IntegerField()
    min_units = models.IntegerField()
    convenor = models.CharField(max_length=100)
    convenor_email = models.EmailField()

class Spec_Major(models.Model):
    program = models.ForeignKey(Programs)
    major_id = models.CharField(max_length=10)
    major_type = models.IntegerField()
    major_title = models.CharField(max_length=200)
    major_min_units = models.IntegerField()

class Courses(models.Model):
	course_code = models.CharField(max_length=8)
	course_title = models.CharField(max_length=100)
	course_length = models.IntegerField()
	course_units = models.IntegerField()
	course_college = models.ForeignKey(Programs)
	course_major = models.ForeignKey(Spec_Major)
	course_convenor = models.CharField(max_length=100)
	course_convenor_email = models.EmailField()

class Course_Offering(models.Model):
	course_id = models.CharField(max_length=8)
	course_code = models.ForeignKey(Courses)
	course_offered_in = models.DateField()
