import discord
import os  # Maybe necessary at some point.
import shutil

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

import random


def dice(n):
    """Rolls a virtual dice"""
    for i in range(n):
        return random.randint(1, 6)


def random_letter(n):
    """Generates random letters from the latin alphabet"""
    for i in range(n):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        spot = random.randint(0, 25)
        return letters[spot]


def random_chars(n):
    """Same as random_caps but with numbers added"""
    for i in range(n):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
        what_char = random.randint(0, 2)
        if what_char == 0:
            spot = random.randint(0, 25)
            return letters[spot]
        elif what_char == 1:
            spot = random.randint(0, 25)
            return caps[spot]
        else:
            return str(random.randint(0, 9))


def passwd(n):
    """Same as random_caps but with numbers added"""
    for i in range(n):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
        other = ["@", "'", "<", ">", ",", ".", "#", "!", "(", ")", "^", "*", "&", "%", "$", "_", "+"]
        what_char = random.randint(0, 3)
        if what_char == 0:
            spot = random.randint(0, 25)
            return letters[spot]
        elif what_char == 1:
            spot = random.randint(0, 25)
            return caps[spot]
        elif what_char == 2:
            spot = random.randint(0, len(other) - 1)
            return other[spot]
        else:
            return str(random.randint(0, 9))


def random_hex(n):
    """Generates random hexadecimal"""
    for i in range(n):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        what_char = random.randint(0, 1)
        if what_char == 0:
            spot = random.randint(0, 5)
            return letters[spot]
        else:
            return str(random.randint(0, 9))


def coinflip(n):
    """Flips a virtual coin"""
    head = 0
    tails = 0
    for i in range(n):
        side = random.randint(0, 1)
        if side == 0:
            head += 1
        else:
            tails += 1
    return "Flipped " + str(n) + " times, " + str(head) + " times head and " + str(tails) + " times tails."


def random_words(n):
    """Chooses words based on its given dictionary of words. Codename Schizophrenia Generator."""
    words = ['hi', 'good', 'awesome', 'power', 'even', 'urge', 'oh', 'cool', 'pretty', 'very', 'tech', 'i', 'costs',
             'word', 'flipped', 'random', 'head', 'for', 'times', 'what', 'but', 'only', 'nothing', 'panels', 'stove',
             'until', 'better', 'or', 'know', 'history', 'electricity', 'mentality', 'more', 'well', 'hate', 'hell',
             'that', 'drug', 'sounds', 'no', 'am', 'not', 'drink', 'actually', 'damn', 'wine', 'little', 'like', 'you',
             'day', 'wish', 'tired', 'computer', 'math', 'bed', 'eat', 'box', 'wind', 'god', 'car', 'might', 'terror',
             'see', 'chemical', 'attack', 'death', 'murder', 'closet', 'display', 'exile', 'to', 'be', 'execute',
             'worry', 'happy', 'intentions', 'how', 'glass', 'bread', 'bird', 'gun', 'without', 'control', 'blow',
             'function', 'time', 'light', 'sound', 'food', 'days', 'numbers', 'letters', 'english', 'air', 'metal',
             'hard', 'difficult', 'things', 'who', 'cult', 'mental', 'physical', 'hurt', 'why', 'really', 'if',
             'then', 'open', 'caring', 'intimate', 'look', 'lock', 'killing', 'within', 'land', 'country',
             'dont', 'cant', 'about', 'me', 'want', 'this', 'further', 'free', 'democracy', 'terrorism',
             'attacks', 'discord', 'chat', 'sick', 'hospital', 'asylum', 'ruler', 'hatred', 'work', 'house',
             'could', 'card', 'return', 'code', 'card', 'worse', 'tree', 'mountain', 'church', 'mosque', 'help',
             'project', 'snake', 'current', 'briefcase', 'years', 'heat', 'to', 'have', 'a', 'in', 'take', 'people',
             'some', 'them', 'give', 'us', 'because', 'after', 'before', 'there', 'their', 'back', 'temple',
             'shine', 'allure', 'coin', 'economic', 'money', 'school', 'education', 'levels', 'knowledge', 'repeat',
             'abuse', 'police', 'amount', 'list', 'length', 'range', 'radio', 'station', 'shuffle', 'giving', 'disease',
             'reason', 'did', 'do', 'border', 'patrol', 'intelligence', 'plants', 'wood', 'dirt', 'pot', 'intoxicated',
             'synthetic', 'key', 'door', 'window', 'insert', 'home', 'button', 'page', 'paper', 'documents',
             'long', 'mail', 'envelope', 'received', 'tail', 'dog', 'fox', 'owl', 'cat', 'ball', 'clock', 'sticks',
             'wool', 'arrow', 'mirror', 'outside', 'outsiders', 'walled', 'city', 'stray', 'reference', 'transmitter',
             'midnight', 'sentinel', 'factory', 'waste', 'leave', 'bike', 'listen', 'child', 'adult', 'old', 'grave',
             'agree', 'leaf', 'finish', 'vision', 'remote', 'bottle', 'water', 'backpack', 'package', 'glove', 'bat',
             'happiness', 'friends', 'enemies', 'losing', 'positive', 'bright', 'useful', 'furry', 'sticky', 'notes']
    amount_of_words = len(words) - 1  # Don't want to recalculate the number of words each time I update the list.
    # print(len(words))  # Debug step
    for i in range(n):
        what_word = random.randint(0, int(amount_of_words))
        return words[what_word]


