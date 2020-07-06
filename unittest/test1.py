from portfolio import Portfolio
p = Portfolio()
print("Empty portfolio cost: %s, should be 0.0" %p.cost())
assert p.cost() == 0.0 # Success
p.buy('Google', 100, 176.48)
assert p.cost() == 17648.0 # Success
print("With 100 Google @ 176.48: %s, should be 17648.0" %p.cost())
p.buy('Yahoo', 100, 36.15)
assert p.cost() == 21263.0 #Success
print("With 100 Yahoo @ 36.15: %s, should be 21263.0" %p.cost())
assert p.cost() == 17648.0 # Fail
