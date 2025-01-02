import pandas
data=pandas.read_csv('weather_data.csv')
temp_list=data['temp'].to_list()
mon=data[data['day']=='Monday']
mon_temp=(((mon.temp*9)/5)+32)
print(mon_temp)