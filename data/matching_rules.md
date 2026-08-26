# Matching Rules

PRIMARY RULES
1. Customer_ID must match.
2. Grand_Total should match Transaction_Amount. Any discrepancy must be reported as an exception unless explained by predefined business rules (e.g., fees, discounts, partial payments).
3. Currency must match. If currencies differ, convert both amounts using the applicable exchange rate before comparison.
4. Transaction_Date must be within ±2 days of Invoice_Date unless business rules specify otherwise.

SECONDARY RULES
1. Reference_Number should match when available.
If no reference number exists, reconciliation should continue using the remaining rules.
2. Description similarity increases confidence but does not alone determine a match.
3. Payment_Mode similarity increases confidence but does not alone determine a match.
4. Customer_Name similarity increases confidence but does not alone determine a match.
5.No single secondary rule is sufficient to determine a match in the absence of the primary rules.