from frappe.model import Model,Max,PI
import name_mod

mod1 = Model("database")
print(mod1.model_name())

print(Max(2,3))
print(f"Value of PI {PI}")

name_mod.printName()