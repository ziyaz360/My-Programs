def plan_trip(budget,countries):
    BuyableCountries = []
    
    for country, cost in countries.items():
        if cost <= budget:
            BuyableCountries.append(country)
            budget -= cost
    
    return BuyableCountries


X = 1000
countries = {"Japan": 1000, "Brazil": 300, "Australia": 500}

result = plan_trip(X, countries)
print(result)
