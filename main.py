from pytube import YouTube

print("Welcome In \" Youtube Video Downloader \" ")

link = input("Enter Video Link: ")

try:
    video = YouTube(link) # create YouTube object with given link from the user
    for stream in video.streams:
        print(stream, '\n')
    user_itag = input('Select With The Itag: ')
    video.streams.get_by_itag(user_itag).download('./')
    video.register_on_complete_callback(print('Download Completed Successfully ! '))
    input('Press Enter To Close ... ')
except ValueError as e:
    print(e)
