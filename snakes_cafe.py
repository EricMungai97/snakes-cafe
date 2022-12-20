
def greeting():
    print("$ python snakes_cafe.py")
    print("*"*38)
    print("**  Welcome to Snakes Cafe! **")
    print("**  Please see our menu below.  **")
    print("**")
    print("** To quit at any time, type 'quit' **")
    print("*"*38)
greeting()

def empty_line():
    print()


def menu():
    app_names = {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0}
    menu_choices(app_names, "Appetizers")

    entree_names = {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal '
        'Garden': 0}
    menu_choices(entree_names, "Entrees")

    dessert_names = {'Ice Cream': 0, 'Cake': 0, 'Pie': 0}
    menu_choices(dessert_names, "Desserts")

    drink_names = {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
    menu_choices(drink_names, "Drinks")

    def make_order():
        print()
        print("*"*35)
        print("** What would you like to order? **")
        print("*"*35)

    make_order()

    status = True

    while status:
        order_food = input("> ")
        if order_food in app_names:
            order_response(app_names, order_food)
        elif order_food in entree_names:
            order_response(entree_names, order_food)
        elif order_food in dessert_names:
            order_response(dessert_names, order_food)
        elif order_food in drink_names:
            order_response(drink_names, order_food)
        elif order_food == 'quit':
            exit()
        else:
            print()
            print("That item does not exist.")
            print()


def order_response(food_category, order_food):
    food_category[order_food] += 1
    if food_category.get(order_food) == 1:
        print()
        print("** " + str(food_category.get(order_food)) + " order of " +
              order_food + " have been added to your meal **")
        print()
    elif food_category.get(order_food) > 1:
        print()
        print("** " + str(food_category.get(order_food)) + " orders of "
              + order_food + " have been added to your meal **")
        print()


def menu_choices(menu_category, category_header):
    print()
    print(category_header)
    print("-"*len(category_header))
    for key in menu_category.keys():
        print(key)


empty_line()

greeting()
menu()
