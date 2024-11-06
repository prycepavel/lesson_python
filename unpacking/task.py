my_gadgets = [{'brand': 'Samsung', 'ram_qty': 16},
              {'brand': 'Honor', 'ram_qty': 8}, {'brand': 'Sony'}]

samsung, honor, sony = my_gadgets


def gadget_parameters(brand, ram_qty=0):
    if not ram_qty:
        return f"На {brand} не установлен модуль оперативной памяти"
    return f"На {brand} установлено {ram_qty}Gb оперативной памяти"


print(gadget_parameters(**samsung))
print(gadget_parameters(**honor))
print(gadget_parameters(**sony))
