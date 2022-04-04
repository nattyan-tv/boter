# BOTER
Discord like Bot Client

# Usage
1. first, create a `setting.json` file by referring to `temp.setting.json`.  
It is possible to save multiple TOKEN.  
You can also enter `ja` in the `language` field to make it Japanese.

2. Run `main.py` and select TOKEN.

3. after login, select `Guild` and `Channel`.

4. type your message and press enter to send it.

To re-select Guild/Channel again, type `/change`.  
Another way to get a list of commands is to type `/help`.  
Also, if you want to send a message containing a slash at the beginning, you can use two initial slashes to send the message starting with the second character.  
- Example
```
[/help - Show Help]
・Send a message to #Channel as TestBot@1234
/help

BOTER - Help

/help - Show this help
/exit - Logout client
/change - Change guild/channel
/load - Reload message history

[/help - Show Help]
・Send a message to #Channel as TestBot@1234
//<-This is slash!
# TestBot@1234 04/01 12:34(UTC)
/<-This is slash!

[/help - Show Help]
・Send a message to #Channel as TestBot@1234
```

