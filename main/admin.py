from django.contrib import admin
from .models import Review
from tinymce.widgets import TinyMCE
from django.db import models

class ReviewAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	
	fieldsets= [ 
			("Title/date", {"fields":["review_title","review_published"]}),
			("Content",{"fields":["review_content"]}),
			("Rating",{"fields":["review_rating"]}),
			("Genre",{"fields":["review_genre"]}),

	]
	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }



admin.site.register(Review,ReviewAdmin)

# Register your models here.
