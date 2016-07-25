from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import loginForm
from .models import Attendance, Assosiate, Project, Sequence, ProjectLog, MainDepartment, Department, Projectstatus, Template, RawTemplateName, StatusCode, RawStatusCode, Shot, DepartmentName, Linker, Assetstatus, Asset, AssetLog, AssetCategory, Color
import time, json
from django.utils import timezone
from functools import wraps
from django.contrib.auth.decorators import login_required
from collections import OrderedDict
##from production.tables import ProjectLogTable


# Create your views here.
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        return result
    return wrapper

@debug
def main(request):
    if request.user.is_authenticated():
        return redirect('/login/')
    return render(request,'scope/index.html',{})

@debug
def logins(request):
    projs = Project.objects.all()
    seq = Sequence.objects.all()
    asse = Asset.objects.all()
    maindepts = MainDepartment.objects.all()
    tmpls = RawTemplateName.objects.all()
    atmpls = AssetCategory.objects.all()
    etmpls = RawTemplateName.objects.filter(epass=1)
    if request.user.is_authenticated():
        #return render(request, 'scope/login.html', {'projects':projs, 'seq':seq, 'maindepts':maindepts,'tmpls':tmpls,'atmpls':atmpls,'etmpls':etmpls, 'asse':asse})
        return render(request, 'scope/welcome.html', {'projects':projs, 'seq':seq, 'maindepts':maindepts,'tmpls':tmpls,'atmpls':atmpls,'etmpls':etmpls, 'asse':asse})
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            uname= authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if uname is not None:
                login(request,uname)
                userd = Assosiate.objects.get(username=form.cleaned_data['username'])
                kwargs = {'day':time.strftime('%Y-%m-%d',time.gmtime()), 'user_id' : userd.idusers, 'department_id': userd.dept_id}  ## time.mktime(datetime.date.today().timetuple())
                try:
                    Attendance.objects.get(**kwargs)
                except:
                    Attendance.objects.create(**kwargs)
                return render(request, 'scope/welcome.html', {'projects':projs, 'seq':seq, 'maindepts':maindepts,'tmpls':tmpls,'atmpls':atmpls,'etmpls':etmpls, 'asse':asse})
            else:
                return render(request,'scope/login.html',{'form':form , 'invalid':'Check username and password'})
        else:
            return render(request,'scope/login.html',{'form':form , 'invalid':'Not Logged in'})
    else:
        return render(request,'scope/login.html',{'form':loginForm})
    #return render(request,'scope/login.html',{'form':loginForm})

@debug
@login_required
def welcomes(request):
    projs = Project.objects.all()
    seq = Sequence.objects.all()
    maindepts = MainDepartment.objects.all()
    tmpls = RawTemplateName.objects.all()
    atmpls = AssetCategory.objects.all()
    etmpls = RawTemplateName.objects.filter(epass=1)
    return render(request, 'scope/welcome.html', {'projects':projs, 'seq':seq, 'maindepts':maindepts,'htmpls':tmpls,'atmpls':atmpls,'etmpls':etmpls})

@debug
@login_required
def logouts(request):
    logout(request)
    return HttpResponseRedirect('/')


@debug
@login_required
def episodes(request):
    atmpls = AssetCategory.objects.all()
    etmpls = RawTemplateName.objects.filter(epass=1)
    asse = Asset.objects.all()
    pathparts=str(request.get_full_path()).split('/')
    status = Projectstatus.objects.filter(seq_id=pathparts[3]).order_by('project','seq','shot','dept')#.annotate('created')
    shotlist = list()
    for eachshot in status:
        shotlist.append('{}-{}-{}'.format(eachshot.project, eachshot.seq, eachshot.shot))
    maindepts = MainDepartment.objects.all()
    depts = Department.objects.filter(project=pathparts[2])
    wtmpls = Template.objects.filter(template=pathparts[4])
    projs = Project.objects.all()
    seq = Sequence.objects.all()
    tmpls = RawTemplateName.objects.all()
    prsnttmplname = RawTemplateName.objects.get(idraw_template_names=pathparts[4])
    sendval = {'projects':projs, 'seq':seq, 'status':status, 'maindepts':maindepts, 'depts':depts, 'wtmpls':wtmpls, 'tmpls':tmpls, 'tplname':prsnttmplname, 'shotlist':sorted(list(set(shotlist))),'atmpls':atmpls,'etmpls':etmpls, 'asse':asse}
    return render(request, 'scope/welcome.html', sendval)


