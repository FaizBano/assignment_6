class Bank:
     bank_name = "state Bank"

     @classmethod

     def change_bank_name(cls, name):
          bank_name = name
          cls.bank_name = name
b1 = Bank()
print(f"{b1.bank_name} is the Central or main Bank of Pakistan!!!!")
b1.change_bank_name("National Bank of Pakistan")
print(f"the New name of State Bank is {b1.bank_name}")
        
