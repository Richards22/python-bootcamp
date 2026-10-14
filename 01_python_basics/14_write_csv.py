import csv



applications = [
    ["ABC Electronics", 5000, 15000, 3.00, "Moderate Ratio"],
    ["Bright Foods", 8000, 12000, 1.50, "Lower Ratio"],
    ["New Startup", 0, 10000, None, "Needs Review"],
    ["Green Farms", 12000, 24000, 2.00, "Lower Ratio"]
]

with open(
    "01_python_basics/14_screening_results.csv", 
    "w",
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

    writer.writerows(applications)

print("All applications written to CSV.")