@client.event
async def on_ready():
    print(f"logon as {client.user}")
    print("running ver1.1.0-9c80dfb7")
    shutil.copyfile('token.txt', 'token.txt.bak')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hi!! :3')

    if message.content.startswith('$info'):
        await message.channel.send('A bot that does stupid things, $cmds for cmds. Made by NovaCow. '
                                   'Version 1.1.0-9c80dfb7')

    if message.content.startswith('$cmds'):
        await message.channel.send('$hi, $info, $cmds, $tos, $words^, $dice^, $hex^, $passwd^, $chars^, $letters^, '
                                   '$coinflip^. cmds with a ^ at the end require a space and then a whole integer.')

    if message.content.startswith('$tos'):
        await message.channel.send('ToS can be viewed at: https://novacow.ch/bot/tos/, privacy policy (GDPR compliant)'
                                   ' can be viewed at: https://novacow.ch/bot/privacy-policy')

    if message.content.startswith('$words'):  # Allow the usage of random_words within Discord.
        rng = message.content.split(" ", 1)  # Split the message, so we know how many times to do it
        print(len(rng))   # Debug
        try:  # If the user decided to pass a string, will allow passing no string to give a standard amount.
            if 2 > len(rng):  # If the user failed to specify an amount.
                amount = 5  # We set the default to 5, for other functions it might be 1
            else:  # If the user does specify an amount
                amount = int(rng[1])  # This is so that the function we're calling spits out the correct amount.
            for i in range(0, amount):  # Without this, the bot only sends 1 message, so here we account for all messages sent by the function.
                result = random_words(amount)  # Push the result of the function in a variable for easy printing.
                print(result)  # Print it in console, so I can compare the difference between Discord and here.
                await message.channel.send(result)  # Send the message in the Discord chat.
        except TypeError as e:  # Exception handling if the user sent a string.
            await message.channel.send("You didn't specify a number!")  # Notify the user of the mistake.
            print("Oh no! Exception Occurred in $words!! " + str(e))  # Log in console what went wrong.
        except:  # More general exception handling.
            await message.channel.send("Something went wrong, try again later!")  # Tell the user something went wrong.
            print("Oh no! Exception Occurred in $words!!")  # Log in console that something went wrong.
