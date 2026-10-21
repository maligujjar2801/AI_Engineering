import Make_receipt
def run_operation(function,*args,**kwargs):
    print("Function Running.....")
    result = function(*args,**kwargs)
    print(result)
    print("Function executed.....")
    return result

    

run_operation(Make_receipt.make_receipt, "Ali", "Apples", "Bananas", discount = 10, date = "2024-06-01", time = "12:00 PM")