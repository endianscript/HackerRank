def max_sub_array(arr, size):
    max_so_far = arr[0]
    current_max = arr[0]

    for i in range(1, size):
        current_max = max(arr[i], current_max + arr[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far


def max_non_contiguous(arr, size):
    max_so_far = 0
    positive = False

    for i in range(0, size):
        if arr[i] > 0:
            positive = True
            max_so_far += arr[i]

    if not positive:
        for i in range(0, size):
            max_so_far = max_sub_array(arr, size)

    return max_so_far


if __name__ == '__main__':
    number_of_testcases = int(input().strip())
    for i in range(number_of_testcases):
        size = int(input().strip())
        arr = [int(i) for i in input().strip().split(" ")]
        result_sub_array = max_sub_array(arr, size)
        result_non_contiguous = max_non_contiguous(arr, size)
        result = [result_sub_array, result_non_contiguous]
        for i in result:
            print(i, end=" ")
        print()