# eml-rename
Python script to rename EML files, in case filename is obfuscated.

## How it works
The code looks inside a directory, `path`, and iterates through each and every one of the EML files, taking in the message subject and the message sender. It then renames the file to `sender + " - " + subject + .eml`, for easy identification and sorting through File Explorer or other means.

## Credit
Credit due to a friend from the [Re:Union Discord server](https://discord.gg/reunion) - a fun place to make new friends and forge long-lasting bonds!