from StudentCard import StudentCard
import datetime
from PIL import Image
from gensim.models import word2vec


class MainShopCharger:

    insertedStudentCard = None #挿入されている学生証
    updateDate = None #更新年月日

    def __init__(self):
        pass
    
    #学生証へのチャージ
    @classmethod
    def chargeMoney(cls, money):
        if cls.insertedStudentCard is None:
            print("学生証が挿入されていません.")
        else:
            cls.insertedStudentCard.setAccountBalance(cls.insertedStudentCard.getAccountBalance() + money)
            cls.printAccountBalance()
            cls.updateDate = datetime.date.today()

    #情報の表示
    @classmethod
    def printAccountBalance(cls):
        print("残高を表示します")
        print("学生名: " + cls.insertedStudentCard.getStudentName())
        print("残高: " + str(cls.insertedStudentCard.getAccountBalance()))

    #学生証の挿入
    @classmethod
    def insertStudentCard(cls, studentId):
        cls.insertedStudentCard = StudentCard.getStudentCard(studentId)

    #更新年月日の表示
    @classmethod
    def printUpdateDay(cls):
        print("最終チャージ: {0:%Y} {0:%m} {0:%d}".format(cls.updateDate))
    
    #画像の表示
    @classmethod
    def printPicture(cls):
        img = cls.insertedStudentCard.getStudentPicture()
        img.show()

    #キーワードの類似語検索
    @classmethod
    def keywordExtraction(cls):
        cnt = 0
        model = word2vec.Word2Vec.load("./wiki.model")
        results = model.wv.most_similar(positive=[cls.insertedStudentCard.getStudentKeyword()])
        for result in results:
            cnt = cnt + 1
            print(result)
            if cnt == 3:
                break

    @classmethod
    def main(cls):
        #画像の用意
        img = Image.open("sample.jpg")
        img2 = Image.open("sample2.jpg")

        #インスタンス生成   
        studentCard1 = StudentCard(0, "tut", "物理", img)
        studentCard2 = StudentCard(1, "tenpaku", "南京錠", img2)

        #初期残高の設定
        studentCard1.setAccountBalance(1000)
        studentCard2.setAccountBalance(0)

        #エラー処理の確認
        cls.chargeMoney(200)

        #学生証1枚目の挿入とチャージ
        cls.insertStudentCard(0)

        cls.chargeMoney(1000)
        cls.chargeMoney(-300)

        #設定された画像の表示
        cls.printPicture()

        #キーワードの検索
        cls.keywordExtraction()

        #学生証2枚目の挿入とチャージ
        cls.insertStudentCard(1)

        cls.chargeMoney(500)
        cls.chargeMoney(-1000)

        #キーワードの検索
        cls.keywordExtraction()

        #最終更新年月日と設定された画像の表示
        cls.printUpdateDay()
        cls.printPicture()


if __name__ == "__main__":
    MainShopCharger.main()
