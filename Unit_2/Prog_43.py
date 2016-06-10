
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
        print 'Success. Entered Date is Validated'
    except ValueError:
        # raise ValueError("Incorrect date")
        print 'Incorrect date'

print 'Enter your date in this format DD-MM-YYYY'

validate('31-02-2013')
validate('12-06-2015')

