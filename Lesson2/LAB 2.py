prices = {'Tomato': 3, 'Cucamber': 2, 'coke': 5, 'Chicken': 20}
total = int([sum((int(input(f'how many {i}s would you like to buy? ')) * prices[i]) for i in prices.keys())][0])
print(f'your total is {total} before tax')
print(f'your total is {str("%.2f"%(total * 1.17))} taxed')
