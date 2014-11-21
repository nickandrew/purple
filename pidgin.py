"""pidgin class for using dbus interface im.pidgin.purple.PurpleInterface
without continual purple.Something calls"""

import dbus

PURPLE_CONV_TYPE_UNKNOWN = 0
PURPLE_CONV_TYPE_IM      = 1
PURPLE_CONV_TYPE_CHAT    = 2
PURPLE_CONV_TYPE_MISC    = 3
PURPLE_CONV_TYPE_ANY     = 4

PURPLE_DISCONNECTED = 0
PURPLE_CONNECTED    = 1
PURPLE_CONNECTING   = 2

PURPLE_CONNECTION_ERROR_NETWORK_ERROR             =  0
PURPLE_CONNECTION_ERROR_INVALID_USERNAME          =  1
PURPLE_CONNECTION_ERROR_AUTHENTICATION_FAILED     =  2
PURPLE_CONNECTION_ERROR_AUTHENTICATION_IMPOSSIBLE =  3
PURPLE_CONNECTION_ERROR_NO_SSL_SUPPORT            =  4
PURPLE_CONNECTION_ERROR_ENCRYPTION_ERROR          =  5
PURPLE_CONNECTION_ERROR_NAME_IN_USE               =  6
PURPLE_CONNECTION_ERROR_INVALID_SETTINGS          =  7
PURPLE_CONNECTION_ERROR_CERT_NOT_PROVIDED         =  8
PURPLE_CONNECTION_ERROR_CERT_UNTRUSTED            =  9
PURPLE_CONNECTION_ERROR_CERT_EXPIRED              = 10
PURPLE_CONNECTION_ERROR_CERT_NOT_ACTIVATED        = 11
PURPLE_CONNECTION_ERROR_CERT_HOSTNAME_MISMATCH    = 12
PURPLE_CONNECTION_ERROR_CERT_FINGERPRINT_MISMATCH = 13
PURPLE_CONNECTION_ERROR_CERT_SELF_SIGNED          = 14
PURPLE_CONNECTION_ERROR_CERT_OTHER_ERROR          = 15
PURPLE_CONNECTION_ERROR_OTHER_ERROR               = 16

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

	def notify_added(self, remote_user, _id, alias, message):
		"Notifies the user that the account was added to a remote user's buddy list."
		return self.purple.PurpleAccountNotifyAdded(self.account, remote_user, _id, alias, message)

	def request_add(self, remote_user, _id, alias, message):
		"""Notifies the user that the account was added to a remote user's buddy list and asks ther user if they want to
		add the remote user to their buddy list."""
		return self.purple.PurpleAccountRequestAdd(self.account, remote_user, _id, alias, message)

	def request_close_with_account(self):
		"Close account requests registered for the given PurpleAccount."
		return self.purple.PurpleAccountRequestCloseWithAccount(self.account)

	def request_change_password(self):
		"Requests information from the user to change the account's password."
		return self.purple.PurpleAccountRequestChangePassword(self.account)

	def request_change_user_info(self):
		"Requests information from the user to change the account's user information."
		return self.purple.PurpleAccountRequestChangeUserInfo(self.account)

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

	def set_buddy_icon_path(self, path):
		"Sets the account's buddy icon path."
		return self.purple.PurpleAccountSetBuddyIconPath(self.account, path)

	def set_protocol_id(self, protocol_id):
		"Sets the account's protocol ID."
		return self.purple.PurpleAccountSetProtocolId(self.account, protocol_id)

	def set_remember_password(self, value):
		"Sets whether or not this account should save its password."
		return self.purple.PurpleAccountSetRememberPassword(self.account, value)

	def set_check_mail(self, value):
		"Sets whether or not this account should check for mail."
		return self.purple.PurpleAccountSetCheckMail(self.account, value)

	def set_enabled(self, ui, value):
		"Sets whether or not this account is enabled for the specified UI."
		return self.purple.PurpleAccountSetEnabled(self.account, ui, value)

	def get_silence_suppression(self):
		"Return whether silence suppression is used during voice call."
		return self.purple.PurpleAccountGetSilenceSuppression(self.account)

	def set_silence_suppression(self, value):
		"Sets whether silence suppression is used during voice call."
		return self.purple.PurpleAccountSetSilenceSuppression(self.account, value)

	def clear_settings(self):
		"Clears all protocol-specific settings on an account."
		return self.purple.PurpleAccountClearSettings(self.account)

	def remove_setting(self, name):
		"Removes an account-specific setting by name."
		return self.purple.PurpleAccountRemoveSetting(self.account, name)

	def set_int(self, name, value):
		"Sets a protocol-specific integer setting for an account."
		return self.purple.PurpleAccountSetInt(self.account, name, value)

	def set_string(self, name, value):
		"Sets a protocol-specific string setting for an account."
		return self.purple.PurpleAccountSetString(self.account, name, value)

	def set_bool(self, name, value):
		"Sets a protocol-specific boolean setting for an account."
		return self.purple.PurpleAccountSetBool(self.account, name, value)

	def is_connected(self):
		"Returns whether or not the account is connected."
		return self.purple.PurpleAccountIsConnected(self.account)

	def is_connecting(self):
		"Returns whether or not the account is connecting."
		return self.purple.PurpleAccountIsConnecting(self.account)

	def is_disconnected(self):
		"Returns whether or not the account is disconnected."
		return self.purple.PurpleAccountIsDisconnected(self.account)

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

	def get_buddy_icon_path(self):
		"Returns the account's buddy icon path."
		return self.purple.PurpleAccountGetBuddyIconPath(self.account)

	def get_protocol_id(self):
		"Returns the account's protocol ID."
		return self.purple.PurpleAccountGetProtocolId(self.account)

	def get_protocol_name(self):
		"Returns the account's protocol name."
		return self.purple.PurpleAccountGetProtocolName(self.account)

	def get_connection(self):
		"Returns the account's connection."
		connection = self.purple.PurpleAccountGetConnection(self.account)
		return PurpleConnection(self.purple, connection)

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
		self.connection = connection

	def is_connected(self):
		"Returns TRUE if the account is connected, otherwise returns FALSE."
		return self.get_state() == PURPLE_CONNECTED

	def destroy(self):
		"Disconnects and destroys a PurpleConnection."
		return self.purple.PurpleConnectionDestroy(self.connection)

	def set_state(self, state):
		"Sets the connection state."
		"state is one of PURPLE_DISCONNECTED, PURPLE_CONNECTED, PURPLE_CONNECTING"
		return self.purple.PurpleConnectionSetState(self.connection, state)

	def get_state(self):
		"Returns the connection state."
		return self.purple.PurpleConnectionGetState(self.connection)

	def get_account(self):
		"Returns the connection's account."
		return PurpleAccount(self.purple, self.purple.PurpleConnectionGetAccount(self.connection))

	def get_password(self):
		"Returns the connection's password."
		return self.purple.PurpleConnectionGetPassword(self.connection)

	def get_display_name(self):
		"Returns the connection's displayed name."
		return self.purple.PurpleConnectionGetDisplayName(self.connection)

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
