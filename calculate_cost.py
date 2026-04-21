def calc_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item['price']* item['quantity']
    return total_cost    
        


##example of card data

cart = [{'name':'apple','price':100,'quantity':4},
        {'name':'banana','price':60,'quantity':12},
        {'name':'attaa','price':360,'quantity':1}]

print(calc_total_cost(cart))