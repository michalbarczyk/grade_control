from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from system.models import Grade, Student, Teacher


@login_required
def manage_groups(request):
    user = request.user
    student_exists = Student.objects.filter(user=user.id).exists()
    teacher_exists = Teacher.objects.filter(user=user.id).exists()
    groups = []
    if student_exists:
        grades = Grade.objects.filter(owner_id=user.id)
        groups.append('Student')
    else:
        grades = None
    if teacher_exists:
        groups.append('Teacher')

    student_str = ''
    teacher_str = ''
    if len(groups) > 1:
        student_str = ' (I learn)'
        teacher_str = ' (I teach)'
    context = {
        'sidebar': True,
        'groups': groups,
        'grades': grades,
        'student_str': student_str,
        'teacher_str': teacher_str,
        'title': 'Manage your groups'
    }
    return render(request, 'system/manage_groups.html', context)
