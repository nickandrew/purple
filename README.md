# Controlling Pidgin/Purple through DBus

This library is an object-oriented interface to controlling the Pidgin Instant Messaging client
(or Purple, which is Pidgin's messaging framework) through DBus.

It is based on instructions found in the Pidgin documentation: https://developer.pidgin.im/wiki/DbusHowto

The python code in that document is quite unwieldy to use as it's not at all object-oriented
and there are a huge number of functions. In this library I've attempted to structure it into
several classes (_PurpleAccount_, _PurpleConversation_ etc) each including the methods relevant
to that class.

## Example

```python
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
```

## Contributing

This is very much a work in progress. There are a large number of functions defined in the Pidgin
docs:

  * https://developer.pidgin.im/doxygen/dev2.x.y/html/account_8h.html
  * https://developer.pidgin.im/doxygen/dev2.x.y/html/blist_8h.html
  * https://developer.pidgin.im/doxygen/dev2.x.y/html/savedstatuses_8h.html
  * https://developer.pidgin.im/doxygen/dev2.x.y/html/conversation_8h.html
  * https://developer.pidgin.im/doxygen/dev2.x.y/html/prefs_8h.html

I haven't even implemented all the classes, let alone all the functions. But the functions themselves
are pretty direct translations from the documentation, so adding more is just a matter of effort.

In other words, *please send me pull requests to help complete this library*.
