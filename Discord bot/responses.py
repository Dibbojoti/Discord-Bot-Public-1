import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"

    if p_message == 'oi':
        return str(random.randint(1, 6))

    if p_message == 'give me some facts':
        r = random.randint(1,6)
        if r == 1:
            return 'Jews did 9/11'
        if r == 2:
            return 'Its Holohoax'
        if r ==3 :
            return 'Hitler was right'
        if r==4 :
            return 'Zelensky blew up nordstream'
        if r==5 : 
            return 'Jews control the Fed'
        else:
            return 'You Anti-Semite Crap'

    #  return 'Yeah, I don\'t know. Try typing "!help".'    