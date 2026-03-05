def determine_discount(category, membership_status):
discounts = {
        ("electronics", "premium"): 0.20,
        ("electronics", "basic"): 0.10,
        ("clothing", "premium"): 0.15,
        ("clothing", "basic"): 0.05,
    }
    return discounts.get((category, membership_status), 0.0)
