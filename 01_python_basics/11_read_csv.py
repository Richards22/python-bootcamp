import csv

def calculate_loan_to_revenue(monthly_revenue, requested_loan):
    if monthly_revenue <=0:
        return None, "Monthly revenue must be greater than zero"

    if requested_loan <=0:
        return None, "Requested loan must be gretaer than zero"

    ratio = requested_loan / monthly_revenue
    return ratio, None

def categorize_application(ratio):
    if ratio is None:
        return "Cannot access"
    elif ratio <= 2:
        return "Lower ratio"
    elif ratio <= 4:
        return "Moderate ratio"
    else:
        return "Higher ratio"


with open("01_python_basics/11_business_applications.csv", "r",
          newline="") as file:
    reader = csv.DictReader(file)

    for application in reader:
        business_name = application["business_name"]
        monthly_revenue = float(application["monthly_revenue"])
        requested_loan = float(application["requested_loan"])

        ratio, error = calculate_loan_to_revenue(
            monthly_revenue,
            requested_loan
        )

        print("\nBusiness:", business_name)

        if error:
            print("ERROR:", error)
            print("Category:", categorize_application(None))
        else:
            print("Monthly Revenue:", monthly_revenue)
            print("Requested Loan:", requested_loan)
            print(f"Loan-to-monthly-revenue-ratio: {ratio:.2f}")
            print("Category:", categorize_application(ratio))
            print("-" * 40)