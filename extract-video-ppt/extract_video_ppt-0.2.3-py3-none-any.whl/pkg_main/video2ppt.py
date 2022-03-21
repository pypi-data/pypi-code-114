# Importing all necessary libraries
import math
import cv2
import os
import shutil
import click

import compare
import images2pdf

# export pdf
# images = os.listdir('./data')
# images.sort()
# imagePaths = []

# for image in images:
#     basepath = './data/' + image
#     (fileName, mimeType) = os.path.splitext(basepath)
    
#     if mimeType != '.jpg':
#         continue

#     imagePaths.append(basepath)

# images2pdf.images2pdf('data/test.pdf', imagePaths)

# exit(0)

DEFAULT_PATH = './.extract-video-ppt-tmp-data'
DEFAULT_PDFNAME = 'outputPath.pdf'
DEFAULT_MAXDEGREE = 0.6
CV_CAP_PROP_FRAME_WIDTH = 1920
CV_CAP_PROP_FRAME_HEIGHT = 1080

_url = 'https://v1-bdl.ixigua.com/803cd508740b9ebe3b4468a8a7e4123b/6235bb53/video/tos/cn/tos-cn-v-c1801c/637b96b096be4673abc2118fc1f5975d/?a=2098&br=238&bt=238&cd=0%7C0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=4&er=0&ft=tdF_r88-oU-DYlnt7TQ_plXxuhsdk.avtqY&l=20220319172136010194034033036A9641&lr=&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M2Y6Nmg6ZnN0OzMzNDxkM0ApOGY6N2gzNztpNzYzNmVkNGduYzIycjRfXzJgLS1kMS9zc15eLjMxLzViMDIyXjVeLjQ6Yw%3D%3D&vl=&vr='
# _url = '../test.mp4'
URL = ''
OUTPUTPATH = ''
PDFNAME = DEFAULT_PDFNAME
MAXDEGREE = DEFAULT_MAXDEGREE

@click.command()
@click.option('--degree', default=DEFAULT_MAXDEGREE, help = 'frame diff degree scale, default: 0.6')
@click.option('--pdfname', default=DEFAULT_PDFNAME, help = 'the name of output pdf file, default: output.pdf')
@click.argument('outputpath')
@click.argument('url')
def main(degree, pdfname, outputpath, url):
    global URL
    global OUTPUTPATH
    global MAXDEGREE
    global PDFNAME

    URL = url
    OUTPUTPATH = outputpath
    MAXDEGREE = degree
    PDFNAME = pdfname

    prepare()
    start()
    exportPdf()

    

def start():
    global CV_CAP_PROP_FRAME_WIDTH
    global CV_CAP_PROP_FRAME_HEIGHT

    vcap = cv2.VideoCapture(URL)
    FPS = vcap.get(5)
    TOTAL_FRAME= int(vcap.get(7))
    CV_CAP_PROP_FRAME_WIDTH = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    CV_CAP_PROP_FRAME_HEIGHT = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #if not vcap.isOpened():
    #    print "File Cannot be Opened"
    # frame
    lastDegree = 0
    lastFrame = []
    readedFrame = 0

    # process bar
    # with click.progressbar(length=100, label='readed frame') as bar:
    # exit(0)
    while(True):
            click.clear()
            print('process:' + str(math.floor(readedFrame / TOTAL_FRAME * 100)) + '%')
            # bar.update(math.ceil(readedFrame / TOTAL_FRAME))
            # Capture frame-by-frame
            ret, frame = vcap.read()
            #print cap.isOpened(), ret
            if ret:
                readedFrame += 1
                if readedFrame % FPS != 0:
                    continue

                isWrite = False

                if len(lastFrame):
                    degree = compare.compareImg(frame, lastFrame)
                    if degree < MAXDEGREE:
                        isWrite = True
                        lastDegree = round(degree, 2)
                else:
                    isWrite = True

                if isWrite:
                    name = DEFAULT_PATH + '/frame'+ second2hms(math.ceil(readedFrame / FPS)) + '-' + str(lastDegree) + '.jpg'
                    cv2.imwrite(name, frame)
                    lastFrame = frame
                    

            else:
                break

    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()

# prepare env
def prepare():
    global OUTPUTPATH

    try:

        if not os.path.exists(OUTPUTPATH):
            os.makedirs(OUTPUTPATH)

    # if not created then raise error
    except OSError as error:
        print (error)
        exit(1)

    try:
        
        if os.path.exists(DEFAULT_PATH):
            shutil.rmtree(DEFAULT_PATH)

        if not os.path.exists(DEFAULT_PATH):
            os.makedirs(DEFAULT_PATH)

    # if not created then raise error
    except OSError as error:
        print (error)
        exit(1)

# export pdf and clear env
def exportPdf():
    images = os.listdir(DEFAULT_PATH)
    images.sort()
    imagePaths = []

    for image in images:
        basepath = DEFAULT_PATH + '/' + image
        (fileName, mimeType) = os.path.splitext(basepath)
        
        if mimeType != '.jpg':
            continue

        imagePaths.append(basepath)

    pdfPath = DEFAULT_PATH + '/' + PDFNAME
    images2pdf.images2pdf(pdfPath, imagePaths, CV_CAP_PROP_FRAME_WIDTH, CV_CAP_PROP_FRAME_HEIGHT)

    # copy to outputPath path
    shutil.copy(pdfPath, OUTPUTPATH)

    # clear env
    shutil.rmtree(DEFAULT_PATH)

def second2hms(second):
    m, s = divmod(second, 60)
    h, m = divmod(m, 60)
    return ("%02d:%02d:%02d" % (h, m, s))

if __name__ == '__main__':
    # main(0.6, 'o.pdf', './output', _url)
    main()