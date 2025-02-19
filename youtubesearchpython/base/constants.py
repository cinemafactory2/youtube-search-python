
VIDEO_ELEMENT      = 'videoRenderer'
CHANNEL_ELEMENT    = 'channelRenderer'
PLAYLIST_ELEMENT   = 'playlistRenderer'
SHELF_ELEMENT      = 'shelfRenderer'

class ResultMode:
    json = 0
    dict = 1

class SearchMode:
    videos = 'EgIQAQ%3D%3D'
    channels = 'EgIQAg%3D%3D'
    playlists = 'EgIQAw%3D%3D'

class VideoUploadDateFilter:
    lastHour = 'EgQIARAB'
    today = 'EgQIAhAB'
    thisWeek = 'EgQIAxAB'
    thisMonth = 'EgQIBBAB'
    thisYear = 'EgQIBRAB'

class VideoDurationFilter:
    short = 'EgQQARgB'
    long = 'EgQQARgC'

class VideoSortOrder:
    relevance = 'CAASAhAB'
    uploadDate = 'CAISAhAB'
    viewCount = 'CAMSAhAB'
    rating = 'CAESAhAB'
