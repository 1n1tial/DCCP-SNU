"""
Program: Simple Calculator
"""

EPSILON = 1e-5

print("=== Welcome to the Calculator Program ===")
print("Enter an expression or command (type 'quit' to exit).")

while True:
    expr = input(">>> ").lower()
    if expr == "quit":
        print("Program terminated.")
        break

    tokens = expr.split()
    if len(tokens) == 0:
        continue

    try:
        # 1) Addition
        if "+" in tokens:
            a, b = float(tokens[0]), float(tokens[2])
            result = a + b

        # 2) Subtraction
        elif "-" in tokens:
            a, b = float(tokens[0]), float(tokens[2])
            result = a - b

        # 3) Multiplication
        elif "*" in tokens:
            a, b = float(tokens[0]), float(tokens[2])
            result = a * b

        # 4) Division
        elif "/" in tokens:
            a, b = float(tokens[0]), float(tokens[2])
            if b == 0:
                print("Error: Division by zero")
                continue
            result = a / b

        # 5) Exponentiation
        elif "^" in tokens:
            a, b = float(tokens[0]), float(tokens[2])
            result = a ** b

        # 6) Integer division (quotient)
        elif "//" in expr:
            m, n = int(tokens[0]), int(tokens[2])
            if n == 0:
                print("Error: Division by zero")
                continue
            result = m // n

        # 7) Remainder
        elif "%" in expr:
            m, n = int(tokens[0]), int(tokens[2])
            if n == 0:
                print("Error: Division by zero")
                continue
            result = m % n

        # 8) Permutation (n P r)
        elif "p" in tokens:
            n, r = int(tokens[0]), int(tokens[2])
            result = 1
            for i in range(r):
                result *= n-i

        # 9) Combination (n C r)
        elif "c" in tokens:
            n, r = int(tokens[0]), int(tokens[2])
            result = 1
            for i in range(r):
                result *= n-i
            for i in range(r):
                result //= i+1

        # 10) Square root (sqrt) using Newton's method
        elif "sqrt" in tokens:
            a = float(tokens[1])
            guess = 1.0
            quotient = 0.0
            while True:
                quotient = a / guess
                average = (guess + quotient) / 2
                error = average - guess if average - guess > 0 else guess - average
                if error <= EPSILON:
                    break
                guess = average
            result = guess

        # 11) GCD (greatest common divisor)
        elif "gcd" in tokens:
            m_, n_ = int(tokens[1]), int(tokens[2])
            m = m_ if m_ > n_ else n_
            n = m_ if m_ < n_ else n_
            while True:
                r = m % n
                if r:
                    m = n
                    n = r
                else:
                    break
            result = n

        # 12) Decimal to binary base conversion
        elif "dec2bin" in tokens:
            n = tokens[1]
            if n[0] == '-' and int(tokens[1]) != 0:
                print('-', end='')
                n = n[1:]
            remainders_list = []
            while True:
                if int(n) <= 1:
                    remainders_list.append(int(n))
                    break
                remainders_list.append(int(n) % 2)
                n = int(n) // 2
            for i in range(len(remainders_list)):
                print(remainders_list[len(remainders_list)-i-1], end='')
            print()
            continue

        # 13) Decimal to hexadecimal base conversion
        elif "dec2hex" in tokens:
            n = tokens[1]
            if n[0] == '-' and int(tokens[1]) != 0:
                print('-', end='')
                n = n[1:]
            remainders_list = []
            while True:
                if int(n) <= 15:
                    remainders_list.append(int(n))
                    break
                remainders_list.append(int(n) % 16)
                n = int(n) // 16
            for i in range(len(remainders_list)):
                remainder = remainders_list[len(remainders_list)-i-1]
                if remainder == 10:
                    print('A', end='')
                elif remainder == 11:
                    print('B', end='')
                elif remainder == 12:
                    print('C', end='')
                elif remainder == 13:
                    print('D', end='')
                elif remainder == 14:
                    print('E', end='')
                elif remainder == 15:
                    print('F', end='')
                else:
                    print(remainder, end='')
            print()
            continue

        # 14) Binary to decimal base conversion
        elif "bin2dec" in tokens:
            n, is_negative = tokens[1], 1
            if n[0] == '-':
                is_negative = -1
                n = n[1:]
            result = 0
            for i in range(len(n)):
                result += (2**i) * int(n[len(n)-i-1])
            result *= is_negative

        # 15) Lagrange Interpolation
        elif "lagrange" in tokens:
            # Format: lagrange x0 y0 x1 y1 ... xn yn x
            if len(tokens) < 4 or len(tokens) % 2 != 0:
                raise ValueError(
                    "Invalid number of arguments for Lagrange interpolation"
                )
            
            is_x_unique = True
            x_list = []
            for i in range(1, len(tokens)-2, 2):
                x_list.append(tokens[i])
            for i in range(len(x_list)):
                for j in range(i + 1, len(x_list)):
                    if x_list[i] == x_list[j]:
                        is_x_unique =  False
            if not is_x_unique:
                print("Error: x values must be unique for Lagrange interpolation")
                continue
            result = 0
            x = float(tokens[-1])
            n = len(tokens) // 2 - 1
            for k in range(n):
                basis_k = 1
                for m in range(n):
                    if m == k:
                        continue
                    basis_k *= (x - float(tokens[2*m+1])) / (float(tokens[2*k+1]) - float(tokens[2*m+1]))
                result += float(tokens[2*k+2]) * basis_k
            

        else:
            print("Error: Unsupported expression")
            continue

    except Exception as e:
        print(f"Error: {str(e)}")
        continue # in case of error, skip print(result)

    # Implement common result formatting
    # if the result is an integer, print the result as an integer
    # if the result is not an integer, format the result to 3 decimal places
    try: # result 가 실수가 아닌 경우 건너뛰기(ex -1 ^ 0.5)
        decimals = result - int(result) # 소수부 계산, result가 양수이면 소수부가 0이상으로, 음수이면 소수부가 0이하로 계산된다.
        # result 가 양수인 경우
        if 0 <= decimals < 0.001:
            result = int(result)
        elif decimals > 0.999:
            result = int(result) + 1
        # result 가 음수인 경우
        elif -0.001 < decimals < 0:
            result = int(result)
        elif decimals < -0.999:
            result = int(result) - 1
        else:
            result = f"{result:.3f}"
    except:
        continue

    # Print the formatted result
    print(result)
