'''
This tool generates various offer variations
Created by Austin Harshberger
1/22/21
Free and Open Source
'''

print('This tool presents a NEAR offer given the current token price and a intial salary\n\n')

# Obtain initial salary
initial_salary = float(input('What is the base salary? (ex: 118000.00) '))
# print(f'Inital salary is {initial_salary}\n\n')

# Obtain percentage of salary (token to salary ratio) in order to generate token grant
token_percentage = int(input(f'What is the token % in relation to {initial_salary}? (ex: 25) '))
# print(f'Token % is {token_percentage}\n\n')

# How many offer variations to generate? The standard is 2 offers. Some teams like 3.
num_variations = int(input(f'How many variations would you like? (ex: 2) '))
# print(f'Token % is {token_percentage}\n\n')

# Prettyfies
print()

# Calculate the token allocation, i.e., the token grant based on the token to salary ratio enetered
def calculate_token_allocation(initial_salary, token_percentage):
  token_percentage = token_percentage/100
  # print(f'Token percentage is currently {token_percentage}')
  token_allocation = initial_salary*token_percentage*4
  # print(f'Token allocation is now {token_allocation}')
  return (token_allocation)

# Store NEAR grant
token_allocation = calculate_token_allocation(initial_salary, token_percentage)

# Create an array of variations
arr_variations = [[initial_salary,token_allocation]]


# Calculate token allocations then return them as a matrix in arr_variations
def calculate_offer_variations(initial_salary,arr_variations, num_variations, token_percentage):
    for i in range(1,num_variations):
        variation_control = i*10000
        new_salary = initial_salary-variation_control
        # Important to note at higher token to salary ratios i.e., > 50% incrementing by 5% is no longer advantageous for a candidate so it's necessary to increment by 10% between variations instead
        if token_percentage > 50:
            new_token_percentage = token_percentage+i*10
        else:
            new_token_percentage = token_percentage+i*5
        if i > 1:
            if arr_variations[i-1][2] > 50:
                new_token_percentage = arr_variations[i-1][2]+10
            else:
                new_token_percentage = token_percentage+i*5
        arr_variations.append(["${:,.2f}".format(new_salary),"${:,.2f} in $N --> tokens at {}%".format(calculate_token_allocation(new_salary,new_token_percentage), new_token_percentage), new_token_percentage])
    arr_variations[0][0] = "${:,.2f}".format(arr_variations[0][0])
    arr_variations[0][1] = "${:,.2f} in $N --> tokens at {}%".format(arr_variations[0][1], token_percentage)
    return arr_variations

# Store newly created variations in array or arrays i.e., matrix
arr_variations = calculate_offer_variations(initial_salary,arr_variations,num_variations,token_percentage)

# print(arr_variations)

# Function to print out formatted offer variations
def print_offer(arr_variations):
  print(f"\n\nOffer breakdown with {len(arr_variations)} variations:\n")
  for i,offer in enumerate(arr_variations):
    print(f'{offer[0]} with {offer[1]} (standard 1-year cliff, 4-year vesting schedule)')
  print("\n")

# Print offer variations
print_offer(arr_variations)

# EOF
