import time
import sys

def machineWrite(text, velocity = 0.01):
	"""
    Machine Write
    =============

    Simulates the behavior of a typewriter to offer more realism in the output flow.

    Parameters
    ----------
    text : str
        What the machine is going to write.
    velocity : float
        Speed at which the text is written. Default is 0.01.
    """
	for caracter in text:
		sys.stdout.write(caracter)
		sys.stdout.flush() #forces the character to be written
		time.sleep(velocity)
	print() #add a line break at the end
	time.sleep(0.1)

