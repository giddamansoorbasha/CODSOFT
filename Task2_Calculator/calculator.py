class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        try:
            return self.a+self.b
        except Exception as e:
            print(f"Error: {e}")
    
    def sub(self):
        try:
            return self.a-self.b
        except Exception as e:
            print(f"Error: {e}")
    
    def mul(self):
        try:
            return self.a*self.b
        except Exception as e:
            print(f"Error: {e}")
    
    def div(self):
        try:
            if self.b==0:
                return "Error: Can't Divide With Zero"
            return self.a/self.b
        except Exception as e:
            print(f"Error: {e}")
        
    
def main():
    try:
        while True:
            print("\n-----Welcome To Calculator-----\n")
            a = float(input("Enter the first number : "))
            b = float(input("Enter the second number : "))
            cal = Calculator(a,b)

            choice = input("\n1) Addition (+)\n2) Subtraction (-)\n3) Multiplication (*)\n4) Division (/)\n5) Exit\n\nEnter the Choice : ")
            if choice in ("1", "+"):
                print(f"Addition : {cal.add()}")
            elif choice in ("2", "-"):
                print(f"Subtraction : {cal.sub()}")
            elif choice in ("3", "*"):
                print(f"Multiplication : {cal.mul()}")
            elif choice in ("4", "/"):
                print(f"Division : {cal.div()}")
            elif choice == "5":
                print("Thank You, Bye!")
                break
            else:
                print("Invalid Input")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