@debug
@login_required
def assets(request):
    atmpls = AssetCategory.objects.all()
    etmpls = RawTemplateName.objects.filter(epass=1)
    asse = Asset.objects.all()
    pathparts=str(request.get_full_path()).split('/')
    assstatus = Assetstatus.objects.filter(seq_id=pathparts[3],catagory_id=pathparts[4]).order_by('project','seq','assetname','dept')#.annotate('created')
    assetlist = list()
    for eachshot in assstatus:
        assetlist.append('{}-{}-{}'.format(eachshot.project, eachshot.seq, eachshot.assetname))
    maindepts = MainDepartment.objects.all()
    depts = Department.objects.filter(project=pathparts[2])
    wtmpls = Template.objects.filter(template=pathparts[4])
    projs = Project.objects.all()
    seq = Sequence.objects.all()
    tmpls = RawTemplateName.objects.all()
    prsnttmplname = AssetCategory.objects.get(idasset_category=pathparts[4])
    senddict = {'projects':projs, 'seq':seq, 'assstatus':assstatus, 'maindepts':maindepts, 'depts':depts, 'wtmpls':wtmpls, 'tmpls':tmpls, 'tplname':prsnttmplname, 'assetlist':sorted(list(set(assetlist))),'atmpls':atmpls,'etmpls':etmpls, 'asse':asse}
    return render(request, 'scope/welcome.html', senddict)



@debug
@login_required
def getlogep(request,shot_details):
    print(request)
    shot_parts = shot_details.split('_')
    if shot_parts[4] != 0:
        getlog = ProjectLog.objects.filter(project=shot_parts[0],seq=shot_parts[1],shot=shot_parts[2],dept=shot_parts[3]).order_by('-idproject_log')
    else:
        getlog = []
    return render(request,'scope/logviewer.html',{'getlog':getlog})

@debug
@login_required
def getassetlog(request,shot_details):
    shot_parts = shot_details.split('_')
    if shot_parts[4] != 0:
        getlog = AssetLog.objects.filter(project=shot_parts[0],seq=shot_parts[1],asset=shot_parts[2],dept=shot_parts[3]).order_by('-idasset_log')
    else:
        getlog = []
    return render(request,'scope/logviewer.html',{'getlog':getlog})

@debug
@login_required
def updatewin(request, shot_details):
    shot_parts = shot_details.split('_')
    if int(shot_parts[4]) == 0:
        codeval = RawStatusCode.objects.get(status_code='-').idraw_status_codes
        status = StatusCode.objects.get(department=shot_parts[3], statuscode = codeval)
    else:
        status=StatusCode.objects.get(idstatus_codes=shot_parts[4])
    codes = StatusCode.objects.filter(project=shot_parts[1],department=shot_parts[3])
    project = Project.objects.get(idprojects=shot_parts[0])
    seq = Sequence.objects.get(idsequences=shot_parts[1])
    shot = Shot.objects.get(idshots=shot_parts[2])
    dept = Department.objects.get(iddepartments=shot_parts[3])
    shotname = Projectstatus.objects.get(project=project,seq=seq,shot=shot,dept=dept,statuscode=status)
    deptname = Template.objects.filter(dept=shot_parts[3])[0]
    return render(request,'scope/update_status.html',{'codes':codes,'details':shotname,'showdeptname':deptname, 'deptname':dept})


@debug
@login_required
def updateassetwin(request, shot_details):
    shot_parts = shot_details.split('_')
    if int(shot_parts[4]) == 0:
        codeval = RawStatusCode.objects.get(status_code='-').idraw_status_codes
        status = StatusCode.objects.get(department=shot_parts[3], statuscode = codeval)
    else:
        status=StatusCode.objects.get(idstatus_codes=shot_parts[4])
    codes = StatusCode.objects.filter(project=shot_parts[1],department=shot_parts[3])
    project = Project.objects.get(idprojects=shot_parts[0])
    seq = Sequence.objects.get(idsequences=shot_parts[1])
    assetname = Asset.objects.get(idassets=shot_parts[2])
    dept = Department.objects.get(iddepartments=shot_parts[3])
    shotname = Assetstatus.objects.get(project=project,seq=seq,assetname=assetname,dept=dept,statuscode=status)
    deptname = Template.objects.filter(dept=shot_parts[3])[0]
    return render(request,'scope/update_asset_status.html',{'codes':codes,'details':shotname,'showdeptname':deptname, 'deptname':dept})


