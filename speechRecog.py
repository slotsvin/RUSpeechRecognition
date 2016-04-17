from dragonfly.all import Grammar, CompoundRule, Dictation
import pythoncom
import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


# Voice command rule combining spoken form and recognition processing.
class Greeting(CompoundRule):
	spec = "hello"                 # Spoken form of command.

	def _process_recognition(self, node, extras):   # Callback when command is spoken.
		speaker.Speak("Hi, how are you, ya cunt?")


class Recreation(CompoundRule):
	spec = "recreation <campus>"
	extras = [Dictation("campus")]

	def _process_recognition(self, node, extras):
		from features.sports import Campus
		Campus(extras)

# Create a grammar which contains and loads the command rule.
grammar = Grammar("speech recognition")                # Create a grammar to contain the command    rule.
grammar.add_rule(Greeting())                     # Add the command rule to the grammar.
grammar.add_rule(Recreation())
grammar.load()                                      # Load the grammar.

while True:
	pythoncom.PumpWaitingMessages()
	time.sleep(.1)
