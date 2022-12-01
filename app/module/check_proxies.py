from threading import Thread

import requests

from app.module import pools


def check_proxy(proxy):
    print(p)
    proxies = {'http': proxy, 'https': proxy}
    try:
        response = requests.get('http://api.ipify.org')
        if response:
            print(proxies)
            working.append(f'http://{proxy}')
    except Exception as e:
        print(e)


def main():
    wwmix_pool = pools.WwmixProxyFilePool().pool
    working = []
    threads = []
    for p in wwmix_pool:
        t = Thread(target=check_proxy, args=(p,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    with open('wwmix.txt', 'w') as file:
        file.write('\n'.join([f'http://{p}' for p in working]))
