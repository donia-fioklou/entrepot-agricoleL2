from django.shortcuts import render


def admin(request):
    return render(request,template_name="admin/base.html")