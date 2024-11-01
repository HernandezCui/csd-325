def countdown_bottles(num_bottles):
    while num_bottles > 0:
        if num_bottles > 1:
            print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
            num_bottles -= 1
            print(f"Take one down and pass it around, {num_bottles} bottle(s) of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            num_bottles -= 1
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
    
print("No more bottles of beer on the wall. Time to buy more beer!")

def main():
    try:
        bottles = int(input("Enter number of bottles: "))
        if bottles < 0:
            print("Please enter a positive number.")
        else:
            countdown_bottles(bottles)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()