class Config(object):
	LOGGER = True
	
	# Must be filled
	api_id = 123456
	api_hash = "123456789abcdefghijklmnopqrstuvw"

	# Let it default, unless you understand what to do
	BOT_SESSION = "religram/session/main"
	BOT_VERSION = "0.1"
	app_version = "💝 Religram v{}".format(BOT_VERSION)
	device_model = "PC"
	system_version = "Linux"
	lang_code = "en"
	WORKERS = 4

	# Optional to change
	COMMAND = ["/", "!"]

	# If you fill the whitelist, bot will response to the whitelist only, else bot will response to anyone
	# Fill it with your Telegram UserID
	WHITELIST_USERS = []

	# Fill this if you are using real bot, fill blank if you using user bot
	BOT_TOKEN = ""

	# Fill the LOAD_PLUGINS will loaded whitelist only
	# And NOLOAD_PLUGINS will do not load that plugins
	# Not filling that will load all plugins
	LOAD_PLUGINS = []
	NOLOAD_PLUGINS = []

	# Fill True will have more debug output
	IS_DEVELOPMENT = True

	# Fill True and bot will running on test server, best for testing something
	IS_TEST_MODE = False

