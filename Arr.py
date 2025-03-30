arr = [10,5,95,20,30,40,50,60,70,80,90]

def biggest():
    Largest = Second_largest = float('-inf')
    for num in arr:
        if num > Largest:
            Second_largest = Largest
            Largest = num
        elif num > Second_largest and num != Largest:
            Second_largest = num

    if Second_largest == float("-inf"): 
        print("There is no second largest")
    else:
        print("Second largest number is:", Second_largest)

def smallest():
    Smallest = Second_smallest = float('inf')
    for num in arr:
        if num < Smallest:
            Second_smallest = Smallest
            Smallest = num
        elif num < Second_smallest and num != Smallest:
            Second_smallest = num

    if Second_smallest == float("inf"): 
        print("There is no second smallest")
    else:
        print("Second smallest number is:", Second_smallest)

biggest()
smallest()

