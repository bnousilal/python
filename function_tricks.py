def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


def big(n1, n2):
  return ([n1, n2][(n2>n1)])
    
print(dispatch_if('mul', 2, 8))
print(dispatch_dict('mul', 2, 8))
print(dispatch_if('unknown', 2, 8))
print(dispatch_dict('unknown', 2, 8))

print(big(3, 6))
