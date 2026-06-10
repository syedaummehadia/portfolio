def add(x, y):
    """Do numbers ko add karta hai"""
    return x + y

def subtract(x, y):
    """Do numbers ko subtract karta hai"""
    return x - y

def multiply(x, y):
    """Do numbers ko multiply karta hai"""
    return x * y

def divide(x, y):
    """Do numbers ko divide karta hai"""
    if y == 0:
        return "Error: Zero se divide nahi kar sakte"
    return x / y

def show_menu():
    print("\n=== Python Calculator ===")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def calculator():
    while True:
        show_menu()
        choice = input("Apna choice select karein 1/2/3/4/5: ")
        
        if choice == '5':
            print("Calculator band ho raha hai. Allah Hafiz!")
            break
            
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Pehla number daalein: "))
                num2 = float(input("Doosra number daalein: "))
                
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
                    
            except ValueError:
                print("Error: Sirf numbers hi daalein!")
        else:
            print("Ghalat choice! 1 se 5 tak number daalein")

# Program yahan se start hota hai
if __name__ == "__main__":
    calculator()
