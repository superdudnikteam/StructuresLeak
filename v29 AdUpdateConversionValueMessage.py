from Utils.Reader import Reader

class AdUpdateConversionValueMessage(Reader):
    def __init__(self, client, player):
      super().__init__(client)#40000
       
      self.player = player

    def decode(self):
    	self.readVInt()
    	self.readString()
    	self.readInt()
    	self.readInt()
    	self.readVInt()
    
    def process(self):
      pass