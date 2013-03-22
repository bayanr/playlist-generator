ABOUT THIS PROGRAM

This program is basically a lazy way to generate a playlist in
rhythmbox. What it does is skip over the music you skip over,
and add only the music you listen to all the way to the end.

HOW TO USE

1. Open rhythmbox and hit play.
2. Open a terminal.
3. Navigate to the folder containing playlist-gen.py, so if it's in /home/user/shikaka type in 'cd /home/user/shikaka' without quotes
4. start the script with 'python playlist-gen.py name-of-your-playlist.pls'
5. just listen to your music, skip the songs you don't want and this program will do the rest :)
6. Every time the list is updated, the file will be updated so just check the playlist name you gave it 

The timer stops when you pause, and resumes when you hit play

If you don't use rhythmbox, simply open the playlist-gen.py file, go to the line where it says org.mpris.Player.rhythmbox and change rhythmbox to whatever music player you want.

I know for a fact, guayadeque, banshee and amarok work with this script.

This script is unfinished; I threw it together in a couple of hours but it works. I still need to clean up the code and make it user friendly, so consider it still under development.

Questions you're probably not asking yourself:

Why not just make it a plugin?

Right now I'm just sanding off the rough edges, and this way it won't need any major modification to work with different media players. I will make it into a plugin eventually, but this way you won't be bound to a single media player.

I'll think of more later.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
	Version 2, December 2004

Copyright (C) 2013 Bayan Rafeh <bayan.rafeh92@gmail.com>
Everyone is permitted to copy and distribute verbatim or modifiedcopies of this license document, and changing it is allowed as longas the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSETERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
