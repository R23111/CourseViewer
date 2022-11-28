import sys
import os   
import vlc

# print(os.path.dirname(sys.argv[0]))

def main(argv):
    video = "test.mp4"
    player = vlc.MediaPlayer(video)
    player.play()

if __name__ == "__main__":
    main(sys.argv)