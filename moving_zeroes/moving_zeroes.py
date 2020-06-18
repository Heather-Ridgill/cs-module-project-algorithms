'''
Input: a List of integers
Returns: a List of integers
'''

#Time complexity: 0(n)

def moving_zeroes(arr):
    # Create a pointer for the search and end position
    i = 0
    end = len(arr) - 1
    # Iterate through the list, while the search position has not reached the end postion
    while i < end:
        # If the value is 0, append value, del postion, dec end
        if arr[i] == 0:
            arr.append(arr[i])
            del arr[i]
            end -= 1
        # Inc search postion
        else:
            i += 1
    # Return adjusted list
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")