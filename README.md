# austin-energy-mix
Scraping Austin Energy data on the energy mix every 10 minutes


#### Install and run
- pip install -r requirements.txt


#### Troubleshooting

* Error = `UNSAFE_LEGACY_RENEGOTIATION_DISABLED`
  - Solution - downgraded openssl to 1.1.1o (`conda install openssl=1.1.1o`)