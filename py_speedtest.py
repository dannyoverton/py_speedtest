import speedtest
import datetime
import time
import itertools
from tkinter import *


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

starttime=time.time()
def main():
    # write to csv
    with open('file.csv', 'a') as f, open('file.txt', 'a') as g:
        for i in itertools.count(0):
            d, u, p = test()
            x = datetime.datetime.now()
            f = open('file.csv', 'a')
            f.write('{},{},{},{}\n'.format(d / 1E+6, u / 1E+6, p, x))
            f.close()
            print('\n CSV updated \n')
            g = open('file.txt', 'a')
            g.write('\n')
            g.write('Download: {:.2f} Mb/s\n'.format(d / 1E+6))
            g.write('Upload: {:.2f} Mb/s\n'.format(u / 1E+6))
            g.write('Ping: {}\n'.format(p))
            g.write('Time: {}\n'.format(x))
            g.close()
            print('Text file updated \n')
            print('Download: {:.2f} Mb/s\n'.format(d / 1E+6))
            print('Upload: {:.2f} Mb/s\n'.format(u / 1E+6))
            print('Ping: {}\n'.format(p))
            print('Time: {}\n'.format(x))
            time.sleep(7200.0 - ((time.time() - starttime) % 7200.0))



window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text='Hola')
lbl.grid(column=0, row=0)

def clicked():
    d, u, p = test()
    lbl.configure(text=('D:{:.1f}\nU:{:.1f}\nP:{:.1f}').format(d / 1E+6, u / 1E+6, p))

btn = Button(window, text='Test the Internet speed', command=clicked)
btn.grid(column=1, row=0)
window.mainloop()


    # pretty write to txt file
    # with open('file.txt', 'a') as f:
    #     for i in range(3):
    #         print('Making test #{}'.format(i+1))
    #         d, u, p = test()
    #         x = datetime.datetime.now()
    #         f.write('Test #{}\n'.format(i+1))
    #         f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
    #         f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
    #         f.write('Ping: {}\n'.format(p))
    #         f.write('Time: {}\n'.format(x))
    #         #time.sleep(10)
    # # simply print in needed format if you want to use pipe-style: python script.py > file
    # for i in range(3):
    #     d, u, p = test()
    #     x = datetime.datetime.now()
    #     print('Test #{}\n'.format(i+1))
    #     print('Download: {:.2f} Kb/s\n'.format(d / 1024))
    #     print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
    #     print('Ping: {}\n'.format(p))
    #     print('Time: {}\n'.format(x))
    #     #time.sleep(10)


if __name__ == '__main__':
    main()

