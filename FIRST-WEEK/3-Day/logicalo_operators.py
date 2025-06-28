# logical operator is and, or, not

#problem if a applicant has high income AND good credit eligible for loan
high_income = True
good_credit = False
if high_income and not good_credit:
    print("Eligiable for loan")
else:
    print("not eligible for loan")