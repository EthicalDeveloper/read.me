class BankAccount:
    def __init__(self,name,balance,pin):
        self.name=name
        self.balance=balance
        self.pin=pin

    def greeting(self):
        code = int(input("Enter 4 digits pin:"))
        tries=0
        left=3

        while tries<2:

            if code!=self.pin:
                print("Wrong pin! You have %s tries left. " %left)
                code = int(input("Enter 4 digits pin:"))
                tries=tries+1
                left=left-1
                if left==1:
                    print("Sorry but we will have to finish this session. Bye!")

            elif code==self.pin:
                print("Welcome to Bank of Utopia Mr/Mrs %s" % self.name)
                break


    def main_question(self):
        question=input("How can I help you today? Deposit(D)//Withdraw(W)//See the Balance(S)//Exit(E):")
        question=question.lower()
        while True:
            if question=='d' or question=='deposit':
                amount_d = float(input("Amount:"))
                self.deposit(amount_d)
                question = input("Is there anything else I can do for you? Deposit//Withdraw//See the Balance//Exit:")

            elif question=='w' or question=='withdraw':
                amount_w=float(input("Amount:"))
                self.withdrawal(amount_w)
                question = input("Is there anything else I can do for you? Deposit//Withdraw//See the Balance//Exit:")

            elif question=='s' or question=='see':
                self.see_balance()
                question = input("Is there anything else I can do for you? Deposit//Withdraw//See the Balance//Exit:")


            elif question=='e' or question=='exit':
                print("Thank you for using Bank Of Utopia")
                break











    def deposit(self,damount):
        self.balance=self.balance+damount

    def withdrawal(self,wamaount):
        self.balance=self.balance-wamaount

    def see_balance(self):
        print("Your current balance is %s"%self.balance)










client1=BankAccount('Kerim',1000,1997)
client2=BankAccount('Arslan',2000,1998)
client3=BankAccount('Alym',3000,1999)

client1.greeting()
client1.main_question()








