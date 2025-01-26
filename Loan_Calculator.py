import time

class Carpayment:

    def __init__(self):
        self.carprice = 0.0
        self.loanTerm = 0.0
        self.creditScore = 0
        self.downPayment = 0.0
        self.interest_rate = self.loan_term

    def car_price(self):
        while True:
            try:
                self.car_price = float(input("Enter Car Price: "))
                if self.car_price <= 0:
                    print("Car cannot be less than or equal to zero.")
                else:
                    break
            except ValueError:
                print("Enter a valid number")


    def loan_term(self):
        valid_terms = [24, 36, 48, 60, 72]
        while True:
            try:
                self.loan_term = float(input("Select Loan Term (24, 36, 48, 60, 72 months): "))
                if self.loan_term not in valid_terms:
                    print("Please choose one of the valid loan terms.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
    
    def down_payment(self):
        while True:
            try:
                self.down_payment = float(input("Enter your down payment amount: "))
                if self.down_payment < 0:
                    print("Down payment cannot be negative")
                elif self.down_payment > self.car_price:
                    print("Down payment cannot be a larger amount than the car cost.")
                else:
                    break
            except ValueError:
                print("Enter a valid number")

    def credit_score(self):
        while True:
            try:
                self.credit_score = float(input("Enter Credit Score: "))
                if self.credit_score >= 781:
                    self.interest_rate = 5.25
                elif 661 <= self.credit_score <= 780:
                    self.interest_rate = 6.87
                elif 601 <= self.credit_score <= 660:
                    self.interest_rate = 9.83
                elif 501 <= self.credit_score <= 600:
                    self.interest_rate = 13.18
                else:
                    self.interest_rate = 15.77

                print("Calculating interest... ", end = "")
                print(f"{self.interest_rate}%")
                break

            except ValueError:
                print("Please enter a valid number")

    def calculate_monthly_payment(self):
        loan_amount = self.car_price - self.down_payment
        monthly_rate = self.interest_rate / 100 / 12
        num_payments = self.loan_term

        if monthly_rate == 0:
            monthly_payment = loan_amount / num_payments
        else:
            monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                          ((1 + monthly_rate) ** num_payments - 1)

        return monthly_payment

    def run(self):
        print("\n--- Car Loan Payment Calculator ---\n")
        self.car_price()
        self.loan_term()
        self.down_payment()
        self.credit_score()

        monthly_payment = self.calculate_monthly_payment()
        print("\nCalculating your monthly payment...")
        time.sleep(1.25)
        print(f"Your estimated monthly payment is: ${monthly_payment: .2f}")


if __name__ == "__main__":
    calculator = Carpayment()
    calculator.run()



        


