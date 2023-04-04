import random

def picker(ctx):
    options = ctx.message.content.split(' ')
    if len(options) == 2:
        return "You didn't give me any options!"
    if len(options) == 3:
        return options[2] + ' should go first.'
    del options[0:2]
    return random.choice(options) + ' should go first.'