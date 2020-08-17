age =-1

while age <= 0:
    try:
        age = int(input('Digite sua idade em anos: '))

        if age <= 0:
            print('Digite um numero positivo!')
    except ValueError:
        print('Invalid age spec')
        raise
    except EOFError:
        print('unexpected error!')
    finally:
        print('adieu')
        
