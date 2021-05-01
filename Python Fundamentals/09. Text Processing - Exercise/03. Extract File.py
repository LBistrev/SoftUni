file = input().split("\\")
files = {}
needed_data = file[-1].split(".")

print(f"File name: {needed_data[0]}")
print(f"File extension: {needed_data[1]}")
