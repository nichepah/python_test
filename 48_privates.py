class Employee:
    """ Musings on access restrictions and conventions

    leading single _ indicates protected; no error shown howsoever you use it
    __ indicates private, results in error from outside the class
    """
    def __init__(self, name, desig, plNo):
        self.name = name
        self.desig = desig
        self.plNo = plNo

    def _show_sal(self):
        if self.desig == 'DM':
            print("Rs. 100")
        else:
            print("Rs. `1000")

    def __promote(self, newDesig):
        self.desig = newDesig

    def show_details(self):
        print(self.name, self.desig, self.plNo)


if __name__ == "__main__":
    e_buendia = Employee("Buendia", "DM", 1987)
    e_buendia.show_details()
    # error
    # e_buendia.__promote("GM")
    # Works
    e_buendia._show_sal()



