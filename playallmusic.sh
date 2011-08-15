mount /dev/sda6
setsid find /media/sda6/  -iname  *.mp3  -exec mplayer -nocache -af volnorm -shuffle -loop 0 '{}' +
