from pytube import YouTube


def video_indir():
    x = input("Youtube URL Adresinizi Giriniz Lütfen: ")
    url = YouTube(x)
    # print(url.streams)
    # for i in url.streams:
    #    print(i)
    url_stream = url.streams.filter(res="360p").first()
    url_stream.download()
    print("*" * 40)
    print("Youtube Video İndirme İşlemi Tamamlandı.")
    print("*" * 40)


def ses_indir():
    url = YouTube(input("Youtube URL Adresini Giriniz ? :"))
    url_stream = url.streams.filter(mime_type="audio/mp4").first()
    url_stream.download()


while True:
    print("*" * 40)
    print("Youtube Video ve Ses Dosyası İndirmeye Hoşgeldiniz.")
    print("*" * 40)
    desc = int(
        input("Video İndirmek için 1 yazınız\nSes dosyası indirmek için 2 yazınız\nÇıkmak için 3 yazınız lütfen?  "))
    print("*" * 40)
    if desc == 1:
        video_indir()
        print("Dosyasınız indiriliyor....")
        print("Dosyanız indirildi.")
        print("Gökay GÖKÇE")
    elif desc == 2:
        ses_indir()
        print("Dosyasınız indiriliyor....")
        print("Dosyanız indirildi.")
        print("Gökay GÖKÇE")
    else:
        break
