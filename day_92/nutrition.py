def main():
    # Get fruit input from user
    fruit = input("Item: ").lower().strip()
    
    # Look up and display calories
    calories = get_calories(fruit)
    
    if calories is not None:
        print(f"Calories: {calories}")


def get_calories(fruit):
    """
    Return the number of calories in one portion of the given fruit.
    Returns None if fruit is not in the database.
    """
    # Dictionary of fruits and their calorie values
    nutrition_data = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    
    # Return calories if fruit exists, None otherwise
    return nutrition_data.get(fruit)


if __name__ == "__main__":
    main()