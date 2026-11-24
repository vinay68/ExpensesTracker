import mysql.connector as db
class Expense:
    con=db.connect(user='root',password='1234',host='localhost',database='Expensestracker')
    cur=con.cursor()
    def addexpense(self):
        print('='*10,'ADD EXPENSES','='*10)
        self.a=int(input('Enter Amount: '))
        self.b=input('Enter Category: ')
        self.d=input('Enter Description: ')
        self.date=input('Enter Date: ')
        self.cur.execute('''insert into expenses(date,category,description,amount) values(%s,%s,%s,%s)''',[self.date,self.b,self.d,self.a])
        self.con.commit()
        print('💰Expense details saved successfully!')
    def viewexpenses(self):
        self.cur.execute('select * from expenses')
        data=self.cur.fetchall()
        print('='*22,'VIEW EXPENSES','='*22)
        print()
        print(f'{"S.No":^10}{"Date":^12}{"Category":^12}{"Description":^15}{"Amount":^10}')
        print('-'*60)
        for row in data:
            from datetime import datetime
            date=row[1]
            if isinstance(date,str):
                  date=datetime.strptime(date,"%y-%m-%d").date()
            date=date.strftime("%d-%m-%y")
            print(f'{row[0]:^10}{date:^12}{row[2]:^12}{row[3]:^15}{"₹"+str(row[4]):^10}')
        print('-'*60)
    def calculatetotal(self):
        print('='*22,'CALCULATE TOTAL EXPENSES','='*22)
        print()
        self.cur.execute('select sno,date,category,description,amount,sum(amount) over(order by sno asc) from expenses')
        data=self.cur.fetchall()
        print(f'{"S.No":^10}{"Date":^12}{"Category":^12}{"Description":^15}{"Amount":^10}{"Total":^12}')
        print('-'*71)
        for row in data:
            from datetime import datetime
            date=row[1]
            if isinstance(date,str):
                date=date.strptime(date,"%y-%m-%d").date()
            date=date.strftime("%d-%m-%y")
            print(f'{row[0]:^10}{date:^12}{row[2]:^12}{row[3]:^15}{"₹"+str(row[4]):^10}{"₹"+str(row[5]):^12}')
        print('-'*71)   
          
        

obj=Expense()
while True:
    print('='*5,'EXPENSE TRACKER','='*5)
    print('1.Add Expense')
    print('2.View Expenses')
    print('3.Calculate Total')
    print('4.Exit')     
                    
    choice=input('choose one option: ')

    if choice=='1' or choice.lower()=='add expense':
        obj.addexpense()
    elif choice=='2' or choice.lower()=='view expenses':
        obj.viewexpenses()
    elif choice=='3' or choice.lower()=='calculate total':
        obj.calculatetotal()
    elif choice=='4' or choice.lower()=='exit':
          print('Thank you for using Expense Tracker!')
          print('Keep tracking, keep saving. Goodbye!')
          obj.cur.close()
          obj.con.close()
          break
