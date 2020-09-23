#use python2 youtubemp3.y
import os, sys


try:
  url = sys.argv[1]
except:
  print('------------------------------------------------------')
  print('  Download Youtube to MP3  --audio-format mp3')
  print('------------------------------------------------------')
  print('    Usage     :  python2 youtubemp3.py <url> ')
  print('------------------------------------------------------')
  sys.exit()

os.system("youtube-dl -x --audio-format mp3 -o 'result/%(title)s.%(ext)s' "+url)
print('\nSUKSES DOWNLOAD !\nResult file > result/hasildonwloadmu.mp3')
