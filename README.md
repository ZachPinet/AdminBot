# This is AdminBot, a multi-purpose Discord bot.

## Features

- Set a custom command prefix unique to the server.
- Use commands with the prefix, or by mentioning the bot.
- Set a custom message to welcome new members when they join the server.
- Set which channel these messages are sent to.
- Toggle the sending of these messages on or off.

## List of Commands

### Miscellaneous Commands:

- **help [h]**: Sends a list of commands.
- **ping [p]**: Sends the bot latency in milliseconds.
- **checkserver [cs]**: Sends all stored information about the server.
- **setprefix [sp] (prefix)**: Sets the given prefix as the new server prefix.

### Welcome Commands:

- **welcomeon [welcon, won]**: Enables welcome messages on the server.
- **welcomeoff [welcoff, woff]**: Disables welcome messages on the server.
- **setwelcome [setwelc, sw] (message)**: Sets a new custom welcome message. 
  - Writing '[mention]' will mention the new user.
  - Writing '[server]' will send the name of the server.
  - Writing '[CHANNEL_ID_HERE]' will link to the specified channel ID.
- **viewwelcome [viewwelc, vw]**: Sends a preview of the current welcome message. '[mention'] will mention the command user.
- **setwelcomechannel [swc] (channel_id)**: If a valid channel ID is provided, then that channel will receive all future welcome messages.
