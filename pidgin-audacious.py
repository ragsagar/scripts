#!/usr/bin/python

# Execute this script repeatedly using watch command in every 30 second or so to set the 
# status of pidgin client as the title of song playing in audacious.

import dbus


def set_message(message):
    # Get current status type (Available/Away/etc.)
    current = purple.PurpleSavedstatusGetType(purple.PurpleSavedstatusGetCurrent())
    # Create new transient status and activate it
    status = purple.PurpleSavedstatusNew("", current)
    msg="Now Playing: "
    emsg=msg+message
    purple.PurpleSavedstatusSetMessage(status, emsg)
    purple.PurpleSavedstatusActivate(status)


session_bus=dbus.SessionBus()
proxy = session_bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(proxy, "im.pidgin.purple.PurpleInterface")
proxy1 = session_bus.get_object('org.mpris.audacious','/TrackList')
purple1 = dbus.Interface(proxy1,'org.freedesktop.MediaPlayer')
ct = purple1.GetCurrentTrack()
proxy2 = session_bus.get_object('org.mpris.audacious','/org/atheme/audacious')
purple2 = dbus.Interface(proxy2,'org.atheme.audacious')
currentsong = purple2.SongTitle(ct)
print currentsong
set_message(currentsong)
