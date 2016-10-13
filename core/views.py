from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy


@login_required
def index(request):
    template = loader.get_template('core/index.html')
    context = {
        'var': 'foo',
    }
    return HttpResponse(template.render(context, request))


def login_view(request):
    data_context = {
        "error": None,
    }
    valid = False
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        next_page = request.GET.get('next', None)
        if username == '' or password == '':
            data_context["error"] = 'El Usuario y la Contraseña deben ser ingresados.'
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.POST.get('remember_me', None):
                        request.session.set_expiry(1209600)  # 2 weeks
                    if next_page:
                        return HttpResponseRedirect(next_page)
                    else:
                        return HttpResponseRedirect(reverse_lazy("index"))
                else:
                    data_context["error"] = 'El Usuario esta deshabilitado.'
            else:
                # Return an 'invalid login' error message.
                data_context["error"] = 'El Usuario o Contraseña es incorrecta.'
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("index"))
        valid = True
    data_context["valid"] = valid
    return render(request, "login.html", data_context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("login"))
