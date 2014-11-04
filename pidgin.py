"""pidgin class for using dbus interface im.pidgin.purple.PurpleInterface
without continual purple.Something calls"""

import dbus

PURPLE_CONV_TYPE_UNKNOWN = 0
PURPLE_CONV_TYPE_IM = 1
PURPLE_CONV_TYPE_CHAT = 2
PURPLE_CONV_TYPE_MISC = 2
PURPLE_CONV_TYPE_ANY = 2

class Purple:
	@staticmethod
	def purple():
		"Return the 'purple' object which is our connection to dbus"
		bus = dbus.SessionBus()
		obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
		purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")
		return purple


class PurpleAccount:
	"A PurpleAccount connects to a server"
	def __init__(self, purple, account):
		self.purple = purple
		self.account = account

	def destroy(self):
		"Destroys an account."
		return self.purple.PurpleAccountDestroy(self.account)
	
	def connect(self):
		"Connects to an account."
		return self.purple.PurpleAccountConnect(self.account)
	
	def register(self):
		"Registers an account."
		return self.purple.PurpleAccountRegister(self.account)

	def unregister(self, cb, user_data):
		"Unregisters an account (deleting it from the server)."
		return self.purple.PurpleAccountUnregister(self.account, cb, user_data)
	
	def disconnect(self):
		"Disconnects from an account."
		return self.purple.PurpleAccountDisconnect(self.account)

	def set_username(self, username):
		"Sets the account's username."
		return self.purple.PurpleAccountSetUsername(self.account, username)

	def set_password(self, password):
		"Sets the account's password."
		return self.purple.PurpleAccountSetPassword(self.account, password)

	def set_alias(self, alias):
		"Sets the account's alias."
		return self.purple.PurpleAccountSetAlias(self.account, alias)

	def set_user_info(self, user_info):
		"Sets the account's user information."
		return self.purple.PurpleAccountSetUserInfo(self.account, user_info)

	def is_connected(self):
		"Returns whether or not the account is connected."
		return self.purple.PurpleAccountIsConnected(self.account)

	def get_username(self):
		"Returns the account's username."
		return self.purple.PurpleAccountGetUsername(self.account)

	def get_password(self):
		"Returns the account's password."
		return self.purple.PurpleAccountGetPassword(self.account)

	def get_alias(self):
		"Returns the account's alias."
		return self.purple.PurpleAccountGetAlias(self.account)

	def get_user_info(self):
		"Returns the account's user information."
		return self.purple.PurpleAccountGetUserInfo(self.account)

	def get_protocol_id(self):
		"Returns the account's protocol ID."
		return self.purple.PurpleAccountGetProtocolId(self.account)

	def get_protocol_name(self):
		"Returns the account's protocol name."
		return self.purple.PurpleAccountGetProtocolName(self.account)

class PurpleAccounts:
	def __init__(self, purple):
		self.purple = purple

	def get_all(self):
		"Retrieve a list of PurpleAccount"
		array = self.purple.PurpleAccountsGetAll()
		return [ PurpleAccount(self.purple, int(n)) for n in array ];

	def find(self, name, protocol_id):
		"Finds an account with the specified name and protocol id."
		a = self.purple.PurpleAccountsFind(name, protocol_id)
		if a == 0: return None
		return PurpleAccount(self.purple, a)

class PurpleConnection:
	def __init__(self, purple, connection):
		self.purple = purple
		self.account = account

class PurpleConversation:
	"A PurpleConversation is akin to an open chat window"

	def __init__(self, purple, conv):
		self.purple = purple
		self.conv = conv

	@staticmethod
	def new(purple, conv_type, account, name):
		"Creates a new conversation of the specified type."
		conv = purple.PurpleConversationNew(conv_type, account.account, name)
		if conv == 0: return None
		return PurpleConversation(purple, conv)

	def destroy(self):
		"Destroys the specified conversation and removes it from the parent window."
		return self.purple.PurpleConversationDestroy(self.conv)

	def present(self):
		"Present a conversation to the user."
		return self.purple.PurpleConversationPresent(self.conv)

	def get_type(self):
		"Returns the specified conversation's type."
		return self.purple.PurpleConversationGetType(self.conv)

	def set_ui_ops(self,ops):
		"Sets the specified conversation's UI operations structure."
		return self.purple.PurpleConversationSetUiOps(self.conv, ops)
	
	def get_ui_ops(self):
		"Returns the specified conversation's UI operations structure."
		return self.purple.PurpleConversationGetUiOps(self.conv)

	def set_account(self, account):
		"Sets the specified conversation's purple_account"
		return self.purple.PurpleConversationSetAccount(self.conv, account)
	
	def get_account(self):
		"Returns the specied conversation's purple_account"
		return PurpleAccount(self.purple, self.purple.PurpleConversationGetAccount(self.conv))

	def name(self):
		"Returns the name of this conversation."
		return self.purple.PurpleConversationGetName(self.conv)

	def im(self):
		"Return an instance of PurpleConvIm for this conversation"
		return PurpleConvIm(self.purple, self.purple.PurpleConvIm(self.conv))

class PurpleConvIm:
	def __init__(self, purple, im):
		self.purple = purple
		self.im = im

	def send(self, message):
		"Send an Instant Message."
		return self.purple.PurpleConvImSend(self.im, message)
