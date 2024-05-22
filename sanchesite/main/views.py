from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def problem(request):
    return render(request, 'main/problem.html')

def me(request):
    data = {
        'step' : ['Имя: Александр Степанников', 'Почта: aostepannikov@edu.hse.ru', 'Телефон: +79777419321'],
        'booking' : ['Имя: Букин Кирилл Александрович', 'Почта: kbukin@hse.ru'],
        'makarova' : ['Имя: Макарова Галина Викторовна', 'Почта: gmakarova@hse.ru'],
        'sardor' : ['Имя: Сабиров Сардор', 'Почта: stsabirov@edu.hse.ru', ''],
        'artem' : ['Имя: Цыгуй Артём', 'Почта: artsyguy@edu.hse.ru']
    }
    return render(request, 'main/me.html', data)