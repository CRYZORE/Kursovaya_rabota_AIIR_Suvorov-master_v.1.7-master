from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import summary.sum


class UserForm(forms.Form):
    SendMeText = forms.CharField()


def index(request):
    if request.method == 'POST':
        s = request.POST.get('SendMeText')
        origin = s
        return HttpResponse(f'<h1>Введённый текст: {origin}</h1><h1>Заменённый текст: {summary.sum.summary(s)}</h1>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
