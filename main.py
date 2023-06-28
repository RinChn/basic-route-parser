from ticket_class import *
from list_tckt_class import *

if __name__ == "__main__":
    with open('спб-барнаул2.csv') as file:
        df = [i.strip().split('\t') for i in file.readlines()[1:]]

    new_df = []
    for i in df:
        new_df.append(ticket(i))
    new_df = lst_routes(new_df)

    str_A = input('Откуда: ')
    str_B = input('Куда: ')

    hard = new_df.hard_rout(str_A, str_B)
    simply = new_df.light_rout(str_A, str_B)

    print_all_hard(hard)
    print_all_simply(simply)