import random

def picker(ctx):
    options = ctx.message.content.split(' ')
    if len(options) == 2:
        return "You didn't give me any options!"
    if len(options) == 3:
        return 'You should pick ' + options[2]
    del options[0:2]
    return 'You should pick ' + random.choice(options) + '.' 