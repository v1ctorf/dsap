def get_list_integers():
    done = False
    int_list = []

    while not done:
        n = input('Enter an integer number (blank if done): ')

        if n == '':
            done = True
        else:
            int_list.append(int(n))
            print('List = {0}'.format(int_list))

    return int_list
