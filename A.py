# class A:
# #     def __init__(self,age,name,address):
# #         print(age," ",name," ",address)
# # obj=A(20,"abir","jhalda")
#      a=20
#      _b=10
#      __c=30
#      print(a," ",_b," ",__c)
# class B(A):
#     def show(self):
#          print(self.a)
#          print(self._b)
#          print(self.__c)
# obj=B()
# obj.show()
# class Father:
#      def lands(self):
#           print("Having 50 acres land")
# class son(Father):
#      def money(self):
#           print("having 20 lakhs money")
# S=son()
# S.lands()
# S.money()
# class A:
#      num1=int(input("Eneter the first number:"))
#      num2=int(input("Enter the second number:"))
     
#      def add(self):
#           print("Add",self.num1+self.num2)
#      def sub(self):
#           print("Sub",self.num1-self.num2)
          
# class B(A):
#      def multi(self):
#           print("multi",self.num1*self.num2)     
#      def div(self):
#           print("div",self.num1/self.num2)   
#      def rem(self):
#           print("rem",self.num1%self.num2) 
               
# obj=B()
# obj.add()
# obj.sub()
# obj.multi()
# obj.div()
# obj.rem()
# class father:
#      surname="Saw"
# class son(father):
#      def show(self):
#           print("Abir "+self.surname)
# class GSon(son):
#      def disp(self):
#           print("Aditya "+self.surname)
# s=son()
# s.show()

# Gs=GSon()
# Gs.disp()
# class Abir:  
#      back="Oracle DB Java"
#      def backend(self):
#           print("Backend task implemented:",self.back)
# class Sanatanu:
#      front="HTML CSS JAVASCRIPT"
#      def frontend(self):
#           print("Frontend task implemented",self.front)
# class Teamlead(Abir,Sanatanu):
#      def show(self):
#           print("Dynamic website created......")
# T=Teamlead()
# T.backend()
# T.frontend()
# T.show()
# class Father:
#      surname="SAW"
#      def show(self):
#           print("My Name surname is",self.surname)
# class Son1(Father):
#      def disp(self):
#           print("Abir ",self.surname)
# class Son2(Father):
#      def out(self):
#           print("Aditya ",self.surname)
# S1=Son1()
# S2=Son2()

# S1.disp()
# S2.out()
class A:
     def disp(self):
          print("WElcome to pornhub")
class B(A):
     def disp(self):
          print("Welcome to brazzers")
class C(B):
     def disp(self):
          super().disp()
          print("Welccome to vixen")
obj=A()
obj.disp()

