import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def Campus(extras):

	campus = str(extras['campus'])
	if campus == "bush":
		speaker.Speak("bush")

