def calculate_loan_to_revenue(monthly_revenue,
                              requested_loan):
    if monthly_revenue <= 0:
        return None, "Monthly revenue must be greater than zero"

    if requested_loan <= 0:
        return None, "Requested loan must be greater than zero"
    
    ratio = requested_loan / monthly_revenue
    return ratio, None

def categorize_application(ratio):
    if ratio is None:
        return "Cannot assess"

    elif ratio <= 2:
        return "Lower ratio"

    elif ratio <= 4:
        return "Moderate Ratio"

    else:
        return "Higher ratio"

applications = [
    {
        "business_name": "Fitsquare LTD",
        "monthly_revenue": 5000,
        "requested_loan": 15000
    },
    {
        "business_name": "ABC Electronics",
        "monthly_revenue": 8000,
        "requested_loan": 12000
    },
    {
        "business_name": "New startup",
        "monthly_revenue": 0,
        "requested_loan": 10000
    }
]

for application in applications:
    ratio, error = calculate_loan_to_revenue(
        application["monthly_revenue"],
        application["requested_loan"]
    )

    print("\nBusiness:", application["business_name"])

    if error:
        print("ERROR:", error)
        print("Category:", categorize_application(None))
    else:
        print(f"Loan-to-monthly-revenue-ratio:, {ratio:.2f}")
        print("Category:", categorize_application(ratio))
        print("Loan is", ratio, "months of revenue")

