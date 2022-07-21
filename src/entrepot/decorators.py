from django.http import HttpResponse


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrap_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("you are not authorized to view this page")
        return wrap_func
    return decorators
            