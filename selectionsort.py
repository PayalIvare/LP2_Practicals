# Function to perform selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Make the array dynamic based on user input
def dynamic_selection_sort():
    # Get input from the user
    try:
        n = int(input("Enter the number of elements in the array: "))  # Get array size
        arr = []
        print(f"Enter {n} elements:")
        
        # Get each element from the user
        for i in range(n):
            element = int(input(f"Element {i+1}: "))
            arr.append(element)

        # Sort the array using selection sort
        sorted_arr = selection_sort(arr)
        print("Sorted array:", sorted_arr)
    except ValueError:
        print("Invalid input. Please enter integers.")

# Call the dynamic selection sort function
dynamic_selection_sort()

