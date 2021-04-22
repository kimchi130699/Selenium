from multiprocessing import Pool
import time 

def mu(x):
    time.sleep(3)
    return x**3

def sum(lst):
    x =lst[0]
    y = lst[1]
    return x +y

def pool_handler():
    p = Pool(2)
    # kq =p.map_async(mu,(1,2,3)) #ko bi block
    kq = p.map_async(sum,([1,2],[3,4],[5,6]))
    print('wait.....')

    print(kq.get()) #khi chay ham nay _>block
    p.close()
    p.join()
    print('task end')
if __name__ =='__main__':
    pool_handler()