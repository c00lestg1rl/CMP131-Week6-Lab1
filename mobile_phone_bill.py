# Samantha Vasquez 
# CMP 131: Week 6, Lab 2
# Program 2: Mobile Phone Service Bill

print('***Mobile Phone Service Billing Program***')

# Part 1: Display the Packages 
print('Below are the three available packages. ')
print(f"~Package A~\nMonthly Charge: $39.99\nIncluded Minutes: 450\nAdditional Minutes: $0.45 per minute")
print(f"~Package B~\nMonthly Charge: $59.99\nIncluded Minutes: 900\nAdditional Minutes: $0.40 per minute")
print(f"~Package C~\nMonthly Charge: $69.99\nIncluded Minutes: unlimited\nNo additional minute charge")

# Part 2: User Input 
selection= str(input('Enter your selected package: '))
minutes_used= int(input('Enter the number of minutes you used during the month: '))

print(f'The package you selected is: {selection}')
print(f'The number of minutes you used is: {minutes_used}')
if selection== 'A' :
    monthly_charge= 39.99
    additional= 0.45
    included_minutes = 450
    if minutes_used > 450:
         additional_minutes= minutes_used - included_minutes
         additional_charge= additional_minutes * additional
         total_bill= monthly_charge + additional_charge
    elif minutes_used <= 450:
         total_bill= monthly_charge
         additional_minutes= 0
         additional_charge= 0
    print(f'Monthly Package Charge: ${monthly_charge}')
    print(f'Number of Additional Minutes: {additional_minutes}')
    print(f'Additional Minute Charge: ${additional_charge:.2f}')
    print(f'Total Amount Due: ${total_bill:.2f}')
elif selection== 'B' :
    monthly_charge= 59.99
    included_minutes= 900
    additional= 0.40
    if minutes_used > 900:
             additional_minutes= minutes_used - included_minutes
             additional_charge= additional_minutes * additional
             total_bill= monthly_charge + additional_charge
    elif minutes_used <= 900:
             total_bill= monthly_charge
             additional_minutes= 0
             additional_charge= 0
    print(f'Monthly Package Charge: ${monthly_charge: }')
    print(f'Number of Additional Minutes: {additional_minutes}')
    print(f'Additional Minute Charge: ${additional_charge:.2f}')
    print(f'Total Amount Due: ${total_bill:.2f}')
elif selection== 'C' :
    monthly_charge= 69.99
    total_bill= monthly_charge
    print(f'Monthly Package Charge: ${monthly_charge}')
    print('This package includes unlimited minutes.')
    print(f'Total Amount Due: ${total_bill:.2f}')
elif selection != 'A' or 'B' or 'C':
    print('INVALID PACKAGE')
    selection= str(input('Enter your correctly selected package: '))
