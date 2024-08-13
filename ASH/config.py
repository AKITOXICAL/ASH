import json
import os


def get_user_list(config, key):
    with open('{}/ASH/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    # REQUIRED

    API_ID = 29764570
    API_HASH = "7676192e491329a1b859b2184e5d7823"
    TOKEN = "7048029832:AAHtX9gs9kuNjqhhBUioueMbYSGGoh4ZKLk"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6411059657
    OWNER_USERNAME = "ELITE_GANESH"
    SUPPORT_CHAT = 'E_H_Club'  #Own group for support, do not added the @
    JOIN_LOGGER = -1001801945066  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001801945066  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://rkffvakt:o7mkbX8hS7h5IPhMyPHSteGaWvuDYOp-@surus.db.elephantsql.com/rkffvakt'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "QzhnoxpyhMXwSdpLMk77NUE8OPUJSMAsDMI088IHlPJS~_NenKRX5wbtAyCbCGZc"  
    SPAMWATCH_SUPPORT_CHAT = "@E_H_Support"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAACAgUAAxkBAAIk8Ga7ZiCCRkhuBsT-cwAB09fHpddeWgAC8Q8AAhP7aVdcDFV00iDG_DQE'  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'H1HOGR3MMV2XWIF7' 
    TIME_API_KEY = 'awoo'
    WALL_API = 'awoo'  
    AI_API_KEY = 'awoo'
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