@debug
@login_required
def update(request, shot_details):
    if request.method == 'POST':
        requesteddata = json.loads(request.POST['client_response'])
    shot_parts = requesteddata['shotname'].split('-')
    associatename = Assosiate.objects.get(login=request.user)
    codes = StatusCode.objects.get(idstatus_codes=requesteddata['code'], department = Department.objects.get(department=DepartmentName.objects.get(department_name=requesteddata['dept'])))
    pshot = Projectstatus.objects.get(idprojectstatus=shot_details)
    pshot.statuscode=codes
    pshot.user = associatename
    pshot.save(update_fields=["statuscode"])
    project = Project.objects.get(project_name=shot_parts[0])
    seq = Sequence.objects.get(sequence=shot_parts[1])
    shot = Shot.objects.get(proj=project,seq=seq,shotname=shot_parts[2])
    dept = Department.objects.get(department=DepartmentName.objects.get(department_name=requesteddata['dept']), project=project.idprojects)
    logupdate = ProjectLog.objects.create(user=associatename,project=project,seq=seq,shot=shot,dept=dept,status_code=codes,notes=requesteddata['notes'],created=timezone.now())
    links = Linker.objects.filter(project=project, department=dept, code=codes)
    for eachlink in links:
        ProjectLog.objects.create(user=associatename,project=project,seq=seq,shot=shot,dept=eachlink.effect_department,status_code=eachlink.effect_code,notes=requesteddata['notes'],created=timezone.now())
        #try:
        pshot = Projectstatus.objects.get(project=project,seq=seq,shot=shot,dept=eachlink.effect_department)
        pshot.statuscode=eachlink.effect_code
        pshot.user = associatename
        pshot.save(update_fields=["statuscode"])
        #except:
        #    Projectstatus.objects.create(project=project,seq=seq,shot=shot,dept=eachlink.effect_department,statuscode=eachlink.effect_code)
    return HttpResponse(json.dumps("Updated"))


@debug
@login_required
def updateasset(request, shot_details):
    if request.method == 'POST':
        requesteddata = json.loads(request.POST['client_response'])
    shot_parts = requesteddata['shotname'].split('-')
    associatename = Assosiate.objects.get(login=request.user)
    codes = StatusCode.objects.get(idstatus_codes=requesteddata['code'], department = Department.objects.get(department=DepartmentName.objects.get(department_name=requesteddata['dept'])))
    pshot = Assetstatus.objects.get(idassetstatus=shot_details)
    pshot.statuscode=codes
    pshot.user = associatename
    pshot.save(update_fields=["statuscode"])
    project = Project.objects.get(project_name=shot_parts[0])
    seq = Sequence.objects.get(sequence=shot_parts[1])
    assetname = Asset.objects.get(assetname=shot_parts[2])
    dept = Department.objects.get(department=DepartmentName.objects.get(department_name=requesteddata['dept']), project=project.idprojects)
    logupdate = AssetLog.objects.create(user=associatename,project=project,seq=seq,asset=assetname,dept=dept,status_code=codes,notes=requesteddata['notes'],created=timezone.now())
    links = Linker.objects.filter(project=project, department=dept)
    for eachlink in links:
        AssetLog.objects.create(user=associatename,project=project,seq=seq,asset=assetname,dept=eachlink.effect_department,status_code=eachlink.effect_code,notes=requesteddata['notes'],created=timezone.now())
        #try:
        pshot = Assetstatus.objects.get(project=project,seq=seq,assetname=assetname,dept=eachlink.effect_department)
        pshot.statuscode=eachlink.effect_code
        pshot.user = associatename
        pshot.save(update_fields=["statuscode"])
        #except:
        #    Assetstatus.objects.create(user=associatename,project=project,seq=seq,assetname=assetname,dept=eachlink.effect_department,statuscode=eachlink.effect_code)
    return HttpResponse(json.dumps("Updated"))



@debug
@login_required
def add(request):
    associatename = Assosiate.objects.get(login=request.user)
    print(associatename)
    precode = RawStatusCode.objects.get(status_code='-')
    precolor = Color.objects.get(color_name = '#949494')
    for eachproj in Project.objects.all():
        for eachepi in Sequence.objects.filter(project=eachproj):
            for eachshot in Shot.objects.filter(proj=eachproj,seq=eachepi):
                for eachdept in Department.objects.all():
                    try:
                        codelink = StatusCode.objects.get(project= eachproj, department=eachdept, statuscode = precode)
                    except:
                        codelink, status = StatusCode.objects.get_or_create(project= eachproj, department=eachdept, statuscode = precode, colorcode=precolor)
                    p,status = Projectstatus.objects.get_or_create(user=associatename,project=eachproj,seq=eachepi,shot=eachshot,dept=eachdept,statuscode=codelink)


    for eachproj in Project.objects.all():
        for eachepi in Sequence.objects.filter(project=eachproj):
            for eachcategory in AssetCategory.objects.all():
                for eachasset in Asset.objects.filter(project=eachproj, seq=eachepi ,catagory=eachcategory):
                    for eachdept in Department.objects.all():
                        try:
                            codelink = StatusCode.objects.get(project= eachproj, department=eachdept, statuscode = precode)
                        except:
                            codelink, status = StatusCode.objects.get_or_create(project= eachproj, department=eachdept, statuscode = precode, colorcode=precolor)
                        p,status = Assetstatus.objects.get_or_create(user=associatename,project=eachproj,seq=eachepi,catagory=eachcategory,assetname=eachasset,dept=eachdept,statuscode=codelink)

    return HttpResponse("Updated")   ##render(request,'scope/add.html',{'projects':projects})


def attendance(request):
    assos = Assosiate.objects.get(login=request.user)
    myatten = Attendance.objects.filter(user=assos)
    sendval = {'myatten': myatten}
    return render(request, 'scope/attendance.html', sendval)
