from PIL import Image

size = 100, 100

class main():
    while(1):
        x=input("Plase Enter operation no. you want to execute: 1. RESIZE THE IMAGE 2. THUMBNAIL OF IMAGE 3.EXIT \n")
        if x == 1:
            try:
                im = Image.open('panda.jpg')
                im = im.resize(size, Image.ANTIALIAS)
                im.save('resize.jpg')
            except IOError:
                print "cannot resize for '%s'" % infile
        elif x == 2:
            try:
                im = Image.open('panda.jpg')
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('thumbnail.jpg')
            except IOError:
                print "cannot create thumbnail for '%s'" % infile
        else:
            exit(0)


if __name__ == '__main__':
    main()
