# Access modify public , private and protected

# public by default hota he
# protected veriaable is not consider good in python

class Employee:

    def __init__(self, name, salary, ssn):
        # now making instance variables

        self.name = name  # public

        # kishi bhi variable ya parameter ko protected bana k liye aik underline dete hen jesa _salary
        self._salary = salary # protected
        self.__ssn = ssn        # private

emp = Employee("Faiz" , 50000 , "418078")
print(emp.name)
print(emp._salary)
print(emp._Employee__ssn) # ham private variable ko direct access nhi kr sakte but agr class k naam k saath_ (underscore)kaga den to access ho jae ga

        