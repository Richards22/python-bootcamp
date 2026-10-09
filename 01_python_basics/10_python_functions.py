def calculate_loan_to_revenue(monthly_revenue,
                              requested_loan):
    if monthly_revenue <= 0:
        return None, "Monthly revenue must be greater than zero"

    if requested_loan <= 0:
        return None, "Requested loan must be greater than zero"
    
    ratio = requested_loan / monthly_revenue
    return ratio, None


monthly_revenue = 0
requested_loan = 1000

ratio, error = calculate_loan_to_revenue(monthly_revenue,
                                  requested_loan)

if error:
    print("ERROR:", error)
else:
    print("Loan-to-monthly-revenue-ratio:", ratio)
    print("Loan is", ratio, "months of revenue")