# activity = input("Enter your activity: ")  

# if 'eat' in activity or 'workout' in activity or 'addiction' in activity:
#     print("Proud of you!")
# else:
#     print("Not")


import random
def roll_dice(num_dice, no_sides):
    rolls = [random.randint(1, no_sides)for _ in range(num_dice)]
    return rolls
def main():
    num_dice = int(input('enter the no: '))
    no_sides = int(input('enter sides:'))
    rolls = roll_dice(num_dice, no_sides)
    print(num_dice, no_sides)
    print (rolls)
    print(sum(rolls))
if __name__ == "__main__":
    main()