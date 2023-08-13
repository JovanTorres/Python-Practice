print("😁Welcome to PlaylistMaker3000!😁\n🎶Enter a song title to add it to the playlist🎶\n🛑When you're done, enter 'Quit' 🛑")
def playlist():
    songs = []
    while True:
        song = input('\nEnter a song title:')
        if song == 'Quit':
            break
        if (song in songs):
            numm = songs.index(song) + 1
            print(f'❌{song} is already in the playlist❌ It is song number {numm} in the playlist!')
            
        else:
            songs.append(song)
            num = len(songs)
            print(f'✅{song} has been added to the playlist✅ It is number {num} in the playlist!')
            

playlist()
