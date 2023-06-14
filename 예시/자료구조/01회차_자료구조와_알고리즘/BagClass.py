class Bag:
 #   def__init__(self):
  #  self.bag=[]

    def contains(self, e):
        return e in self.bag 

    def insert (self, e) :
        self. append(e)

    def remove(self, e) :
        self.bag.remove(e)

    def count(self):
        return len(self.bag)
    
    #===========================
myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print('내 가방속의 물건 : ', myBag.bag)

myBag.insert(myBag, '빗')
myBag.remove(myBag,'손수건')
print('내 가방속의 물건 : ', myBag.bag)

##print('빗의 개수 : ', numOf(myBag,'빗'))
##print('빛의 개수 : ', numOf(myBag,'빛'))

