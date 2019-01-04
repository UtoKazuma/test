

class StudentCard:

    studentCardList_ = [] #学生証のリスト
    studentKeyword = "" #キーワード
    studentPicture = None #画像

    def __init__(self, studentId, studentName, studentKeyword, studentPicture):
        self.studentId = studentId
        self.studentName = studentName
        self.accountBalance = 0
        self.studentKeyword = studentKeyword
        self.studentPicture = studentPicture
        StudentCard.studentCardList_.append(self)

    #残高の取得
    def getAccountBalance(self):
        return self.accountBalance

    #残高の設定
    def setAccountBalance(self, accountBalance):
        self.accountBalance = accountBalance

    #学生証の取得
    @classmethod
    def getStudentCard(cls, studentId):
        return cls.studentCardList_[studentId]
    
    #名前の取得
    def getStudentName(self):
        return self.studentName
    
    #キーワードの設定
    def setStudentKeyword(self, Keyword):
        self.studentKeyword = Keyword

    #キーワードの取得
    def getStudentKeyword(self):
        return self.studentKeyword
    
    #画像の設定
    def setStudentPicture(self, picture):
        self.studentPicture = picture
    
    #画像の取得
    def getStudentPicture(self):
        return self.studentPicture