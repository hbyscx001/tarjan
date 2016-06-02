import os 

def run(**args):
	print '[*] Inn dirlister module.'
	files = os.listdir('.')

	return str(files)
