import subprocess


def pip_quick():
	commands = {'pyttsx3', 'speechrecognition', 'pyaudio', 'gtts', 'googletrans==4.0.0-rc1'}

	for call in commands:
		subprocess.call(["pip install "+call], shell=True)
	
	py = {'espeak, python3-pyaudio, python3-vlc, python3-tkinter'}

	for sudo in py:
		subprocess.call(["sudo apt install "+sudo], shell=True)

if __name__=="__main__":
    pip_quick()