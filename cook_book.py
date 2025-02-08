def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {}
    with open("C:/Users/akpp2/Desktop/OOP/File/Recept.txt", "r") as f:
        for line in f:
            res = any(char.isdigit() for char in line)
            if not res:
                key = line[0:]
            if line.strip() and '|' in line:
                values = line.split('|')
                if len(values) == 3:  
                    dish_name = key[0:-1]
                    ingredient_name = values[0]
                    quantity_measure = values[1]
                    measure = values[2]

                    if dish_name not in cook_book:
                        cook_book[dish_name] = []

                    cook_book[dish_name].append({
                        'ingredient_name': ingredient_name,
                        'quantity': quantity_measure.split()[0],
                        'measure': measure.split()[-1]
                    })

    result = {}
    for dish in dishes: 
        if dish not in cook_book: 
            continue

        for item in cook_book[dish]: 
            ingredient_name = item['ingredient_name'] 
            quantity = int(item['quantity']) * person_count
            measure = item['measure']
            if ingredient_name not in result:
                result[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                result[ingredient_name]['quantity'] += quantity
    return result

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
