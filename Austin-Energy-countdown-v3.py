# sweigart-ch17-countdown
import time # subprocess
# from datetime import datetime
import requests
import copy

url = 'https://austinenergy.com/ae/about/environment/renewable-power-generation'

def get_and_process_page(url, data_datetime_saved):
    r = requests.get(url)
    main_split_str = "title: 'Total Austin Energy Load/Demand - "
    data_datetime = r.text.split(main_split_str)[-1].split("',")[0]
    data_datetime = data_datetime.replace(',', '')

    if data_datetime != data_datetime_saved:
        for energy_type in ['BIO', 'SOLAR', 'WIND', 'NON-RENEWABLE']:
            split_and_write_to_file(r, data_datetime, energy_type)

        # overwrite previous value of data_datetime_saved
        data_datetime_saved = copy.copy(data_datetime)
    else:
        pass

    return data_datetime_saved

def split_and_write_to_file(r, data_datetime, energy_type):
    type_split_str = f'"load-percent {energy_type}", "'
    energy_pct_str = r.text.split(type_split_str)[-1].split('"', 1)[0]
    energy_fract = float(energy_pct_str)/100
    print(f"For {energy_type}, fraction: {energy_fract}")
    current_time = time.localtime()
    current_time_str = time.strftime('%Y-%m-%d_%H%M%S', current_time)
    save_str = f"{current_time_str}, {data_datetime}, {energy_type}, {energy_fract}\n"
    with open(save_path + file_name, "a") as file:
        file.writelines(save_str)

data_datetime_saved = '' # initialize

current_time = time.localtime()
current_time_str = time.strftime('%Y-%m-%d_%H%M%S', current_time)
file_name = f"Austin Energy scrapes {current_time_str}.txt"
data_datetime_saved = get_and_process_page(url, data_datetime_saved)
