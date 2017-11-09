from django.contrib import admin
from .models import Colleges
from .models import Programs
from .models import Spec_Major
from .models import Courses
from .models import Course_Offering



admin.site.register(Colleges)
admin.site.register(Programs)
admin.site.register(Spec_Major)
admin.site.register(Courses)
admin.site.register(Course_Offering)

# Register your models here.
