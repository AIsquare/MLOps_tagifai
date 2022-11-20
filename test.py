def is_crisp(fruit):
    if fruit:
        print(fruit)
        fruit = fruit.lower()
    if fruit in ["apple", "watermelon", "cherries"]:
        return True
    elif fruit in ["orange", "mango", "strawberry"]:
        return False

    else:
        raise ValueError(f"{fruit} not in know list of fruits.")

    return False
    