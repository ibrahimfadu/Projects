from datetime import datetime
date_format="%d-%m-%Y"
CATEGORY={
    "I":"Income",
    "E":"Expenes"
}
def get_date(prompt,allow_default=False):
    date_for=input(prompt)
    if allow_default is not date_for:
        return datetime.today().strftime(date_format)
    try:
        valid_for=datetime.strptime(date_for,date_format)
        return valid_for.strftime(date_format)
    except ValueError :
        print("Invalid date formate Please enter in dd-mm-yyyy: ")
        return get_date(prompt,allow_default)
def get_amount():
    try :
        amount=float(input("Enter the amount: "))
        if amount<=0:
            raise "Amount must be non-zero and non-negative value"
        
    except ValueError as e:
        print(e)
        return get_amount()
def get_category():
    category=input("Enter the category I for Income or E for Expense: ").upper()
    if category in CATEGORY:
        return CATEGORY[category]
    print("Invalid category, for Income or E for Expense")
    return get_category()
def get_description():
    description=input("Enter the description: ")
    return description