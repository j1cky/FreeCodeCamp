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
                return ('Error: Numbers must only contain digits.'  )    
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
