from pytube import YouTube
import os

while(True):
    print("\nYouTube Video Downloader\n")
    print("Do you want to download a video?")
    option = input("[y] YES, [n] NO: ").lower()

    if option == 'y':
        try:
            os.mkdir('Downloaded_Videos')
        except FileExistsError:
            pass
        
        videos = []
        for filename in os.listdir('Downloaded_Videos'):
            filename = filename.strip()
            filename = filename[:-4]
            videos.append(filename)
            
        link = input("\nEnter the youtube video link: ")
        yt = YouTube(link)
        
        video_title = yt.title.replace('.', '')
        video_title = video_title.replace('\\','')
        video_title = video_title.replace('/','')
        video_title = video_title.replace(':','')
        video_title = video_title.replace('*','')
        video_title = video_title.replace('?','')
        video_title = video_title.replace('|','')
        video_title = video_title.replace('"','')
        video_title = video_title.replace("'",'')
        video_title = video_title.replace('>','')
        video_title = video_title.replace('<','')
        
        if video_title in videos:
            print("\nThis video already exists in the 'Downloaded_Videos' folder.")
        else:
            if yt.check_availability == None:
                print("\nThe video is not available.")
            else:
                yd = yt.streams.get_by_resolution('720p')
                if yd == None:
                    yd = yt.streams.get_highest_resolution()
                try:
                    yd.download('Downloaded_Videos')
                except:
                    print("\nAn error has occurred. Try again later!")
                else:
                    print("\nThe video",yd.title,"was downloaded and added to the 'Downloaded_Videos' folder.")
    elif option == 'n':
        break
    else:
        print("\nInvalid option.")