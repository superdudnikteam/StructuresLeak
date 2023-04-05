from Utils.Reader import Reader

class CryptoErrorMessage(Reader):
    def __init__(self, client, player):
      super().__init__(client)#29997
       
      self.player = player

    def decode(self):
    	self.readString()
    	self.readString()
    	self.readString()
    	self.readVInt()
    	self.readVInt()
    
    def process(self):
      pass