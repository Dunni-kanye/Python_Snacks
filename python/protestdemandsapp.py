import random 

def get_random_demand(demands):
    random_index = random.randint(0, len(demands))
    return demands[random_index]

demands = [
    "Restoration of petrol subsidies and forex regime",
    "Government should address food shortage",
    "Government should address unemployment",
    "Government should address wasteful spending by those in power",
    "We don't want protest",
    "Government should enhance healthcare facilities",
    "We dey protest because say we dey hungry",
    "We dey protest because the inflation rate don affect us to di point wey we no fit afford di simple tins of life"
]

random_demand = get_random_demand(demands)

print("You are welcome to the Protest Demands App")
print("#EndBadGovernance")
print("Protest demands 2024")
print(random_demand)