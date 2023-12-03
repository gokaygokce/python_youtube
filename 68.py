from pytube import YouTube
class video:
    def __init__(self,url):
        self.url = url
    def adres(self):
        url_adres = input("URL Adresini Giriniz Lütfen")
        self.url = url_adres
        ur = YouTube(self.url)
        print(ur.title,"\n",ur.author)
        print(ur.streams)
        akıs_gör = ur.streams.filter(progressive="True").first()
        print(akıs_gör)
    def indir_video(self):
        ur2 = YouTube(self.url)
        stream2= ur2.streams.filter(res="360p",progressive="True").first()
        stream2.download()

        #deneme = ur.streams
        # deneme = ur.streams
        #for i in deneme:
           # print(i)
while True:
    yazdır = video("url")
    yazdır.adres()
    bilgi = input("Videoyu indirmek için 1 çıkış için 2")
    if bilgi == "1":
        yazdır.indir_video()
        print("Tebrikler Videonuz indirlidi.")
    else:
        print("Çıkış Yapıldı")
        break


#url = YouTube("https://www.youtube.com/watch?v=tsjJi7pgwXY")
#print("Video baslıgı:", url.title)
#print("Video baslıgı:", url.author)
#print("Video baslıgı:", url.publish_date)
#print("Video begeni:", url.rating)