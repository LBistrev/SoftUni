command = input()

company_dict = {}
while not command == "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_dict:
        company_dict[company_name] = []
    if employee_id not in company_dict[company_name]:
        company_dict[company_name].append(employee_id)

    command = input()

sorted_companies = sorted(company_dict.items(), key=lambda kvp: kvp[0])
for name, emp_id in sorted_companies:
    print(f"{name}")
    for emp in emp_id:
        print(f"-- {''.join(emp)}")
