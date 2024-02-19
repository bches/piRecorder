import sys
from pitftgpio import PiTFT_GPIO
from subprocess import Popen, call, check_output, CalledProcessError
import time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

if __name__ == '__main__':
    directory = sys.argv[1]
    filename = sys.argv[2]
    
    pitft = PiTFT_GPIO()
    runLoop = True
    pids = [None, None]

    print()
    print(f"{BOLD}Welcome to piRecorder!{ENDC}")
    print()
    print("Buttons on the side of the PiTFT screen have the following mapping:")
    print(f"\tButton 1: {OKGREEN}PLAY{ENDC}")
    print(f"\tButton 2: {WARNING}RECORD{ENDC}")
    print(f"\tButton 3: {FAIL}STOP{ENDC}")
    print(f"\tButton 4: {UNDERLINE}EXIT{ENDC}")
    
    while runLoop:
        for i in range(2):
            if pids[i]:
                try:
                    check_output(["/bin/ps", str(pids[i])])
                except CalledProcessError:
                    print("Process PID=%s ended" % pids[i])
                    pids[i] = None
        
        if pitft.Button1:
            if pids[0] is None:
                pid = Popen(["/usr/bin/aplay", "--device=plughw:1,0",
                             f"{directory}/{filename}.wav"]).pid
                print(f"{OKGREEN}PLAY{ENDC}: PID={pid}")
                print(f"file: {directory}/{filename}")
                pids[0] = pid

        if pitft.Button2:
            if pids[1] is None:
                pid = Popen(["/usr/bin/arecord", "--device=hw:1,0",
                             "--format", "S16_LE", "--rate", "44100", "-c2",
                             "-i",
                             f"{directory}/{filename}.wav"]).pid
                print(f"{WARNING}RECORD{ENDC}: PID={pid}")
                print(f"file: {directory}/{filename}")
                pids[1] = pid

        if pitft.Button3:
            for i in range(2):
                pid = pids[i]
                if pid:
                    print(f"{FAIL}STOP{ENDC}: PID={pid}")
                    retcode = call(["/bin/kill", "-SIGINT", f"{pid}"])
                    pids[i] = None
                    
        if pitft.Button4:
            print(f"{UNDERLINE}EXIT{ENDC}: {pid}")
            runLoop = False

        time.sleep(0.01)
    
