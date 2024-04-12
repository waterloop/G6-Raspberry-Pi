class State:
    current_state = 0
    def select(self):
        if current_case == 0:
            return self.default_case()
        else if current_case == 1:
            return self.case1()
        else if current_case == 1:
            return self.case2()
        else if current_case == 1:
            return self.case3()
    def case1(self):
        return "This is case 1"

    def case2(self):
        return "This is case 2"

    def case3(self):
        return "This is case 3"
    def default_case(self):
        return "This is the default case"