import time
def get_user(name):
    print('사용자 {!r} 정보 조회중...'.format(name))
    time.sleep(1)
    print('사용자 {!r} 정보 조회 완료!'.format(name))
    
def main():
    start = time.time()
    get_user('GG')
    get_user('Be')
    end = time.time()
    print(f'소요 시간: {end - start}')
    
main()