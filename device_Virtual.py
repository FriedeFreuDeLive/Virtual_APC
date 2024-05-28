#name=Virtual

import transport
import midi
import patterns
import device
import channels

#fl colors:
#red: #ff0000, #C71414, #901414, #591414, #221414
#skin: #EBCCAB, #C4A585, #9E7F5F, #785939, #523314
#skinnew: #EBCCAB, #F9EEE4, #9E7F5F, #785939, #523314
#green: #00ff00, #14C714, #149014, #145914, #142214
#greennew: #00ff00, #C6FFC6, #004300, #145914, #142214 
#purple: #AA00FF, #8814D0, #6614A1, #441472, #221444 
#purplenew: #AA00FF, #EFD3FF, #6614A1, #441472, #221444
#yellow: #ffff00, #C7C714, #909014, #595914, #222214
#orange: #ffaa00, #CC8414, #995F14, #663914, #331414
#blue: #0000ff, #1414C7, #141490, #141459, #141422
#cyan: #00FFFF, #14CCCC, #149999, #146666, #143333
#magenta: #ff00ff, #CC14CC, #991499, #661466, #331433

class TVirtualScript():
	def HandleMuteToggle(self, event):
		for y in range(0, self.buttons-1):
			if event.data1 == y:
				for z in range(0, channels.channelCount(1)-1):
					if channels.getChannelColor(z) == self.channelColors[y]:
						channels.muteChannel(z)
		for y in range(0, 5):
			if event.data1 == y+82:
				for z in range(0, channels.channelCount(1)):
					if channels.getChannelColor(z) == self.channelColors2[y]:
						channels.muteChannel(z)
	def OnInit(self):
		self.buttons = 41
		self.channelColors = [ -14543852,  -11390188,  -15457772,  -14543804,  -14540268,  -13429740,  -15461342,  -15453389,
							  -10939372, -8890055, -15443692, -12315534, -10921708, -10077932, -15461287, -15440282,
                              -7334892, -6389921, -15449324, -10087263, -7303148, -6725868, -15461232, -15427175,
							  -3730412, -397596, -3735610, -1059841, -3684588, -3374060, -15461177, -15414068,
							  -60396, -1323861, -15401196, -5630721, -236, -21996, -15461121, -15400961]
		self.channelColors2 = [ -60161,  -3402548,  -6744935, -10087322,  -13429709]
	def OnControlChange(self, event):
		print(event.data1)
		print(event.data2)
		print(channels.getChannelColor(channels.selectedChannel(0)))
		if event.data1 == 100:
			patterns.jumpToPattern(patterns.patternNumber() - 1)
		if event.data1 == 101:
			patterns.jumpToPattern(patterns.patternNumber() + 1)
		if event.data1 == 91:
			transport.start()
		if event.data1 == 91:
			transport.stop()
		if event.data1 > 81 and event.data1 < 87:
			HandleMuteToggle(event)
		if event.data1 < 40:
			HandleMuteToggle(event)
		if event.data1 == 113 and event.data2 == 1:
			usedChannels = []
			for y in range(0, channels.channelCount(0)):
				for z in range(0, 63):
					if channels.getGridBit(y, z) == 1:
						usedChannels.append(y)
						break
			for x in usedChannels:
				if channels.selectedChannel(1,0,0) < x:
					channels.selectOneChannel(x)
					break
		elif event.data1 == 113 and event.data2 == 127:
			usedChannels = []
			for y in range(0, channels.channelCount(0)):
				for z in range(0, 63):
					if channels.getGridBit(y, z) == 1:
						usedChannels.append(y)
						break
			usedChannels.reverse()
			for x in usedChannels:
				if x < channels.selectedChannel(1,0,0):
					channels.selectOneChannel(x)
					break
VirtualScript = TVirtualScript()
def HandleMuteToggle(event):
	VirtualScript.HandleMuteToggle(event)
def OnInit():
	VirtualScript.OnInit()
def OnControlChange(event):
	VirtualScript.OnControlChange(event)