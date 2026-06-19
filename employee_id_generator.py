# Smart Employee ID Generator
# Developed by Harsha Rohira

print("=" * 50)
print("      SMART EMPLOYEE ID GENERATOR")
print("=" * 50)

while True:
    # Employee Details Input
    name = input("\nEnter Employee Name: ").strip()
    department = input("Enter Department (IT/HR/SALES/MARKETING/FINANCE): ").strip().upper()
    year = input("Enter Joining Year: ").strip()

    # Validate Name
    if name == "":
        print("Employee name cannot be empty!")
        continue

    # Validate Department
    valid_departments = ["IT", "HR", "SALES", "MARKETING", "FINANCE"]

    if department not in valid_departments:
        print("Invalid Department!")
        print("Allowed Departments: IT, HR, SALES, MARKETING, FINANCE")
        continue

    # Validate Joining Year
    if not year.isdigit() or len(year) != 4:
        print("Invalid Joining Year! Please enter a 4-digit year.")
        continue

    # Generate Employee ID
    name_part = name.upper().replace(" ", "")[:3]

    if len(name_part) < 3:
        name_part = name_part.ljust(3, "X")

    dept_part = department[:2]

    employee_id = name_part + dept_part + year

    # Display Employee Details
    print("\n" + "=" * 50)
    print("           EMPLOYEE DETAILS")
    print("=" * 50)
    print(f"Employee ID   : {employee_id}")
    print(f"Employee Name : {name.title()}")
    print(f"Department    : {department}")
    print(f"Joining Year  : {year}")
    print("=" * 50)

    # Ask User to Continue
    choice = input("\nDo you want to add another employee? (yes/no): ").strip().lower()

    if choice != "yes":
        print("\nThank you for using Smart Employee ID Generator!")
        break