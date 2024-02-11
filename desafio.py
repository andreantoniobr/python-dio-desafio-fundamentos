MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

INVALID_VALUE_TEXT = "Não foi possivel realizar operação! O valor informado é inválido."
DESIRED_VALUE_TEXT = "Informe o valor desejado: "
WITHDRAWAL_LIMIT_EXCEEDED_TEXT = "Não foi possivel realizar operação. Valor de saque maior que limite diario por transação"
FINAL_THANKS_TEXT = "Sistema finalizado com sucesso. Obrigado por usar nosso sistema!"
ACCOUNT_BALANCE_INSUFFICIENT_TEXT = "Saldo insuficiente para realizar operação."
WITHDRAWAL_AMOUNT_EXCEEDED_TEXT = "Limite de saques diários excedido."
NO_MOVEMENT_TEXT = "Não foram realizadas movimentações."
ACCOUNT_BALANCE_BEFORE_TEXT = str.center(" EXTRATO ", 30, "=")
ACCOUNT_BALANCE_AFTER_TEXT = f"=" * 30
WITHDRAW_AMOUNT_LIMIT = 3
WITHDRAW_VALUE_LIMIT = 500

account_balance = 0
withdraw_amount = 0
account_statement = ""

def try_get_float_value(data:str): 
    value = 0   
    can_get_value = False
    try:            
        value = float(data)
        can_get_value = True
    finally:
        return can_get_value, value

def try_get_positive_float_value(data:str):    
    can_get_positive_value = False
    can_get_value, value = try_get_float_value(data)
    if can_get_value and value > 0:
        can_get_positive_value = True
    return can_get_positive_value, value

def try_withdraw(account_balance:float, account_statement:float, withdraw_amount:int):
    if withdraw_amount < WITHDRAW_AMOUNT_LIMIT:
        withdraw_data = input(DESIRED_VALUE_TEXT)
        can_get_withdraw_value, withdraw_value = try_get_positive_float_value(withdraw_data)
        if can_get_withdraw_value:            
            if withdraw_value > WITHDRAW_VALUE_LIMIT:
                print(WITHDRAWAL_LIMIT_EXCEEDED_TEXT, end="\n")
            elif withdraw_value > account_balance:
                print(ACCOUNT_BALANCE_INSUFFICIENT_TEXT, end="\n")
            else:
                account_balance -= withdraw_value
                withdraw_amount += 1
                account_statement += f"Saque: R$ {withdraw_value:.2f}\n"
                print(f"Saque de R$ {withdraw_value:.2f} realizado com sucesso!", end="\n")                
        else:
            print(INVALID_VALUE_TEXT, end="\n")
    else:
        print(WITHDRAWAL_AMOUNT_EXCEEDED_TEXT, end="\n")
    return account_balance, account_statement, withdraw_amount

def try_deposit(account_balance:float, account_statement:float) -> float:
    deposit_data = input(DESIRED_VALUE_TEXT)
    can_get_deposit_value, deposit_value = try_get_positive_float_value(deposit_data)
    if can_get_deposit_value:
        account_balance += deposit_value
        account_statement += f"Deposito: R$ {deposit_value:.2f}\n"
        print(f"Deposito de R$ {deposit_value:.2f} realizado com sucesso!", end="\n")  
    else:
        print(INVALID_VALUE_TEXT, end="\n")
    return account_balance, account_statement

def print_account_balance(account_balance:float, account_statement:float):
    print(ACCOUNT_BALANCE_BEFORE_TEXT, end="\n")
    if len(account_statement) > 0:
        print(f"{account_statement}", end="\n")
    else:
        print(NO_MOVEMENT_TEXT, end="\n")
    print(str.center(f"Saldo atual: R$ {account_balance:.2f}", 20, " "), end="\n")
    print(ACCOUNT_BALANCE_AFTER_TEXT, end="\n")

def quit_bank():
    print(FINAL_THANKS_TEXT , end="\n")

while True:
    option = input(MENU)
    if option == "d":
        account_balance, account_statement = try_deposit(account_balance, account_statement)        
    elif option == "s":
        account_balance, account_statement, withdraw_amount = try_withdraw(account_balance, account_statement, withdraw_amount)
    elif option == "e":       
        print_account_balance(account_balance, account_statement)
    elif option == "q":
        quit_bank()
        break
    else:
        print(INVALID_VALUE_TEXT, end="\n")