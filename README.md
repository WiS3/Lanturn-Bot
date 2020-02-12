# Lanturn Bot Public Source Code

This project has been forked from https://gitlab.com/fishguy6564/lanturn-bot-public-source-code.

Thanks to https://gitlab.com/fishguy6564 for the initial work.


A Pokemon Sword and Shield raid and seed
finding discord bot programmed and designed
by fishguy6564. Credits to algorithms used
and help received below. 

**Credit:**

Used algorithms and documentation from various Pokemon hackers
such as Admiral-Fish and zaksabeast

olliz0r for the sys-botbase sysmodule

**Prerequisites:**

The ability to connect to your switch requires a hacked switch and stable internet connection
and sys-botbase installed. You can download sys-botbase [here](https://github.com/olliz0r/sys-botbase)

Please use by installing python3. 

You must have the latest discord python api installed

Use pip commands to install the following:

pip install z3-solver

**Current Features:**

$GetSeed - Gets a user's seed and next square/star shiny frame
by a user passing their encryption constant, pid, and IVs as arguments.

$GetFrameData - Gets a user's next square/star shiny frame by a
user passing their already generated seed as an argument.

$CheckMySeed - Queues up the invoker and initiates the Dudu Clone modules.
It communicates to the DuduClient script via the communicate.bin file. Please
do not trash any files when downloading them.

$greet - Sends a cute message depending on what the developer sets it to.

$CheckQueueSize - Reports the amount of people currently in the queue

$CheckMyPlace - Reports the current position of the sender in the queue system

$logout - For the admin only. Will turn off the bot for testing.

**How to Run**

You may be wondering how to run this. As for the switch side of things, you
must already have a cfw installed, preferrably atmosphere. Olliz0r has 
instructions on how to setup sys-botbase in the readme of his github page.
Please check DuduClient.py, bot.py, and RaidCommands.py for comments on what
needs to be filled in. Once all of that is done, double click run.bat and if
all goes well, DuduClient should shoot out a message saying "Awaiting... Inputs" 
if successfully connected to your switch. bot.py should show a message that 
prints out your basic discord info.

Want to see it in action? Check out the demo video [here](https://www.youtube.com/watch?v=yDIYqYmnV3Y)

**Important things to note**
- This is calibrated for Pokemon Sword and Shield in English. Other languages
may have more dialogue in certain parts and will need to be recalibrated.
- Text speed must be set to the fastest setting in order to keep the timing of
the button inputs from the dudu client.
- Using a modded switch online CAN get you banned. I am not responsible if you
somehow do get banned. You use this at your own risk.

**Questions?**

If you have any questions, please contact me on discord. I will be more than
happy to help troubleshoot any problems. My discord is: fishguy6564#1228

**Known Bugs**
- None for now. Report any to my discord.

**Planned Features:**
- Dump .pk8 file from offered pokemon from trade and send it via discord.
- Check a offered Pokemon's IVs.
- Check egg status
