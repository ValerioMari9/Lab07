from unittest import result

from database.DB_connect import DBConnect
from model.situazione import Situazione, SituazioneMedia


class MeteoDao():

    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getUmiditaMedia(mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        q="""select avg(s.Umidita) as umidita, s.Localita as localita   
                from situazione s
                where month(s.data)=%s
                group by localita;"""
        cursor.execute(q, (mese,))
        l=cursor.fetchall()
        r=[]
        for i in l:
           r.append(SituazioneMedia(**i))
        cursor.close()
        cnx.close()
        return r
    @staticmethod
    def getSituazioniPercorso(mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        q="""select s.Umidita as umidita, s.Localita as localita, s.Data as data   
             from situazione s
             where month(s.data)=%s and DAY(s.`Data` )<16
             order by s.`Data`, s.Localita ;"""
        cursor.execute(q, (mese,))
        l=cursor.fetchall()
        r={}

        for i in l:
            s=Situazione(**i)
            r.setdefault(s.data, []).append(s)
        li=[]
        for i in r:
            li.append(tuple(r[i]))
        cursor.close()
        cnx.close()
        return li
def main():
    for i in MeteoDao.getSituazioniPercorso(1):
        print(i)


if __name__=="__main__":
    main()