# Comments are the same throughout the file and its various functions, only new functions will be explained.

    if message.content.startswith("$dice"):
        rng = message.content.split(" ", 1)
        print(len(rng))
        try:
            if 2 > len(rng[1]):
                amount = 1
            else:
                amount = int(rng[1])
            for i in range(0, amount):
                result = dice(amount)
                print(result)
                await message.channel.send(str(result))
        except TypeError as e:
            await message.channel.send("You didn't specify a number!")
            print("Oh no! Exception Occurred in $dice!! " + str(e))
        except:
            await message.channel.send("Something went wrong, try again later!")
            print("Oh no! Exception Occurred in $dice!!")

    if message.content.startswith("$hex"):
        rng = message.content.split(" ", 1)
        print(len(rng))
        try:
            if 2 > len(rng[1]):
                amount = 4
            else:
                amount = int(rng[1])
            for i in range(0, amount):
                result = random_hex(amount)
                print(result)
                await message.channel.send(str(result))
        except TypeError as e:
            await message.channel.send("You didn't specify a number!")
            print("Oh no! Exception Occurred in $hex!! " + str(e))
        except:
            await message.channel.send("Something went wrong, try again later!")
            print("Oh no! Exception Occurred in $hex!!")

    if message.content.startswith("$passwd"):
        rng = message.content.split(" ", 1)
        print(len(rng))
        try:
            if 2 > len(rng[1]):
                amount = 8
            else:
                amount = int(rng[1])
            for i in range(0, amount):
                result = passwd(amount)
                print(result)
                await message.channel.send(str(result))
        except TypeError as e:
            await message.channel.send("You didn't specify a number!")
            print("Oh no! Exception Occurred in $passwd!! " + str(e))
        except:
            await message.channel.send("Something went wrong, try again later!")
            print("Oh no! Exception Occurred in $passwd!!")

    if message.content.startswith("$chars"):
        rng = message.content.split(" ", 1)
        print(len(rng))
        try:
            if 2 > len(rng[1]):
                amount = 1
            else:
                amount = int(rng[1])
            for i in range(0, amount):
                result = random_chars(amount)
                print(result)
                await message.channel.send(str(result))
        except TypeError as e:
            await message.channel.send("You didn't specify a number!")
            print("Oh no! Exception Occurred in $chars!! " + str(e))
        except:
            await message.channel.send("Something went wrong, try again later!")
            print("Oh no! Exception Occurred in $chars!!")

    if message.content.startswith("$letters"):
        rng = message.content.split(" ", 1)
        print(len(rng))
        try:
            if 2 > len(rng[1]):
                amount = 1
            else:
                amount = int(rng[1])
            for i in range(0, amount - 1):
                result = random_letter(amount)
                print(result)
                await message.channel.send(str(result))
        except TypeError as e:
            await message.channel.send("You didn't specify a number!")
            print("Oh no! Exception Occurred in $letters!! " + str(e))
        except:
            await message.channel.send("Something went wrong, try again later!")
            print("Oh no! Exception Occurred in $letters!!")

    if message.content.startswith("$coinflip"):
        rng = message.content.split(" ", 1)
        print(len(rng))
        try:
            if 2 > len(rng):
                amount = 1
            else:
                amount = int(rng[1])  # For-loop is not necessary because this function returns as one string.
            result = coinflip(amount)
            print(result)
            await message.channel.send(result)
        except TypeError as e:
            await message.channel.send("You didn't specify a number!")
            print("Oh no! Exception Occurred in $coinflip!! " + str(e))
        except:
            await message.channel.send("Something went wrong, try again later!")
            print("Oh no! Exception Occurred in $coinflip!!")

# Make the token a file, this way I don't expose it within the source. (Rookie mistake)
# And give back-up capabilities.
try:
    token = open('token.txt', 'r')
    content = token.read()
    client.run(content)
except:
    print("WARNING!! Running failed! Assuming token is corrupted. Restoring token, please relaunch!! If this message "
          "continues to appear please generate a new token.txt file with a valid token")
    shutil.copyfile('token.txt.bak', 'token.txt')
