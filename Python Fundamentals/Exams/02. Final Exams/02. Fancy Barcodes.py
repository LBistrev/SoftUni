import re
number = int(input())

pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
product_group = ""
for num in range(number):
    barcodes = input()
    is_valid = [val for val in re.findall(pattern, barcodes)]
    if is_valid:
        for char in barcodes:
            if char.isdigit():
                product_group += char
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
    product_group = ""
