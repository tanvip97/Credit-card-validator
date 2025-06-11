# credit card validator 💳

#1. remove any '-' or ' '
#2. add all the digits in the odd places from right to left
#3. double every second digit from right to left.
#        (if result is two-digit number,
#         add the two-digit number together to get a single digit.)
#4. sum the totals of steps 2 & 3
#5. if the sum is divisible by 10, the credit card # is valid


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x) 

# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else: 
        sum_even_digits += x
        
# Step 4        
total =  sum_odd_digits + sum_even_digits          

# Step 5
if total % 10 == 0:
    print("VALID")
else: 
     print("INVALID")       
    
    
    
    

