### Fial Project number 1

"""
Build an Arithmetic Formatter Project

Students in primary school often arrange arithmetic problems vertically 
to make them easier to solve. For example, "235 + 52" becomes:
Example Code

  235
+  52
-----

Finish the arithmetic_arranger function that receives a list of strings which are 
arithmetic problems, and returns the problems arranged vertically and side-by-side. 
The function should optionally take a second argument. 
When the second argument is set to True, the answers should be displayed.
Example

Function Call:
Example Code

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:
Example Code

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

Function Call:
Example Code

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:
Example Code

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

    Situations that will return an error:
        If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
        The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
        Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
        Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
    If the user supplied the correct format of problems, the conversion you return will follow these rules:
        There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
        Numbers should be right-aligned.
        There should be four spaces between each problem.
        There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

Note: open the browser console with F12 to see a more verbose output of the tests.


"""

def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return 'Error: Too many problems.'

    numbers = '1234567890'
    all_signs ='+-*/'
    signs ='+-'
    space = ' '
    skip = '    '
    line_one , line_two, line_three, line_four = '','','',''
    for problem in problems:
        first_number = []
        second_number = []
        sign = []
        for char in problem:
            if char not in (numbers + all_signs + space):
                return ('Error: Numbers must only contain digits.' )
            elif char in numbers and not sign:
                first_number.append(char)
            elif char in numbers and sign:
                second_number.append(char)
            elif char in all_signs:
                if char in signs:
                    sign = char
                else:
                    return "Error: Operator must be '+' or '-'."

        max_len = max(len(first_number),len(second_number))
        if max_len > 4 :
            return 'Error: Numbers cannot be more than four digits.'

        bar_len = 2+max_len
        bar = '-'* bar_len
        if sign == '+':
            result = int(''.join(first_number)) + int(''.join(second_number))
        elif sign == '-':
            result = int(''.join(first_number)) - int(''.join(second_number))

        # fix len of numbers
        first_number = ' '*(bar_len-len(first_number))+''.join(first_number)
        second_number = sign+' '*(bar_len-1-len(second_number))+''.join(second_number)
        result = ' ' * (bar_len - len(str(result))) + str(result)

        # concat skips
        line_one +=  first_number + skip
        line_two += second_number + skip
        line_three += bar + skip
        line_four += result + skip


    if show_answers : 
        final_result = line_one[:-4] + '\n' + line_two[:-4] + '\n' + line_three[:-4] + '\n' + line_four[:-4]
    else:
        final_result = line_one[:-4] + '\n' + line_two[:-4] + '\n' + line_three[:-4] 

    return final_result


print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
