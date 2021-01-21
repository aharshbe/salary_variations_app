print('This tool presents a NEAR offer given the current token price and a intial salary\n\n')

initial_salary = float(input('What is the base salary? (ex: 118000.00) '))
# print(f'Inital salary is {initial_salary}\n\n')

current_token_price = float(input('What is the current token price? (ex: 2.00) '))
# print(f'Current token price is {current_token_price}\n\n')

token_percentage = int(input(f'What is the token % in relation to {initial_salary}? (ex: 25) '))
# print(f'Token % is {token_percentage}\n\n')

def calculate_token_allocation(initial_salary, token_percentage, current_token_price):
  token_percentage = token_percentage/100
  token_allocation = initial_salary/current_token_price*(token_percentage)*4
  return (token_allocation)


token_allocation = calculate_token_allocation(initial_salary, token_percentage, current_token_price)

arr_variations = [[initial_salary,token_allocation, token_allocation*current_token_price]]

# Generate offer variations
def calculate_offer_variations(arr_variations, current_token_price):

  for i in range(1,3):
    salary=arr_variations[0][0]-i*10000
    token_allocation=(i*10000/current_token_price*4)+arr_variations[0][1]
    token_value=token_allocation*current_token_price

    # Add to array of offer variations
    arr_variations.append(["${:,.2f}".format(salary),"{:,.2f} NEAR tokens".format(token_allocation),"${:,.2f}".format(token_value)])

  # Convert first values to formatted version
  arr_variations[0][0] = "${:,.2f}".format(arr_variations[0][0])
  arr_variations[0][1] = "{:,.2f} NEAR tokens".format(arr_variations[0][1])
  arr_variations[0][2] = "${:,.2f}".format(arr_variations[0][2])

  return (arr_variations)

# Print offer variations
def print_offer(arr_variations):
  print("\n\nOffer breakdown with 3 variations:\n")
  for i,offer in enumerate(arr_variations):
    print(f'{i+1}. {offer[0]} with {offer[1]} valued at {offer[2]} USD (standard 1-year cliff, 4-year vesting schedule)\n')

print_offer(calculate_offer_variations(arr_variations,current_token_price))
