#! /usr/bin/pythonCACHE_TTL = 60#UPDATE_LIBRARY_INTERVAL = 4*60*60if __name__ == "__main__":    import xml.etree.ElementTree as ET    tree = ET.parse('resources/settings.xml')    ids = filter(None, [item.get('id') for item in tree.findall('.//setting')])    content = []    with open(__file__, "r") as me:        content = me.read().splitlines()        content = content[:content.index("#GENERATED")+1]    with open(__file__, 'w') as f:        f.writelines(content)        for _id in ids:            line = "SETTING_{0} = \"{1}\"\n".format(_id.upper(), _id)            f.write(line)    #GENERATEDSETTING_LIBRARY_UPDATES = "library_updates"
SETTING_LIBRARY_SET_DATE = "library_set_date"
SETTING_LIBRARY_SYNC_COLLECTION = "library_sync_collection"
SETTING_LIBRARY_SYNC_COLLECTION_TWOWAY = "library_sync_collection_twoway"
SETTING_LIBRARY_SYNC_WATCHLIST = "library_sync_watchlist"
SETTING_LIBRARY_SYNC_WATCHLIST_TWOWAY = "library_sync_watchlist_twoway"
SETTING_UPDATE_LIBRARY_INTERVAL = "update_library_interval"
SETTING_AIRED_UNKNOWN = "aired_unknown"
SETTING_LIBRARY_TAGS = "library_tags"
SETTING_AIRDATE_OFFSET = "airdate_offset"
SETTING_INCLUDE_SPECIALS = "include_specials"
SETTING_TOTAL_SETUP_DONE = "total_setup_done"
SETTING_PLAYERS_UPDATE_URL = "players_update_url"
SETTING_TRAKT_ACCESS_TOKEN = "trakt_access_token"
SETTING_TRAKT_REFRESH_TOKEN = "trakt_refresh_token"
SETTING_TRAKT_EXPIRES_AT = "trakt_expires_at"
SETTING_MOVIES_ENABLED_PLAYERS = "movies_enabled_players"
SETTING_MOVIES_DEFAULT_PLAYER = "movies_default_player"
SETTING_MOVIES_DEFAULT_PLAYER_FROM_LIBRARY = "movies_default_player_from_library"
SETTING_MOVIES_DEFAULT_PLAYER_FROM_CONTEXT = "movies_default_player_from_context"
SETTING_MOVIES_LIBRARY_FOLDER = "movies_library_folder"
SETTING_MOVIES_PLAYLIST_FOLDER = "movies_playlist_folder"
SETTING_MOVIES_DEFAULT_AUTO_ADD = "movies_default_auto_add"
SETTING_MOVIES_PLAYED_BY_ADD = "movies_played_by_add"
SETTING_MOVIES_BATCH_ADD_FILE_PATH = "movies_batch_add_file_path"
SETTING_TV_ENABLED_PLAYERS = "tv_enabled_players"
SETTING_TV_DEFAULT_PLAYER = "tv_default_player"
SETTING_TV_DEFAULT_PLAYER_FROM_LIBRARY = "tv_default_player_from_library"
SETTING_TV_DEFAULT_PLAYER_FROM_CONTEXT = "tv_default_player_from_context"
SETTING_TV_LIBRARY_FOLDER = "tv_library_folder"
SETTING_TV_PLAYLIST_FOLDER = "tv_playlist_folder"
SETTING_TV_DEFAULT_AUTO_ADD = "tv_default_auto_add"
SETTING_TV_PLAYED_BY_ADD = "tv_played_by_add"
SETTING_TV_BATCH_ADD_FILE_PATH = "tv_batch_add_file_path"
SETTING_PREFERRED_MUSIC_TYPE = "preferred_music_type"
SETTING_MUSIC_ENABLED_PLAYERS = "music_enabled_players"
SETTING_MUSICVIDEOS_ENABLED_PLAYERS = "musicvideos_enabled_players"
SETTING_MUSIC_DEFAULT_PLAYER = "music_default_player"
SETTING_MUSICVIDEOS_DEFAULT_PLAYER = "musicvideos_default_player"
SETTING_MUSIC_DEFAULT_PLAYER_FROM_LIBRARY = "music_default_player_from_library"
SETTING_MUSICVIDEOS_DEFAULT_PLAYER_FROM_LIBRARY = "musicvideos_default_player_from_library"
SETTING_MUSIC_DEFAULT_PLAYER_FROM_CONTEXT = "music_default_player_from_context"
SETTING_MUSICVIDEOS_DEFAULT_PLAYER_FROM_CONTEXT = "musicvideos_default_player_from_context"
SETTING_MUSIC_LIBRARY_FOLDER = "music_library_folder"
SETTING_MUSICVIDEOS_LIBRARY_FOLDER = "musicvideos_library_folder"
SETTING_MUSIC_PLAYLIST_FOLDER = "music_playlist_folder"
SETTING_MUSICVIDEOS_PLAYLIST_FOLDER = "musicvideos_playlist_folder"
SETTING_LIVE_ENABLED_PLAYERS = "live_enabled_players"
SETTING_LIVE_DEFAULT_PLAYER = "live_default_player"
SETTING_LIVE_DEFAULT_PLAYER_FROM_LIBRARY = "live_default_player_from_library"
SETTING_LIVE_DEFAULT_PLAYER_FROM_CONTEXT = "live_default_player_from_context"
SETTING_LIVE_LIBRARY_FOLDER = "live_library_folder"
SETTING_LIVE_PLAYLIST_FOLDER = "live_playlist_folder"
SETTING_LIVE_DEFAULT_AUTO_ADD = "live_default_auto_add"
SETTING_PREFERRED_TOGGLE = "preferred_toggle"
SETTING_PRIMARY_SKIN = "primary_skin"
SETTING_ALTERNATE_SKIN = "alternate_skin"
SETTING_RANDOM_PAGES = "random_pages"
SETTING_USE_SIMPLE_SELECTOR = "use_simple_selector"
SETTING_AUTO_HIDE_DIALOGS = "auto_hide_dialogs"
SETTING_AUTO_HIDE_DIALOGS_PROGRESS = "auto_hide_dialogs_progress"
SETTING_AUTO_HIDE_DIALOGS_INFO = "auto_hide_dialogs_info"
SETTING_AUTO_HIDE_DIALOGS_KEYBOARD = "auto_hide_dialogs_keyboard"
SETTING_POOL_SIZE = "pool_size"
SETTING_STYLE = "style"
SETTING_STYLE_CUSTOM_FOLDER = "style_custom_folder"
SETTING_BACKGROUND = "background"
SETTING_BACKGROUND_CUSTOM_FOLDER = "background_custom_folder"
SETTING_LANGUAGE_ID = "language_id"
SETTING_TRAKT_PERIOD = "trakt_period"
SETTING_ITEMS_PER_PAGE = "items_per_page"
SETTING_FORCE_VIEW = "force_view"
SETTING_MAIN_VIEW = "main_view"
SETTING_MOVIES_VIEW = "movies_view"
SETTING_TVSHOWS_VIEW = "tvshows_view"
SETTING_SEASONS_VIEW = "seasons_view"
SETTING_EPISODES_VIEW = "episodes_view"
SETTING_MUSIC_VIEW = "music_view"
SETTING_LIVE_VIEW = "live_view"
SETTING_LIST_VIEW = "list_view"
SETTING_MOVIES_ENABLED_CHANNELERS = "movies_enabled_channelers"
SETTING_MOVIES_DEFAULT_CHANNELER = "movies_default_channeler"
SETTING_TV_ENABLED_CHANNELERS = "tv_enabled_channelers"
SETTING_TV_DEFAULT_CHANNELER = "tv_default_channeler"
SETTING_LIVE_ENABLED_CHANNELERS = "live_enabled_channelers"
SETTING_LIVE_DEFAULT_CHANNELER = "live_default_channeler"
SETTING_LIBRARY_TITLES = "library_titles"
SETTING_SYNC_FOLDER = "sync_folder"
SETTING_AUTOPATCH = "autopatch"
SETTING_AUTOPATCHES = "autopatches"
SETTING_TRAKT_API_CLIENT_ID = "trakt_api_client_id"
SETTING_TRAKT_API_CLIENT_SECRET = "trakt_api_client_secret"
SETTING_TMDB_API = "tmdb_api"
SETTING_TVDB_API = "tvdb_api"
SETTING_LASTFM_API_KEY = "lastfm_api_key"
SETTING_LASTFM_API_SHARED_SECRET = "lastfm_api_shared_secret"
