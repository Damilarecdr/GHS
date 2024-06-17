from django.contrib import admin

from .models import Slide, Update, HAbout, Hadmission, Whyu, Teacher, Logo

admin.site.register(Slide)
admin.site.register(Update)
admin.site.register(HAbout)
admin.site.register(Hadmission)
admin.site.register(Whyu)
admin.site.register(Logo)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 't_id', 'role', 'image',)
    search_fields = ('full_name', 'role', 't_id')
    #prepopulated_fields = {'slug': ('title',)}

