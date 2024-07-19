from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def menu_view(request, name_dish):

    if name_dish in DATA:
        data = DATA[name_dish]
        servings = request.GET.get('servings', None)

        if servings:
            quantity = dict()
            for item, value in data.items():
                new_value = value * int(servings)
                quantity[item] = new_value
            context = {
                'name_dish': name_dish,
                'recipe': quantity
            }
        else:
            context = {
                'name_dish': name_dish,
                'recipe': data
            }

    else:
        context = None

    return render(request, template_name='calculator.html', context=context)




