import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    # clear the screen
    clear()

    # put hmtl content for the fun fact generator header
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    # url from where we will fetch the data 
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    # use GET request 
    response = requests.get(url)

    # load the request in json file 
    data = json.loads(response.text)

    # we will need 'text' from the data 
    useless_fact = data['text']

    # put the fact in blue color and increase the font size 
    style(put_text(useless_fact), 'color: blue; font_size: 30px')

    # put the "click me" button 
    put_buttons(
        [dict(label='Click Me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

# Driver Function 
if __name__ == '__main__':
    # put a heading "Fun Fact Generator"
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    # Hold the session for a long time and put the "Click Me" button 
    put_buttons(
        [dict(label='Click Me', value='outline-success', clolo='outline-success')],
        onclick=get_fun_fact
    )

    hold()