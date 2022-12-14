import datetime
class ATM():
  def __init__(self):
      self.user_data={10167:{"Amount":50000,"PIN":5890},10187:{"Amount":478000,"PIN":3857},10763:{"Amount":763423,"PIN":7832}}
      self.usrId=int(input("Enter your User Id: "))
      self.credit_amount=0
      self.debit_amount=0
      self.current_dateTime=None
      self.bank_details=dict()
      self.save_data={}
      if self.usrId not in self.user_data.keys():
        print("Unable to detect the card, Please insert Your card again")
        self.__init__()
      
  def varify_user(self):
    flag=False
    if self.usrId in self.user_data.keys():
      count=0
      while count<3:
            atm_pin=int(input("Enter your 4 digit Pin: "))
            
            if atm_pin not in range(1000,10000):
              print("Only Four digits are allowed")
              count+=1
            else:   
              count+=1
              if self.user_data[self.usrId]["PIN"]==atm_pin: 
                  flag=True
                  break
              else:
                  continue 
           
      else:
        print("Your card is Locked")
      return flag
  
  def withdraw_balance(self,withdraw_amount):
    self.debit_amount=withdraw_amount
    self.current_dateTime=datetime.datetime.now().strftime("%d-%m-%y ; %H:%M:%S")
    if withdraw_amount<=self.user_data[self.usrId]["Amount"]:
     self.user_data[self.usrId]["Amount"]=self.user_data[self.usrId]["Amount"]-withdraw_amount
     print("Please wait while your transaction is in Process")
    else:
      print("Insufficient Balance!!")
      withdraw_amount=int(input("Enter a valid amount"))
      self.withdraw_balance(withdraw_amount)

  def deposit_balance(self,deposit_amount):
     self.credit_amount=deposit_amount
     self.current_dateTime=datetime.datetime.now().strftime("%d-%m-%y ; %H:%M:%S")
     self.user_data[self.usrId]["Amount"]=self.user_data[self.usrId]["Amount"]+deposit_amount
     print("The amount is added in your account Successfully")

  def current_balance(self):
    return self.user_data[self.usrId]["Amount"]

  def bank_statement(self):
    self.bank_details={"current balance":self.user_data[self.usrId]["Amount"],"Credited Amount":self.credit_amount,"Debited Amount":self.debit_amount,"Date and Time":self.current_dateTime}
    self.save_data=self.bank_details
    self.credit_amount=0
    self.debit_amount=0
    self.current_dateTime=None
    return self.save_data
try:
  atm_class=ATM()
  isVarified=atm_class.varify_user()
  choice_list={1:"Withdraw Balance",2:"Deposit Balance",3:"Check Balance",4:"Print Transaction Details",5:"Exit"}
  press_key=None
  while not (press_key==5) and isVarified==True:
    for key,value in choice_list.items():
      print("Select {} to {}".format(key,value))
    
    
 
    press_key=int(input("Enter your choice "))
    if press_key==1:
      withdraw_amount=int(input("Enter the withdrawal amount: "))
      atm_class.withdraw_balance(withdraw_amount)
    elif press_key==2:
      deposit_amount=int(input("Enter the Deposit amount: "))
      atm_class.deposit_balance(deposit_amount)
    elif press_key==3:
      print("Your current balance is",atm_class.current_balance())
    elif press_key==4:
      bank_history=atm_class.bank_statement()
      print("-----------Transaction Details--------------")
      
      print("Current Balance",bank_history["current balance"])
      if bank_history["Credited Amount"]!=0:
        print("Credited Amount",bank_history["Credited Amount"])
      if bank_history["Debited Amount"]!=0:
        print("Debited Amount",bank_history["Debited Amount"])
      if bank_history["Credited Amount"]==0 and bank_history["Debited Amount"]==0:
        bank_history["Date and Time"]=datetime.datetime.now().strftime("%d-%m-%y ; %H:%M:%S")
        print("Date and Time",bank_history["Date and Time"])
      else:
        print("Date and Time",bank_history["Date and Time"])
    elif press_key==5:
      print("Thank you for visiting")
    else:
      print("Please Enter a valid choice ")
     
except:
  print("Something went wrong. Please contact to bank")
  
