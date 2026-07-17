from dataclasses import dataclass

@dataclass
class Invoice:
    invoice_no:int
    customer:str
    total:float

i1 = Invoice(241,"Akil",-2091.5)
# print(i1)

class Controller:
    def validate(self,invoice:Invoice):
        if invoice.invoice_no<0 or invoice.invoice_no>1000:
            print("Invalid invoice no")
            return
        if not invoice.customer:
            print("Please provide custmer name")
            return
        if invoice.total<0:
            print("Total cannot be negative")
            return
        print("Success")

c1 = Controller()
c1.validate(i1)
        

