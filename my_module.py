print('Imported my_module...')

test = 'Test String'

def find_index(to_search,target):
    '''Fin the index of a value in a sequence'''
    for i,val in enumerate(to_search):
        if target==val:
            return i
    return -1 