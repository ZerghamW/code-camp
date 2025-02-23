def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    tops = []
    bottoms = []
    dashes = []
    results = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        first, op, second = parts
        
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        max_length = max(len(first), len(second))
        width = max_length + 2
        
        top = first.rjust(width)
        tops.append(top)
        
        bottom = op + ' ' + second.rjust(max_length)
        bottoms.append(bottom)
        
        dashes.append('-' * width)
        
        if show_answers:
            first_num = int(first)
            second_num = int(second)
            result = first_num + second_num if op == '+' else first_num - second_num
            results.append(str(result).rjust(width))
    
    arranged_problems = '    '.join(tops) + '\n' + '    '.join(bottoms) + '\n' + '    '.join(dashes)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)
    
    return arranged_problems