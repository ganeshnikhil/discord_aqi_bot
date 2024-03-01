import random 
import air_index 
from colorama import Fore
import colorama 
colorama.init(autoreset=True)

greeting = ['good morning' , 'good evening' , 'good night']
def handle_response(message , name) -> str:
   p_message = message.lower()
   
   if p_message == 'jarvis':
      return f'```ansi\n {Fore.CYAN}How can i help you {name}\n```'
   
   if p_message == 'hello':
      return f'Hey there {name}'
   
   if result := [greet for greet in greeting if greet in p_message]:
      return f"{' '.join(result).upper()} {name} "
      
   if p_message in ['good morning' , 'good evening' , 'good night']:
      return p_message.upper()
   
   if  p_message == 'roll':
      return str(random.randint(1,6))
   
   # return report of air quality index 
   if p_message.startswith('$'):
      name = p_message[1:].lower().strip()
      return air_index.get_all_data(name)
   
   if p_message == '!help':
      helper='''
```
# roll -- random no generated 
# $country_state_name -- air qualtiy index report 
``` '''
      return helper 
   
   



