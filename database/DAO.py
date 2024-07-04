from database.DB_connect import DBConnect

from model.correlazione import Correlazione


class DAO():

    @staticmethod
    def get_all_cromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT Chromosome as c from genes g
                WHERE g.Chromosome != 0"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["c"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_all_correlazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT g1.Chromosome as c1, g2.Chromosome as c2, g1.GeneID as gen1, g2.GeneID as gen2, i.Expression_Corr as c 
                FROM genes g1, genes g2, classification c1, classification c2, interactions i
                WHERE g1.Chromosome != g2.Chromosome AND g1.Chromosome!=0 and g2.Chromosome!=0 AND c1.GeneId = g1.GeneId AND c1.GeneId = i.GeneID1
                AND g2.GeneID = c2.GeneID AND g2.GeneID =i.GeneID2"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(
                Correlazione(row["c1"], row["c2"], row["gen1"], row["gen2"], row["c"]))

        cursor.close()
        conn.close()
        return result
