try:

    begin = int(input("begin->"))
    end = int(input("end->"))

    for i in range(begin, end+1):
        print(i, end='\t')

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
