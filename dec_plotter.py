import ephem
from matplotlib.pyplot import *
import datetime

file_name = "dec_by_date.png"


def plotter(planet_list: [str] = ["Mars"], initial_date: datetime = datetime.date(year=2013, month=1, day=1),
            final_date: datetime = datetime.date.today(), path_to_save: str = None) -> None:
    for planet_name in planet_list:
        planet = eval("ephem.{planet_name}()".format(planet_name=planet_name))
        dec_list = []
        date_list = []
        day = initial_date
        while day < final_date:
            planet.compute(day.strftime("%Y/%m/%D"))
            if len(dec_list) == 0:
                dec_list.append(planet.dec)
                date_list.append(day)
            if planet.dec != dec_list[-1]:
                dec_list.append(planet.dec)
                date_list.append(day)
            day += datetime.timedelta(days=1)
        plot(date_list, dec_list, label=planet_name)
    legend(loc="upper right")
    xlim(initial_date, final_date)
    if path_to_save:
        savefig(path_to_save + file_name)
    else:
        savefig(file_name)
