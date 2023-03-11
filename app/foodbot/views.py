from django.shortcuts import render
from django.conf import settings

import openai

openai.api_key = settings.OPENAI_API_KEY

def index(request):
    result = ''
    if request.method == "POST":
        food = request.POST.get('dish')
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(food),
            temperature=0.6,
        )
        result = response.choices[0].text

    return render(request, 'foodbot/index.html', {'result': result})

def generate_prompt(food):
    return """Suggest three dishes to eat.

Food: Western
Dishes: Spaghetti Carbonara, Pepperoni Pizza, Buffalo Chicken Wings
Food
Dishes: Nasi Lemak, Rendang, Char Kuey Teow
Food: {}
Dishes:""".format(
        food.capitalize()
    )