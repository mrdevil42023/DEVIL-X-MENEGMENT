# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 21436816  # Get this value from my.telegram.org/apps
    API_HASH = "c269918dddddbc041d536207cab72155"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ierjlkr:OG4dxzO67Zret3Zii43Hhvujkg89WVry0n9KsHE@karma.db.elephantsql.com/ierjlkr"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1001629811868
    MESSAGE_DUMP = -1001629811868

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Mrdevil:Mrdevil@devil.fhl8fbl.mongodb.net/?retryWrites=true&w=majority&appName=Devil"

    # Support chat and support ID
    SUPPORT_CHAT = "devilbotsupport"
    SUPPORT_ID = -1002025625952

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7018144447:AAF0MNLx3cyWSGvoS63hBc0O4QUO5FGhlTw"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6107980637
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
