from django.contrib import admin

# Register your models here.
from .models import Attendance,Color,DepartmentName,Department,Designation,Linker,ProjectLog,Project,RawStatusCode,RawTemplateName,Sequence,Shot,ShowCode,StatusCode,Template,Assosiate,Asset,AssetLog,MainDepartment,Projectstatus,Assetstatus,AssetCategory
from .forms import ProjectstatusForm, ShotForm


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['project','template','show_code','dept', 'editable']
    list_filter = (
        ('project', admin.RelatedOnlyFieldListFilter),
        ('template', admin.RelatedOnlyFieldListFilter),
        ('show_code', admin.RelatedOnlyFieldListFilter),
        ('dept', admin.RelatedOnlyFieldListFilter),
    )
    
class userAdmin(admin.ModelAdmin):
    list_display = ['username','designaton']
    search_fields = ['username']

class ProjectstatusAdmin(admin.ModelAdmin):
    list_display = ['project','seq','shot','dept','statuscode']
    fieldsets = [
        ('Status Add', {'fields': ['project','seq','shot','dept','statuscode']}),
    ]
    list_filter = (
        ('project', admin.RelatedOnlyFieldListFilter),
        ('seq', admin.RelatedOnlyFieldListFilter),
        ('shot', admin.RelatedOnlyFieldListFilter),
        ('dept', admin.RelatedOnlyFieldListFilter),
        ('statuscode', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['project__project_name','seq__sequence','shot__shotname','dept__department__department_name','statuscode__statuscode__status_code']
    select_related=('dept', 'statuscode')
    form_class = ProjectstatusForm
    filter = ('statuscode',)
    list_select_related = ('dept', 'statuscode')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['user','department','day']

class AssetAdmin(admin.ModelAdmin):
    list_display = ['project','seq','assetname']

class StatusCodeAdmin(admin.ModelAdmin):
    list_display = ['project','department','statuscode','colorcode']
    list_filter = (
        ('project', admin.RelatedOnlyFieldListFilter),
        ('department', admin.RelatedOnlyFieldListFilter),
        ('statuscode', admin.RelatedOnlyFieldListFilter),
    )


class ShotAdmin(admin.ModelAdmin):
    list_display = ['seq','shotname']
    form_class = ShotForm

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['project','department']


class LinkerAdmin(admin.ModelAdmin):
    list_display = ['project','department','code','effect_department','effect_code']

class ProjectLogAdmin(admin.ModelAdmin):
    list_display = ['project','seq','shot','dept','status_code','notes','created']


class SequenceAdmin(admin.ModelAdmin):
    list_display = ['project','sequence']

class AssetLogAdmin(admin.ModelAdmin):
    list_display = ['project','seq','asset','dept','status_code','notes','created']

class AssetAdmin(admin.ModelAdmin):
    list_display = ['project','seq','assetname']

class AssetstatusAdmin(admin.ModelAdmin):
    list_display = ['project','seq','assetname','dept','statuscode']

admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Color)
admin.site.register(DepartmentName)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Designation)
admin.site.register(Linker, LinkerAdmin)
admin.site.register(ProjectLog, ProjectLogAdmin)
admin.site.register(Project)
admin.site.register(RawStatusCode)
admin.site.register(RawTemplateName)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Shot, ShotAdmin)
admin.site.register(ShowCode)
admin.site.register(StatusCode, StatusCodeAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Assosiate, userAdmin)
admin.site.register(AssetLog, AssetLogAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(MainDepartment)
admin.site.register(Projectstatus,ProjectstatusAdmin)
admin.site.register(Assetstatus, AssetstatusAdmin)
admin.site.register(AssetCategory)
