class HousePark:
    lastname = '박'
    def _init_(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print('%s, %s여행을 가다.' % (self.fullname, where))
    def _add_(self,other):
        print('%s, %s 결혼했네.' % (self.fullname, other.fullname))
    def _sub_(self, other):
        print('%s, %s 헤어졌네' % ( self.fullname,  other.fullname))

    class HouseKim(HousePark):
        lastname = '김'
    def travel(self, where):
        print('%s은 %s로 여행합니다.' % (self, fullname, where))

    #k
    pey=HousePark('응용')
    juliet=HouseKim('줄리엣')
    pey.travel('독도')
    juliet.travel('독도')
    pey + juliet
    pey - juliet
