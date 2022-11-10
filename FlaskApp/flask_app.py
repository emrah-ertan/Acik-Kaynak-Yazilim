from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime
import pandas


app = Flask(__name__)
api = Api(app)

class ziyaret(Resource):
        def get(self):
                kayit = pandas.read_csv("info.csv",sep=',')
                mesaj = ""
                print("Kayıt: ",kayit)

                listegun = kayit['Gun'].to_list()
                listeay = kayit['Ay'].to_list()
                listeyil = kayit['Yil'].to_list()
                listesaat = kayit['Saat'].to_list()
                listedakika = kayit['Dakika'].to_list()

                gun  = datetime.now().day
                ay   = datetime.now().month
                yil  = datetime.now().year
                saat = datetime.now().hour
                dakika = datetime.now().minute


                #zaman karsilastirilmasi.
                if(yil != listeyil[0]):
                    fark = yil - listeyil[0]
                    mesaj = mesaj + "Son ziyaretten "+fark+" yil gecti. "
                elif(ay != listeay[0]):
                    fark = ay-listeay[0]
                    mesaj = mesaj + "Son ziyaretten beri "+fark+" ay gecti. "
                elif(gun != listegun[0]):
                    fark = gun - listegun[0]
                    mesaj = mesaj + "Son ziyaretten beri "+fark+" gun gecti. "
                elif(saat != listesaat[0]):
                    fark = saat - listesaat[0]
                    mesaj = mesaj + "Son ziyaretten beri "+fark+" saat gecti. ",
                elif(dakika != listedakika[0]):
                    fark = dakika-listedakika[0]
                    mesaj = mesaj+ "Son ziyaretten beri "+fark+" dakika gecti. "
                else:
                    mesaj = "Son ziyaretin ustunden zaman gecmedi."
                #zaman degistirilmesi
                kayit.replace(to_replace=listeyil[0],value=yil,inplace=True)
                kayit.replace(to_replace=listeay[0],value=ay,inplace=True)
                kayit.replace(to_replace=listegun[0],value=gun,inplace=True)
                kayit.replace(to_replace=listesaat[0],value=saat,inplace=True)
                kayit.replace(to_replace=listedakika[0],value=dakika,inplace=True)
                kayit.to_csv("info.csv",index=False)
                #sonuc dondurulmesi
                return mesaj,200

class statikmatris(Resource):
        def get(self):
                matris = [[10,30,124,90,70],[5,77,54,200,44],[182,184,50,12,99]]
                return matris,200

# Add URL endpoints
#api.add_resource(Users, '/users')
#api.add_resource(Cities, '/cities')
#api.add_resource(Name, '/<string:name>')

api.add_resource(ziyaret,'/ziyaret')
api.add_resource(statikmatris,'/statikmatris')


if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)
     app.run()