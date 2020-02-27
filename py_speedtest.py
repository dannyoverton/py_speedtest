import speedtest
import datetime
import time
import itertools


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
            f.write('{},{},{},{}\n'.format(d / 1024, u / 1024, p, x))
            f.close()
            print('CSV updated \n')
            g = open('file.txt', 'a')
            g.write('\n')
            g.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
            g.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
            g.write('Ping: {}\n'.format(p))
            g.write('Time: {}\n'.format(x))
            g.close()
            print('Text file updated \n')
            print('\n')
            print('Download: {:.2f} Kb/s\n'.format(d / 1024))
            print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
            print('Ping: {}\n'.format(p))
            print('Time: {}\n'.format(x))
            time.sleep(7200.0 - ((time.time() - starttime) % 7200.0))


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

