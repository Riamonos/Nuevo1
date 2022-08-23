
def message(_message):
    print('--- ' + _message + ' ---')


def init_sale():
    message('Seleccionar gominolas')



if __name__ == '__main__':
    message('Hola, soy tu máquina de gominola <3')
    is_admin = bool(input('admin?'))    # Cuando es 0 usuario, 1 es admin
    if is_admin == '1212':
        pass
    elif not is_admin:
        init_sale()
