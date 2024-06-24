import dbus

def artwork():
    bus = dbus.SessionBus()
    try:
        vlc_media_player_obj = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        props_iface = dbus.Interface(vlc_media_player_obj, 'org.freedesktop.DBus.Properties')
        pb_stat = props_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
        return str(pb_stat['mpris:artUrl'])
    except:
        return None
def song():
    bus = dbus.SessionBus()
    try:
        vlc_media_player_obj = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        props_iface = dbus.Interface(vlc_media_player_obj, 'org.freedesktop.DBus.Properties')
        pb_stat = props_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
        return str(pb_stat['xesam:title'])
    except:
        return None

def artist():
    bus = dbus.SessionBus()
    try:
        vlc_media_player_obj = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        props_iface = dbus.Interface(vlc_media_player_obj, 'org.freedesktop.DBus.Properties')
        pb_stat = props_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
        return str(pb_stat['xesam:artist'][0])
    except:
        return None