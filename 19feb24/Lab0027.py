var = input('enter the age out of the following <5,<18,>18,>60\n')
match var:
    case '<5':
        print ('child')
    case "<18":
        print ('adolocent')
    case ">18":
        print('Adult')
    case ">60":
        print('senoir')
    case _:
        print('no idea')