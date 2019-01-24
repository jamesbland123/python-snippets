from parse import parse

LOG = '[2018-12-28T12:14:00.733823] - SALE - PRODUCT: 1234 - PRICE: $29.95'
FORMAT = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: {price}'

result = parse(FORMAT, LOG)
print(result)
