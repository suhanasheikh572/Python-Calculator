num1 = float(input("Enter 1st number:"))
sign = input("Enter a operator:")
num2 = float(input("Enter 2nd number:"))

match sign :

    case "+" :

        print(num1 + num2)

    case "-" :

        print(num1 - num2)

    case "*" :

        print(num1 * num2)

    case "/" :

        print(num1 / num2)

    case "//" :

        print(num1 // num2)

    case "%" :

        print(num1 % num2)

    case _ :

        print("not a valid operator")

  

