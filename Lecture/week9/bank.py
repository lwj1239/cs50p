balance = 0

def main():
    print("Balance: ", balance)
    deposit(balance, 100)
    withdraw(balance, 50)
    print("Balance: ", balance)

def deposit(balance, n):
    balance += n # 默认会生成一个局部变量，所以不会读取全局变量

def withdraw(balance, n):
    balance -= n

if __name__ == "__main__":
    main()