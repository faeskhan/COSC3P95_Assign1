import random

#Insertion sort algorithm function 
#Used for sorting integers in ascending order
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

#Random test case generator function 
def random_tc_generator():
    array_length = random.randint(1, 20)  #Random array length between 1 and 20
    test_array = [random.randint(0, 100) for _ in range(array_length)] #Array of random integers between 0 and 100
    return test_array

#Function used to check if array is sorted
def sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))

if __name__ == "__main__":
    input = random_tc_generator() #Set input array as random test case generated array
    output = input.copy()  #Create a copy of input for sorting as output
    insertion_sort(output)  #Sort the output
    
    print(f"Input Array: {input}")
    print(f"Sorted Array: {output}")
    print()
