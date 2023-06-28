def print_all_hard(all_routes):
    try:
        print(f"\nСоставные маршруты {all_routes[0][2].A} -> {all_routes[0][-1].B}:")
        for numb, routes in enumerate(all_routes):
            print(f"\nМаршрут номер {numb + 1}")
            print(f'Время в пути {routes[0]}')
            print(f'Общая стоимость поездки {routes[1]} руб.')
            for i, rout in enumerate(routes[2:]):
                print(i + 1, end='. ')
                rout.print_inf()
    except:
        print("\nМаршруты с пересадками не найдены")


def print_all_simply(all_routes):
    try:
        print(f"\nПрямые маршруты {all_routes[0].A} -> {all_routes[0].B}:")
        for i, root in enumerate(all_routes):
            print('\n', i + 1, end='. ')
            root.print_inf()
    except:
        print("\nПрямых маршрутов не найдено")


class lst_routes(object):

    def __init__(self, df):
        self.df = df

    def search(self, point):
        for i in self.df:
            if i.A == point:
                return i
        return None

    def hard_rout(self, point_a, point_b):
        all_routes = []
        for now_trip in self.df:
            if now_trip.A == point_a and now_trip.B != point_b:
                route = [0, now_trip.price, now_trip]
                while True:
                    search_trip = lst_routes.search(self, now_trip.B)
                    if search_trip and (search_trip.date_A - now_trip.date_B).total_seconds() >= 10800:
                        route.append(search_trip)
                        route[1] += search_trip.price
                        if search_trip.B == point_b:
                            break
                    else:
                        route = []
                        break
                    now_trip = search_trip
                if route:
                    route[0] = route[-1].date_B - route[2].date_A
                    all_routes.append(route)
        return all_routes

    def light_rout(self, point_a, point_b):
        all_routes = []
        for i in self.df:
            if i.A == point_a and i.B == point_b:
                all_routes.append(i)
        return all_routes
