from django.shortcuts import render
from .models import UserName

# Create your views here.

def index(request):
    greeting = None
    error = None

    if request.method == 'POST':
        # Получаем имя из формы и удаляем лишние пробелы по краям
        name_input = request.POST.get('username', '').strip()
        
        if name_input:
            # Сохраняем имя в базу данных
            UserName.objects.create(name=name_input)
            greeting = f"Привет, {name_input}!"
        else:
            # Обработка ошибки, если поле пустое
            error = "Поле не может быть пустым. Пожалуйста, введите имя."

    # Передаем данные в HTML-шаблон (список all_users больше не передаем)
    context = {
        'greeting': greeting,
        'error': error,
    }
    return render(request, 'index.html', context)
