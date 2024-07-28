
'''Take a user input as integer N. Find out the sum from 1 to N. 
If any number if divisible by 5, 
then skip that number. And if the sum is greater than 300, 
don't need to calculate the sum further more.
 Print the final result. And don't use for loop to solve this problem.'''


N = int(input('enter the number'))
sum = 0
i = 1

while i < N+1:
  if i % 5 == 0:
    i+=1
    continue

  sum += i

  if sum > 300:
    sum = sum - i
    break

  i+=1

print(sum)