from portfolio import Portfolio
p = Portfolio()
print("Empty portfolio cost: %s, should be 0.0" %p.cost())
p.buy('Google', 100, 176.48)
print("With 100 Google @ 176.48: %s, should be 17648.0" %p.cost())
p.buy('Yahoo', 100, 36.15)
print("With 100 Yahoo @ 36.15: %s, should be 21263.0" %p.cost())