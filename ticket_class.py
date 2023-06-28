from datetime import datetime


class ticket(object):
    def __init__(self, ticket_new):
        self.type_trans = ticket_new[0].strip()
        self.A = ticket_new[1].strip()
        self.B = ticket_new[2].strip()
        time = ticket_new[9].strip().split(':')
        self.date_A = datetime(*[int(j) for j in ticket_new[3:6]][::-1], int(time[0]), int(time[1]))
        time = ticket_new[10].strip().split(':')
        self.date_B = datetime(*[int(j) for j in ticket_new[6:9]][::-1], int(time[0]), int(time[1]))
        self.way = ticket_new[11]
        self.carrier = ticket_new[12]
        self.price = int(ticket_new[13])

    def print_inf(self):
        print(f'Билет на {self.type_trans}')
        print(f'{self.A} -> {self.B} от компании {self.carrier}')
        print(f'Отбытие {self.date_A.date().day}.{self.date_A.date().month}.{self.date_A.date().year} в'
              f' {self.date_A.time().hour}:{self.date_A.time().minute}')
        print(f'Прибытие {self.date_B.date().day}.{self.date_B.date().month}.{self.date_B.date().year} в'
              f' {self.date_B.time().hour}:{self.date_B.time().minute}')
        print(f'Путь займет {self.way}')
        print(f'Цена - {self.price} руб.')
