def get_shop_list_by_dishes(dishes, person_count):
    cook_book_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in cook_book_dict:
                cook_book_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
            else:
                cook_book_dict[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return cook_book_dict
cook_book = {}
with open('recepe.txt', encoding='utf-8') as file:
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        file.readline()
        cook_book[dish] = ingredients
print(cook_book)
print(get_shop_list_by_dishes(['Запеченый картофель', 'Омлет'], 2))