import requests

url = 'https://austinenergy.com/ae/about/environment/renewable-power-generation'

r = requests.get(url)
if r.status_code != 200:
    raise RuntimeError('Could not load page from Austin energy')

main_split_str = "title: 'Total Austin Energy Load/Demand - "
data_datetime = r.text.split(main_split_str)[-1].split("',")[0]
data_datetime = data_datetime.replace(',', '')

new_row = [data_datetime]

for energy_type in ['BIO', 'SOLAR', 'WIND', 'NON-RENEWABLE']:
    type_split_str = f'"load-percent {energy_type}", "'
    energy_pct_str = r.text.split(type_split_str)[-1].split('"', 1)[0]
    energy_fract = float(energy_pct_str)/100
    new_row.append(energy_fract)

print(','.join([str(x) for x in new_row]))