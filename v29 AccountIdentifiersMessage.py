from Utils.Reader import Reader

class AccountIdentifiersMessage(Reader):
    def __init__(self, client, player):
      super().__init__(client)
       
      self.player = player

    def decode(self):
    	self.readBoolean()
      self.readInt()
      self.readInt()
    
    def process(self):
      pass
       
