# expanded variable names
def calculate_total_price(quantity, unit_price, discount_rate, tax_rate):

# calculate initial price
	subtotal = quantity * unit_price

# calculate discounted price
  discounted_price = subtotal * (1-discount_rate)

# calculate tax after discount
  tax_charge = discounted_price * tax_rate

# calculate final price
  total_price = discounted_price + tax_amount

	return total_pricew
