import re,time,subprocess

with open('../2') as fp:
    for line in fp:
        line=line.strip('\n')
        a = re.split(r'[;,/\s]\s*', line)[3]
        b = "ffmpeg -i " + line +" " + a + ".mp4"
        print b
        subprocess.call([b],shell=True)
        time.sleep(30)
