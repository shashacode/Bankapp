''' BASIC UP YO GENERATION OF ACCOUNT NUMBER'''
#just a copy of the main code
# import random

# class User():
    
#     def __init__(self, name, age, email, phone):

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):

#     def __init__(self, name, age, email, phone): #initialize child class

#         # User.__init__(self, name, age, email, phone):  
#         #initialize attributes from parent class
#         #or
#         super().__init__( name, age, email, phone)

#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)
#         return str(account_num)

# x = Account('atha', 23, "sjkdk", 84858)
# print(x.account_no)

# import random

# class User():
    
#     def __init__(self, name, age, email, phone):

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):

#     def __init__(self, name, age, email, phone): #initialize child class

#         # User.__init__(self, name, age, email, phone):  
#         #initialize attributes from parent class
#         #or
#         super().__init__( name, age, email, phone)

#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)
#         return str(account_num)
        
#     def deposit(self, amount, comment = ''):

#         self.balance += amount #add deposit value to bal
#         self.store_history('credit', amount, comment)

#         print(f"Welldone {self.name} your deposit of ₦{amount} was successful your new balance is ₦{self.balance}.")

#     def withdraw(self, amount, comment = ''):

#         self.balance -= amount #subtract deposit value to bal
#         self.store_history('debit', amount, comment)
#         print(f"Welldone {self.name} your withdrawal of ₦{amount} was successful your new balance is ₦{self.balance}.")

#     def transfer(self, amount, recipient, comment = ''):

#         self.balance -= amount #remove transfer amount from sender's bal
#         recipient.balance += amount #add transfer amount from sender's bal

#         self.store_history('transfer', amount, comment, recipient.name)
#         print(f"Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was successful your new balance is ₦{self.balance}.")


#     def store_history(self,type, amount, comment, reciever = 'same as sender'):
#         file = open("financial_statement.csv", 'a')
#         file.write(f'{type}, {self.name} {amount}, {comment}, {reciever}\n')
#         print(type, amount, comment, reciever)

# x = Account('atha', 23, 'inyangete@gmail.com', '08135859400')
# print(x.account_no)
# x.deposit(20000)
# x.withdraw(3000)
# bolu = Account('bolu', 33, 'bolu@gmail.com' , '08302049494')
# x.transfer(2000, bolu, 'flexing')

#ignore this its just classwork to cool our head
# q = [[1,3,5], [2,10,4], [4,6,7]]
# index = 0
# for i in q:
#     print(i)
# # for i, num in enumerate(q, start=1):
#     # print("q {}: {}".format(i, num))

#     for t in range(len(i)):
#         print(t)
        
# num = 5
# num = int(input('please input a value: '))

# for num_list in q:
#     if num in num_list:
#         print(num, 'found at pos: ', q.index(num_list), num_list.index(num))
#         break

# for index, num_list in enumerate(q):
#     for index2, number in enumerate(num_list):

#         if number == num:
#             print(num, 'found at pos : ', index, index2)
#notepad

#refactored to have transactions using deposit n withdraw methods instead of writing new code
import random

class User():
    
    def __init__(self, name, age, email, phone):

        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

class Account(User):

    def __init__(self, name, age, email, phone): #initialize child class

        # User.__init__(self, name, age, email, phone):  
        #initialize attributes from parent class
        #or
        super().__init__( name, age, email, phone)

        self.balance = 0
        self.account_no = self.generate_acct_no()

    def generate_acct_no(self):

        account_num = random.randint(3000000000, 3000009999)
        return str(account_num)
        
    def deposit(self, amount, comment = 'no comment', source = False):

        transaction_label = "credit"

        if source:
            transaction_type = 'transfer'
            source = source.name
        else:
            transaction_type = 'deposit'
            source = self.name

        self.balance += amount #add deposit value to bal
        self.store_history(transaction_type, transaction_label, amount, self.name, comment, source)

        print(f"Welldone {self.name} your deposit of ₦{amount} was successful your new balance is ₦{self.balance}.")

    def withdraw(self, amount, comment = 'no comment', collector = False):

        transaction_label = "debit"

        if collector:
            transaction_type = 'transfer'
            collector = collector.name
        else:
            transaction_type = 'withdrawal'
            collector = self.name

        self.balance -= amount #subtract deposit value from bal
        self.store_history(transaction_type, transaction_label, amount,self.name, comment, collector)
        print(f"Welldone {self.name} your withdrawal of ₦{amount} was successful your new balance is ₦{self.balance}.")

    def transfer(self, amount, recipient, comment = ''):

        self.withdraw(amount, comment, recipient)
        recipient.deposit(amount, comment, self)

        print(f"Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was successful your new balance is ₦{self.balance}.")


    def store_history(self, transaction_type, transaction_label, amount, source, comment, reciever = 'same as sender'):
        file = open("financial_statement.csv", 'a')
        file.write(f'{transaction_type},{transaction_label}, {amount}, {source}, {comment}, {reciever}\n')
        print(transaction_type, amount, comment, reciever)

atha = Account('atha', 23, 'inyangete@gmail.com', '08135859400')
print(atha.account_no)
atha.deposit(20000)
atha.withdraw(3000)
bolu = Account('bolu', 33, 'bolu@gmail.com' , '08302049494')
atha.transfer(2000, bolu, 'flexing')
