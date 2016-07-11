__author__ = 'venut'

from django import template
register = template.Library()

@register.filter
def compare(shotname, shotstatus):
    parts = shotname.split('-')
    if str(parts[0]) == str(shotstatus.project) and str(parts[1]) == str(shotstatus.seq) and str(parts[2]) == str(shotstatus.shot):
        return True
    else:
        return False


@register.filter()
def comparedept(shotname, shotdept):
    pass


@register.filter()
def compareshot(shotname, shotdept):
    pass


@register.filter()
def final(shots, args):
    dept, shot = args.split('_')
    project, seq, shot = shot.split('-')
    status = True
    for eachshot in shots:
        if eachshot.project == project and eachshot.seq == seq and eachshot.shot == shot and eachshot.dept == dept:
            status = True
        else:
            status = False
    return status

@register.filter()
def checkshot(shots, args):
    return shots,args


class status:
    idprojects = 0
    idsequences = 0
    idshots = 0
    iddepartments = 0
    idstatus_codes = 0

@register.filter()
def checkdept(shots,dept):
    shots, shotname = shots
    project, seq, shot = shotname.split('-')
    stat = status()
    for eachshot in shots:
        if (eachshot.project.project_name==project and eachshot.seq.sequence == seq and eachshot.shot.shotname==shot):
            stat.idprojects = eachshot.project.idprojects
            stat.idsequences = eachshot.seq.idsequences
            stat.idshots = eachshot.shot.idshots

        if eachshot.dept.department.department_name == dept.department.department_name:
            stat.iddepartments = eachshot.dept.iddepartments

    for eachshot in shots:
        if (eachshot.project.project_name==project and eachshot.seq.sequence == seq and eachshot.shot.shotname==shot and eachshot.dept.department.department_name == dept.department.department_name):
            return eachshot

    return stat



class status1:
    idprojects = 0
    idsequences = 0
    idassets = 0
    iddepartments = 0
    idstatus_codes = 0

@register.filter()
def checkdept2(shots,dept):
    shots, shotname = shots
    project, seq, assetname = shotname.split('-')
    stat = status1()
    for eachshot in shots:
        if (eachshot.project.project_name==project and eachshot.seq.sequence == seq and eachshot.assetname.assetname==assetname):
            stat.idprojects = eachshot.project.idprojects
            stat.idsequences = eachshot.seq.idsequences
            stat.idassets = eachshot.assetname.idassets

        if eachshot.dept.department.department_name == dept.department.department_name:
            stat.iddepartments = eachshot.dept.iddepartments

    for eachshot in shots:
        if (eachshot.project.project_name==project and eachshot.seq.sequence == seq and eachshot.assetname.assetname==assetname and eachshot.dept.department.department_name == dept.department.department_name):
            return eachshot

    return stat