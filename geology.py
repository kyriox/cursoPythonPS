def tipo_de_roca(rock_name):      
    if rock_name in ['basalto', 'granito']: 
        rock_type = 'ígneo'
    elif rock_name in ['arenisca', 'esquista']: 
        rock_type = 'sedimentaria'
    else:
        rock_type = 'metamorfica'
    return rock_type
    print('el tipo de la roca es:', rock_type)
    
def is_rock(r):
    return r in ["basalt","granite","sandstone","shale"]

if __name__=="__main__":
    tests=[["basalt",True],["granite",True],
           ["grass",False],["sugar",False]]
    for r,v in tests:
        if v==is_rock(r):
            print("Pass")
    