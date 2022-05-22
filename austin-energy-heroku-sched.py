import time
import requests

url = 'https://austinenergy.com/ae/about/environment/renewable-power-generation'

def get_and_process_page(url):
    r = requests.get(url)
    main_split_str = "title: 'Total Austin Energy Load/Demand - "
    data_datetime = r.text.split(main_split_str)[-1].split("',")[0]
    data_datetime = data_datetime.replace(',', '')

    for energy_type in ['BIO', 'SOLAR', 'WIND', 'NON-RENEWABLE']:
        split_and_write_to_file(r, data_datetime, energy_type)

    # TO DO: after iterating through the energy_type values,
    # then export the data (e.g., to a GitHub file or Postgres db)

def split_and_write_to_file(r, data_datetime, energy_type):
    type_split_str = f'"load-percent {energy_type}", "'
    energy_pct_str = r.text.split(type_split_str)[-1].split('"', 1)[0]
    energy_fract = float(energy_pct_str)/100
    print(f"For {energy_type}, fraction: {energy_fract}")
    current_time = time.localtime()
    current_time_str = time.strftime('%Y-%m-%d_%H%M%S', current_time)
    save_str = f"{current_time_str}, {data_datetime}, {energy_type}, {energy_fract}\n"
    # TO DO: figure out how to save the data to GitHub or the Postgres db
    # with open(save_path + file_name, "a") as file:
    #     file.writelines(save_str)

current_time = time.localtime()
current_time_str = time.strftime('%Y-%m-%d_%H%M%S', current_time)
file_name = f"Austin Energy scrapes {current_time_str}.txt"

get_and_process_page(url)
