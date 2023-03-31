from Utils.Writer import Writer

class CreatePlayerMapRespons(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 22100
        self.player = player

    def encode(self):
    	self.writeBoolean(False)
    	for x in range(0):
    		self.writeStringReference('')
    		self.writeBytes(0)
    		for x in range(0):
    			self.writeVInt(0)
    			self.writeVInt(0)
    			self.writeVInt(0)
    			self.writeVInt(0)
    			self.writeVInt(0)
