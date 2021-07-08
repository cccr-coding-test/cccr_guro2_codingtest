fix_fee, product_fee, price = map(int, input().split())

if product_fee >= price:
    print(-1)
else:
    day = fix_fee/(price-product_fee)
    print(int(day)+1)
