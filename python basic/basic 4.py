# Get the test scores from users
# Get the average score and print value to users

# Author Kangdong Yuan

# 1. Get the scores from users
test_score = int(input("Enter a test score, -1 to get the average: "))

# 2.Set the total socre, member, and average score
total_score = 0
member = 0
average_scores = 0

# 3. Plus all the scores and divided by member number
while test_score >= 0:
    total_score = total_score + test_score
    member = member + 1
    test_score = int(input("Enter a test score, -1 to get the average: "))
else:
    average_scores = total_score//member

# Print value to users
print("The average for all average is "+str(average_scores))
