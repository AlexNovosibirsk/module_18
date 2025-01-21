from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

users = ["Peter"]


# Create your views here.
def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if int(age) < 18:
            info["error"] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info["error"] = 'Пароли не совпадают'
        elif username in users:
            info["error"] = f'Пользователь {username} уже существует'
        else:
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, "fifth_task/registration_page.html", info)


def sign_up_by_django(request):
    form = UserRegister()
    info = {"form": form}
    if request.method == "POST":

        form = UserRegister(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if int(age) < 18:
                info["error"] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info["error"] = 'Пароли не совпадают'
            elif username in users:
                info["error"] = f'Пользователь {username} уже существует'
            else:
                return HttpResponse(f"Приветствуем, {username}!")

    return render(request, "fifth_task/registration_page.html", info)
