class Person:
    """ Implements Person, the base class for Employee

    """
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)


class Employee(Person):
    """ Implements Employee, derived from Person

    """
    emp_id = ""

    def __init__(self, name, age, emp_id):
        # base class's __init__ called
        Person.__init__(self, name, age)
        self.emp_id = emp_id

    def get_emp_id(self):
        print(self.emp_id)


if __name__ == "__main__":
    a = Person("Harshit", 20)
    a.get_name()
    a.get_age()
    # for the derived class, passes first 2 args to the base class
    b = Employee("Kowshik", 26, 1200)
    b.get_emp_id()
    # method from base class called
    b.get_name()