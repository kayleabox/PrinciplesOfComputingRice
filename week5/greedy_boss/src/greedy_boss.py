"""
Simulator for greedy boss scenario
"""
import math

STANDARD = True
LOGLOG = False
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000

class GreedyBoss(object):
    def __init__(self, days, plot_type):
        self.current_savings = 0
        self.total_earnings = 0
        self.current_wage = INITIAL_SALARY
        self.current_bribe = INITIAL_BRIBE_COST
        self.total_bribe = 0
        self.days_to_bribe = 0
        self.current_day = 0
        self.plot_type = plot_type
        self.days_in_simulation = days
        self.days_vs_earnings = []

    def greedy_boss(self, bribe_cost_increment):
        """
        Simulation of greedy boss
        """

        # Each iteration of this while loop simulates one bribe
        while self.current_day <= self.days_in_simulation:
            self.add_point()

            self.calc_days_to_bribe()

            self.update_state(bribe_cost_increment)

        return self.days_vs_earnings

    def add_point(self):
        # update list with days vs total salary earned
        # use plot_type to control whether regular or log/log plot
        if self.plot_type == STANDARD:
            self.days_vs_earnings.append((self.current_day, self.total_earnings))
        else:
            self.days_vs_earnings.append((math.log(self.current_day), math.log(self.total_earnings)))

    def calc_days_to_bribe(self):
        if self.current_savings >= self.current_bribe:
            self.days_to_bribe = 0
        else:
            money_needed_to_pay_bribe = self.current_bribe - self.current_savings
            self.days_to_bribe = int(math.ceil(money_needed_to_pay_bribe/float(self.current_wage)))


    def update_state(self, bribe_cost_increment):
        # update state of simulation to reflect bribe
        self.total_earnings += self.current_wage * self.days_to_bribe
        self.current_savings += self.current_wage * self.days_to_bribe
        self.current_savings -= self.current_bribe
        self.current_wage += SALARY_INCREMENT
        self.current_bribe += bribe_cost_increment
        self.total_bribe += self.current_bribe
        self.current_day += self.days_to_bribe

