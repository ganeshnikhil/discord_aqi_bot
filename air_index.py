#api_key="d59c0346afe9d48c7f26d99ce53f6ec2c3dc53c3"
import requests
from colorama import Fore , Back ,Style
#! program to get air quality index using api requests.

## message 
message=[
   '''Air quality is considered satisfactory, 
   and air pollution poses little or no risk''',
   
   '''Air quality is acceptable; however, for some 
   pollutants there may be a moderate health 
   concern for a very small number of people 
   who are unusually sensitive to air pollution.''',
   
   '''Members of sensitive groups may experience 
   health effects. The general public is not likely 
   to be affected.''',
   
   '''Everyone may begin to experience health 
   effects; members of sensitive groups may 
   experience more serious health effects''',
   
   '''Health warnings of emergency conditions. 
   The entire population is more likely to be affected.''',
      
   '''Health alert: everyone may experience more 
   serious health effects'''
]


def get_air_quality_message(air_quality_index:str) -> None:
   messages = {
      (0, 50): "[+].GOOD.\n"+message[0],
      (51, 100): "[+].Moderate..\n"+message[1],
      (101, 150): "[-].Unhealthy for Sensitive Groups..\n"+message[2],
      (151, 200): "[-].Unhealthy\n"+message[3],
      (201, 300): "[-].Very Unhealthy..\n"+message[4],
      (301, float('inf')): "[+].Hazardous...\n"+message[5],
   }

   for range_limits, msg in messages.items():
      if range_limits[0] <= air_quality_index <= range_limits[1]:
            return msg 
   return "Invalid index"


def get_all_data(country_state):
   api_key = open('api.key', 'r').read()
   url = f"https://api.waqi.info/feed/{country_state}/?token={api_key}"
   data = requests.get(url)
   
   if data.status_code == 200:
      data = data.json()
      air_quality_index=data['data']['aqi']
      lan,lon=data['data']['city']['geo']
      name=data['data']['city']['name']
      msg = get_air_quality_message(air_quality_index)
      all_data= f''' ```ansi\n
{Fore.GREEN}NAME{Fore.RESET} : {Fore.RED}{name}{Fore.RESET}
{Fore.GREEN}QYALITY_INDEX{Fore.RESET}: {Fore.RED}{air_quality_index}{Fore.RESET}
{Fore.GREEN}COORDINATES{Fore.RESET}: {Fore.RED} ({lan} , {lon}){Fore.RESET}
{Fore.GREEN}REPORT{Fore.RESET} :{Fore.CYAN}{msg}{Fore.RESET} \n```
'''
      return all_data
   
   return f''' {country_state} Not found.....'''
   
# india , delhi , mumbai , bihar .
#  api_key = "api_key" you get from url after entering details.
