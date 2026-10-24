# Samantha Vasquez
# CMP 131: Week 6, Lab 1
# Program 1: Software Quantity Discount

# Part 1: User Input
print(f'***Software Quantity Discount Report***')
quantity= int(input('Enter the number of software units purchased (greater than 0): '))
if quantity <= 0:
    print('ERROR')

# Part 2: Calculate the Original Cost
# original cost = number of units x $99.00
original_cost= quantity * 99
print(f' Original Cost: ${original_cost: .2f}')

# Part 3: Determine the Discount 
if quantity < 10:
    discount_rate= 0
    print('No discount')
elif quantity >= 10 and quantity <= 19:
    discount_rate= 0.2
    print(f'Discount Rate: 20%')
elif quantity >= 20 and quantity <= 49:
    discount_rate= 0.3
    print(f'Discount Rate: 30%')
elif quantity >= 50 and quantity <= 99: 
    discount_rate= 0.4
    print(f'Discount Rate: 40%')
elif quantity >= 100:
    discount_rate= 0.5
    print(f'Discount Rate: 50%')


# Part 4: Calculate the discount amount 
discount_amount= original_cost * discount_rate
print(f'Discount Amount: ${discount_amount:.2f}')

#Part 5: Caculate the Final Cost 
final_cost= original_cost - discount_amount
print(f'Final Cost: ${final_cost: .2f}')