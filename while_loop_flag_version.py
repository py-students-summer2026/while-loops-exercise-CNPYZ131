def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall?"))
            if num >= 1:
                return num
        except ValueError:
            pass

def bottle_text(num):
    if num == 1:
        return "1 bottle"
    return f"{num} bottles"

def sing(starting_bottles):
    bottles = starting_bottles
    keep_singing = True

    while keep_singing:
        print(f"{bottle_text(bottles)} of beer on the wall, {bottle_text(bottles)} of beer.")

        if bottles == 1:
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_singing = False
        else:
            print(f"Take one down, pass it around, {bottle_text(bottles - 1)} of beer on the wall.")
            print()
            bottles -= 1

