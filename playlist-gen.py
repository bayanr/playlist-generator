# This code is licensed under the WTFPL

# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#        Version 2, December 2004

# Copyright (C) 2004 Bayan Rafeh <bayan.rafeh92@gmail.com>

# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

# 0. You just DO WHAT THE FUCK YOU WANT TO.



import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import time
import sys

previous_timestamp = 0

DBusGMainLoop(set_as_default=True)
loop=gobject.MainLoop()
session = dbus.SessionBus()
metadata_dict = []
count = 0
if len(sys.argv) < 2:
	print "Usage: python playlist_gen.py playlist_name"
	exit(0)
fname = sys.argv[1]
proxy = session.get_object('org.mpris.MediaPlayer2.rhythmbox', '/org/mpris/MediaPlayer2')
player = dbus.Interface(proxy, dbus_interface='org.mpris.MediaPlayer2.Player')
properties_iface = dbus.Interface(proxy, dbus_interface='org.freedesktop.DBus.Properties')

previous_timestamp=time.time()+properties_iface.Get('org.mpris.MediaPlayer2.Player', 'Position')/1000000

metadata = properties_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

def add_track(title, url):
	global metadata_dict
	global count
	global fname
	metadata_dict.append((title,url))
	count = count+1
	f = open(fname, 'w')
	out = '[playlist]\n'
	out = out + 'X-GNOME-Title='+fname.split('/')[-1]+'\n'
	out = out + 'NumberOfEntries='+str(count)+'\n'
	cnt = 0
	for data_tuple in metadata_dict:
		cnt = cnt+1
		out = out + 'File'+str(cnt)+'='+data_tuple[0]+'\n'
		out = out + 'Title'+str(cnt)+'='+data_tuple[1]+'\n'
	f.write(out)
	f.close()
		

def property_change_handler(iface_name, changed_properties, invalidated_properties):
	global previous_timestamp
	global metadata
	global add_track

	for key in changed_properties:
		if key == 'PlaybackStatus':
			status = changed_properties[key]
			if status == 'Playing':
				previous_timestamp = time.time()-properties_iface.Get('org.mpris.MediaPlayer2.Player', 'Position')/1000000
		if key == 'Metadata':
			track_length = metadata['mpris:length']
			track_length = track_length/1000000
			playback_length = time.time()-previous_timestamp
			if playback_length >= 0.80*track_length:
				add_track(metadata['xesam:title'], metadata['xesam:url'])
			metadata = changed_properties[key]
			previous_timestamp = time.time()



properties_iface.connect_to_signal('PropertiesChanged', property_change_handler)

try:
	print 'Starting listener'
	loop.run()
except KeyboardInterrupt:
	print '\rExiting now'
	exit(0)
