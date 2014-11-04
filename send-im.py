#!/usr/bin/env python

import sys, pidgin

purple = pidgin.Purple.purple()

try:
	from_username = sys.argv[1]
	to_username = sys.argv[2]
except:
	raise Exception("usage: send.py from_username to_username")


accounts = pidgin.PurpleAccounts(purple)

try:
	matching_account = next(a for a in accounts.get_all() if a.get_username() == from_username);
except StopIteration:
	raise Exception("No account matching %s" % from_username)

conversation = pidgin.PurpleConversation.new(purple,
				pidgin.PURPLE_CONV_TYPE_IM,
				matching_account,
				to_username)

conversation.im().send("Sending you a message!")
