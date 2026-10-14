import csv

def calculate_loan_ratio(monthly_revenue, requested_loan):
    if monthly_revenue <= 0:
        raise ValueError("Monthly revenue must be greater than zero.")

    if requested_loan <= 0:
        raise ValueError("Requested loan amount must be greater than zero.")

    return requested_loan / monthly_revenue

def categorize_application(ratio):
    if ratio is None:
        return "Needs Review"
    elif ratio <= 2:
        return "Lower Ratio"
    elif ratio <= 4:
        return "Moderate Ratio"
    else:
        return "High Ratio"

results = []

with open("01_python_basics/11_business_applications.csv", "r") as file:
    reader = csv.DictReader(file)

    for application in reader:
        business_name = application["business_name"]
        revenue_value = application["monthly_revenue"]
        loan_value = application["requested_loan"]

        try:

            monthly_revenue = float(revenue_value)
            requested_loan = float(loan_value)
            
            ratio = calculate_loan_ratio(
                monthly_revenue,
                requested_loan
            )

            category = categorize_application(ratio)

            results.append([
                business_name,
                monthly_revenue,
                requested_loan,
                round(ratio, 2),
                category
            ])

            print("Business: ", business_name)
            print(f"Loan-to-revenue ratio: {ratio:.2f}")
            print("Screening Category:", category)

        except ValueError as error:
            print("Business: ", business_name)
            print("Error: Revenue or loan amount missing or invalid.")

            results.append([
                business_name,
                revenue_value,
                loan_value,
                None,
                "Needs Review"
            ])

        
        print("-" * 30)

with open(
    "01_python_basics/14_screening_results.csv", "w",
    newline=""
) as file:
    writer = csv.writer(file)

    writer.writerow([
        "business_name",
        "monthly_revenue",
        "requested_loan",
        "ratio",
        "screening_category"
    ])

    writer.writerows(results)
print("\nScreening reports created successfully")











