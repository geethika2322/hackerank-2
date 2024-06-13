def check_subset(test_cases):
    results = []
    for _ in range(test_cases):
        # Read the number of elements in set A
        num_elements_a = int(input())
        # Read the elements of set A
        set_a = set(map(int, input().split()))
        
        # Read the number of elements in set B
        num_elements_b = int(input())
        # Read the elements of set B
        set_b = set(map(int, input().split()))
        
        # Check if set A is a subset of set B
        if set_a.issubset(set_b):
            results.append("True")
        else:
            results.append("False")
    
    # Print all results, each on a new line
    for result in results:
        print(result)

# Read the number of test cases
T = int(input())

# Process each test case
check_subset(T)
