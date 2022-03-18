def FruitCounter():
    fruits_list = ["oranges", "apples", "oranges", "apples", "oranges", "apples", "oranges", "apples", "oranges","apples"]
    y = 0
    for i in range(0, len(fruits_list)):
        if fruits_list[i] == "oranges":
            y = y + 1

    print(f"there are 5 {y}")