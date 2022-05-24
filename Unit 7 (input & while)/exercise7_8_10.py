sandwich_orders = ['tuna', 'beef', 'tomanto', 'chis']
finished_sandwiches = []

while sandwich_orders:
    name = sandwich_orders.pop()
    print(f'I made your {name} sandwich')
    finished_sandwiches.append(name)

while finished_sandwiches:
    print(finished_sandwiches.pop())