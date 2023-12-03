from pytube import YouTube

def ses_indir():
    adres = input("Lütfen URL Adresini Giriniz ? :")
    url= YouTube(adres)
    print(url.title)
    #for i in url.streams:
    #    print(i)
    indir = url.streams.filter(mime_type="audio/mp4", abr="48kbps").first()
    indir.download()

ses_indir()