
# Test Case 1
# >>>
# Enter your starting annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 500000
# Enter the semiannual raise, as a deci mal: .03
# Number of months: 142
# >>>
# Test Case 2
# >>>
# Enter your starting annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .1
# Enter the cost of your dream home: 800000
# Enter the semiannual raise, as a deci mal: .03
# Number of months: 159
# >>>
# Test Case 3
# >>>
# Enter your starting annual salary: 75000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 1500000
# Enter the semiannual raise, as a deci mal: .05
# Number of months: 261
# >>>


def calculateMonthlyPortion(value):
    return value / 12


def calculateMonthlySavingsRate(current_savings, monthly_rate):
    return current_savings * monthly_rate


def calculateCurrentSavings(current_savings, monthly_savings, monthly_rate):
    return \
        monthly_savings + \
        calculateMonthlySavingsRate(current_savings, monthly_rate)


def getUserData():
    annual_salary = float( \
        input("Enter your annual salary: "))
    
    portion_saved = float( \
        input("Enter the percent of your salary to save, as a decimal: "))
        
    total_cost = float( \
        input("Enter the cost of your dream home: "))
    
    semi_annual_raise = 0.05
    portion_down_payment = 0.25
    annual_rate = 0.04
    monthly_rate = calculateMonthlyPortion(annual_rate)
    current_savings = 0
    
    return (
        annual_salary, 
        portion_saved, 
        total_cost, 
        semi_annual_raise, 
        portion_down_payment, 
        annual_rate, 
        monthly_rate,
        current_savings
    )


def calculateMonthsToSave(
        current_savings, 
        dpp, monthly_rate, 
        semi_annual_raise
    ):

    total_months = 0
    
    while(current_savings < dpp.calculateDownPaymentValue()):
        if (total_months != 0 and total_months % 6 == 0):
            dpp.setNewAnnualSalary(semi_annual_raise)
            
        current_savings += \
            calculateCurrentSavings (
                current_savings, 
                dpp.calculateMonthlySavedValue(), 
                monthly_rate
            )
        
        total_months +=  1
        
    return total_months
    

class DownPaymentPlannerClass:

    def __init__(
            self, 
            annual_salary, 
            portion_saved, 
            total_cost, 
            portion_down_payment
        ):

        self.annual_salary = annual_salary
        self.portion_saved = portion_saved
        self.total_cost = total_cost
        self.portion_down_payment = portion_down_payment

    def getAnnualSalary(self):
        return self.annual_salary
    
    def getMonthlySalary(self):
        return calculateMonthlyPortion(self.annual_salary)

    def getPortionSaved(self):
        return self.portion_saved

    def getTotalCost(self):
        return self.total_cost

    def getDownPaymentPortion(self):
        return self.portion_down_payment

    def calculateDownPaymentValue(self):
        return self.getTotalCost() * self.getDownPaymentPortion()

    def calculateMonthlySavedValue(self):
        return \
            calculateMonthlyPortion(self.getAnnualSalary()) * \
            self.getPortionSaved()
    
    def setNewAnnualSalary(self, semi_annual_raise):
        self.annual_salary += self.annual_salary * semi_annual_raise
 
def start():
        annual_salary, \
        portion_saved, \
        total_cost, \
        semi_annual_raise, \
        portion_down_payment, \
        annual_rate, \
        monthly_rate, \
        current_savings = getUserData()


        downPaymentPlanner = \
            DownPaymentPlannerClass (
                annual_salary,
                portion_saved,
                total_cost,
                portion_down_payment
            )


        total_months = \
            calculateMonthsToSave (
                current_savings, 
                downPaymentPlanner, 
                monthly_rate, 
                semi_annual_raise
            )
            
            
        print("Number of months:", total_months)           


start()