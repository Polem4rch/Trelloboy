from googlesearch import search
import webbrowser
from random_user_agent.user_agent import UserAgent



word = input( "which word? ")
print ("you chose " + word )
joint = "site:trello.com " + word

query = joint
for j in search(query, tld="com", num=10, stop=None, pause=3): 
   print(j) 
