def students_with_both_subscriptions(english, french):
    # Convert the lists to sets
    english_set = set(english)
    french_set = set(french)
    
    # Find the intersection of the two sets
    both_subscriptions = english_set.intersection(french_set)
    
    # Return the count of students with both subscriptions
    return len(both_subscriptions)

# Read input
n = int(input())
english = list(map(int, input().split()))
b = int(input())
french = list(map(int, input().split()))

# Print the result
print(students_with_both_subscriptions(english, french))
