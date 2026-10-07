
def total_revenue(adult_ticket_sold, student_ticket_sold):
    adult_price = 10
    student_price = 7
    total_tickets = adult_ticket_sold + student_ticket_sold
    adult_revenue = adult_ticket_sold * adult_price
    student_revenue = student_ticket_sold *student_price
    if total_tickets > 100:
        print("Large Audience")
    print("The total revenue is " + str(adult_revenue + student_revenue) + " euros")

total_revenue(100, 90)