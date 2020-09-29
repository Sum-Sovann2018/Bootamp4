

def fun_calc(num1,num2,operator):

   if operator == "*":
       result = num1 * num2
   elif operator == "-":
       result = num1 - num2
   elif operator == "+":
       result = num1 + num2
   else:
       result = num1 / num2

   return f"fun_calc({num1},{num2},'{operator}')\nProduct:{result}\nProcess:{num1}{operator}{num2}={result}"

print(fun_calc(50, 2, '*'))