from tours.tour_data import departures, title

def code_base(request):

    return {
        "title": title,
        "departures": departures,  # места отправления для формирования меню
    }