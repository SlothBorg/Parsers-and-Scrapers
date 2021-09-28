import textract
from wand.image import Image as Img
from os import getcwd, listdir, makedirs, sep
from os.path import isfile, join, dirname, exists
from re import split as Split

# DOCUMENTATION CRAP:
#   Dependancies
#       python 3
#   System packages (working on ubuntu 18.04 and debian Stretch)
#       sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev
#       pip3 install textract
#       pip3 install wand
#   Usage
#   For ease of use, you should first split a pdf, into subsections
#       pdftk A=INPUT_FILE.pdf cat A##-## output OUTPUT_FILE.pdf
#       WHERE:  ## = a page number

def get_files():
    files = []
    for f in listdir(getcwd()):
        if isfile(join(f)) and f.endswith('pdf'):
            files.append(f)
    count = len(files)

    if count == 0:
        print('No PDFs found. Exiting')
        exit()
    else:
        return files

def file_list(files):
    for index, file in enumerate(files):
        print(str(index) + "\t" + file)

def select_file(files):
    file_list(files)
    count = len(files)
    while True:
        try:
            input_ = int(input('Select a file: '))
        except ValueError:
            print('Not a valid input, try again.')
            continue
        else:
            if 0 <= input_ <= (count - 1):
                print(files[input_])
                return files[input_]
            else:
                print('Input: ' + str(input_) + ': not found in range 0-' + str(count-1))

def create_dir(directory):
    if not exists(directory):
        try:
            makedirs(directory)
            return True
        except Exception as e:
            print(e)
            exit()
        else:
            return True

# from https://stackoverflow.com/a/48030307
def alphaNumSort(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in Split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

def main(files):
    file = select_file(files)

    workingDir = 'images' + sep + file.replace('.pdf', '')
    create_dir(workingDir)

    with Img(filename=file, resolution=300) as img:
        print('Converting PDF to images')
        img.compression_quality = 99
        filename_ = join(workingDir, 'test.jpg')
        img.save(filename=filename_)

    # Set up file output.
    create_dir('output')
    outPutFile = join('output', file.replace('.pdf', '.txt'))
    fileHandler = open(outPutFile, 'w')

    pages = []
    for f in alphaNumSort(listdir(workingDir)):
        print('Working on: ' + str(f))
        if isfile(join(workingDir, f)) and f.endswith('jpg'):
            image = join(workingDir, f)
            print('Starting to OCR image: ' + str(image))
            text = textract.process(image, encoding='ascii', method='tesseract')
            page = text.decode('utf-8').strip()
            print('Writing text to file: ' + str(outPutFile))
            fileHandler.write(str(image) + "\n\n")
            fileHandler.write(page)
            fileHandler.write("\f")

if __name__ == '__main__':
    # fail early fail often
    files = get_files()
    main(files)
