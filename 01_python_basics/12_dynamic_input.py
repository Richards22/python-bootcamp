def calculate_loan_ratio(monthly_revenue, requested_loan):
    if monthly_revenue <=0:
        raise ValueError("Monthly revenue must be greater than zero.")

    if requested_loan <=0:
        raise ValueError("Requested loan amount must be greater than zero.")

    return requested_loan / monthly_revenue

business_name = input("Enter the business name: ")

try:
    monthly_revenue = float(input("Enter the monthly revenue: "))
    requested_loan = float(input("Enter the requested loan amount: "))

    ratio = calculate_loan_ratio(
        monthly_revenue, 
        requested_loan
        )

        
    print("\nBusiness: ", business_name)
    print(f"Monthly Revenue:  {monthly_revenue:.2f}")
    print(f"Requested Loan:  {requested_loan:.2f}")
    print(f"Loan-to-Revenue Ratio:  {ratio:.2f}")

except ValueError as error:
    print("ERROR:", error)
