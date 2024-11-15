class BankAccount:
    """
    Clase para gestionar las operaciones de una cuenta bancaria.
    """

    def __init__(self, initial_balance):
        """
        Inicializa la cuenta bancaria con un saldo inicial.

        Args:
            initial_balance (int): El saldo inicial de la cuenta.
        """
        self.balance = initial_balance
        self.transactions = []
        self.commits = []

    def read(self):
        """
        Lee e imprime el saldo actual de la cuenta.
        """
        print(self.balance)

    def credit(self, amount):
        """
        Acredita una cantidad al saldo de la cuenta.

        Args:
            amount (int): La cantidad a acreditar.
        """
        self.transactions.append(("credit", amount))
        self.balance += amount

    def debit(self, amount):
        """
        Debita una cantidad del saldo de la cuenta.

        Args:
            amount (int): La cantidad a debitar.
        """
        if self.balance >= amount:  # Verifica si hay suficiente saldo
            self.transactions.append(("debit", amount))
            self.balance -= amount
        else:
            print("Saldo insuficiente") # Manejo de error si no hay suficiente saldo


    def abort(self, transaction_index):
        """
        Anula una transacción específica.

        Args:
            transaction_index (int): El índice de la transacción a anular.
        """
        if not self.commits: # Verifica si hay commits previos
            transaction_index -= 1
            if 0 <= transaction_index < len(self.transactions):
                transaction_type, amount = self.transactions[transaction_index]
                if transaction_type == "credit":
                    self.balance -= amount
                elif transaction_type == "debit":
                    self.balance += amount
                self.transactions.pop(transaction_index)
            else:
                print("Índice de transacción inválido") # Manejo de error si el índice es inválido

    def rollback(self, commit_index):
        """
        Revierte los cambios hasta un commit específico.

        Args:
            commit_index (int): El índice del commit al que revertir.
        """
        if 0 < commit_index <= len(self.commits):
            self.balance = self.commits[commit_index-1]
            self.commits = self.commits[:commit_index-1]
            self.transactions = [] # Borra las transacciones después del rollback
        else:
            print("Índice de commit inválido") # Manejo de error si el índice es inválido

    def commit(self):
        """
        Guarda los cambios permanentemente.
        """
        self.commits.append(self.balance)
        self.transactions = [] # Borra las transacciones después del commit


# Lee la entrada
initial_balance = int(input('Ingrese el saldo inicial de la cuenta: '))
num_operations = int(input('Ingrese el número de operaciones a realizar: '))

account = BankAccount(initial_balance)

for _ in range(num_operations):  # Bucle principal, solo uno
    operation = input('Ingrese la operación (read, credit, debit, abort, rollback, commit): ').split()
    op_code = operation[0]

    if op_code == "read":
        account.read()
    elif op_code == "credit":
        if len(operation) > 1:
            account.credit(int(operation[1]))
        else:
            print("Error: La operación 'credit' requiere un operando.")
    elif op_code == "debit":
        if len(operation) > 1:
            account.debit(int(operation[1]))
        else:
            print("Error: La operación 'debit' requiere un operando.")
    elif op_code == "abort":
        if len(operation) > 1:
            account.abort(int(operation[1]))
        else:
            print("Error: La operación 'abort' requiere un operando.")
    elif op_code == "rollback":
        if len(operation) > 1:
            account.rollback(int(operation[1]))
        else:
            print("Error: La operación 'rollback' requiere un operando.")
    elif op_code == "commit":
        account.commit()

