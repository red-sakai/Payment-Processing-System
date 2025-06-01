from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount:float):
        pass
    
    @abstractmethod
    def validate(self):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of PHP{amount:.2f}.")
    
    def validate(self):
        if len(self.card_number) != 16:
            print("Invalid card number.")
        else:
            print("Card number validated.")

class PayPalPayment(PaymentMethod):
    def __init__(self, email: str):
        self.email = email
    
    def process_payment(self, amount: float):
        print(f"Processing paypal payment of PHP{amount:.2f}.")
    
    def validate(self):
        if "@" not in self.email:
            print("Invalid email address.")
        else:
            print("Email address validated.")

class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def process_payment(self, amount: float):
        print(f"Processing crpyto payment of PHP{amount:.2f}.")
    
    def validate(self):
        if len(self.wallet_address) < 26:
            print("Invalid wallet address.")
        else:
            print("Wallet address validated.")

def checkout(payment: PaymentMethod, amount: float):
    payment.validate()
    payment.process_payment(amount)

# test cases
print("Success test cases:")
success_credit_card = CreditCardPayment("1234567812345678")
success_paypal = PayPalPayment("user@gmail.com")
success_crypto = CryptoPayment("0xABCDEF1234567890ABCDEF123456")

checkout(success_credit_card, 100.0)
checkout(success_paypal, 150.0)
checkout(success_crypto, 0.05)

print("\nFailed test cases:")
failed_credit_card = CreditCardPayment("1234567812346")
failed_paypal = PayPalPayment("usergmail.com")
failed_crypto = CryptoPayment("0xABCDEF1234567890")

checkout(failed_credit_card, 100.0)
checkout(failed_paypal, 150.0)
checkout(failed_crypto, 0.05)