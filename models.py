# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Asset(models.Model):
    idassets = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    seq = models.ForeignKey('Sequence', models.DO_NOTHING)
    catagory = models.ForeignKey('AssetCategory', models.DO_NOTHING)
    assetname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'asset'


class AssetCategory(models.Model):
    idasset_category = models.AutoField(db_column='idAsset_Category', primary_key=True)  # Field name made lowercase.
    catagory_name = models.CharField(db_column='Catagory_Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_category'


class AssetLog(models.Model):
    idasset_log = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    seq = models.ForeignKey('Sequence', models.DO_NOTHING)
    asset = models.ForeignKey(Asset, models.DO_NOTHING)
    main_dept = models.ForeignKey('MainDepartment', models.DO_NOTHING)
    status_code = models.ForeignKey('RawStatusCode', models.DO_NOTHING)
    notes = models.TextField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'asset_log'


class Assetstatus(models.Model):
    idassetstatus = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    seq = models.ForeignKey('Sequence', models.DO_NOTHING)
    assetname = models.ForeignKey(Asset, models.DO_NOTHING)
    dept = models.ForeignKey('Department', models.DO_NOTHING)
    statuscode = models.ForeignKey('StatusCode', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assetstatus'


class Assosiate(models.Model):
    idusers = models.AutoField(primary_key=True)
    login_id = models.IntegerField()
    username = models.CharField(max_length=45)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    lead_id = models.IntegerField()
    dept = models.ForeignKey('MainDepartment', models.DO_NOTHING)
    designaton = models.ForeignKey('Designation', models.DO_NOTHING)
    blood_group = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    authorised = models.IntegerField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assosiate'


class Attendance(models.Model):
    idattendance = models.AutoField(primary_key=True)
    user = models.ForeignKey(Assosiate, models.DO_NOTHING)
    department = models.ForeignKey('DepartmentName', models.DO_NOTHING)
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'attendance'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Color(models.Model):
    idcolors = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'color'


class Department(models.Model):
    iddepartments = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    department = models.ForeignKey('DepartmentName', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentName(models.Model):
    iddepartment_names = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'department_name'


class Designation(models.Model):
    iddesignations = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'designation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Linker(models.Model):
    idlinkers = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    code = models.ForeignKey('StatusCode', models.DO_NOTHING)
    effect_department = models.ForeignKey(Department, models.DO_NOTHING)
    effect_code = models.ForeignKey('StatusCode', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'linker'


class MainDepartment(models.Model):
    idmain_department = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'main_department'


class Project(models.Model):
    idprojects = models.AutoField(primary_key=True)
    project_name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectLog(models.Model):
    idproject_log = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    seq = models.ForeignKey('Sequence', models.DO_NOTHING)
    shot = models.ForeignKey('Shot', models.DO_NOTHING)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    status_code = models.ForeignKey('StatusCode', models.DO_NOTHING)
    notes = models.TextField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_log'


class Projectstatus(models.Model):
    idprojectstatus = models.AutoField(db_column='idprojectStatus', primary_key=True)  # Field name made lowercase.
    project = models.ForeignKey(Project, models.DO_NOTHING)
    seq = models.ForeignKey('Sequence', models.DO_NOTHING)
    shot = models.ForeignKey('Shot', models.DO_NOTHING)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    statuscode = models.ForeignKey('StatusCode', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projectstatus'


class RawStatusCode(models.Model):
    idraw_status_codes = models.AutoField(primary_key=True)
    status_code = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'raw_status_code'


class RawTemplateName(models.Model):
    idraw_template_names = models.AutoField(primary_key=True)
    template_name = models.CharField(max_length=45)
    epass = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raw_template_name'


class Sequence(models.Model):
    idsequences = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    sequence = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'sequence'


class Shot(models.Model):
    idshots = models.AutoField(primary_key=True)
    proj = models.ForeignKey(Project, models.DO_NOTHING)
    seq = models.ForeignKey(Sequence, models.DO_NOTHING)
    shotname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'shot'


class ShowCode(models.Model):
    idshow_codes = models.AutoField(primary_key=True)
    show_codescol = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'show_code'


class StatusCode(models.Model):
    idstatus_codes = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    statuscode = models.ForeignKey(RawStatusCode, models.DO_NOTHING)
    colorcode = models.ForeignKey(Color, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'status_code'


class Template(models.Model):
    idtemplates = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    template = models.ForeignKey(RawTemplateName, models.DO_NOTHING)
    show_code = models.ForeignKey(ShowCode, models.DO_NOTHING)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    size = models.IntegerField()
    editable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'template'
