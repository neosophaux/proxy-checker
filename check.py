import socket
import sys
import json

PROXY_TIMEOUT = 1

runs = int(sys.argv[2])

with open(sys.argv[1], 'r') as proxy_list:
    proxies = json.loads(proxy_list.read())['proxies']
    proxy_stats = {}

    for run in range(1, runs + 1):
        for idx, proxy in enumerate(proxies):
            if proxy not in proxy_stats:
                proxy_stats[proxy] = {
                    'fails': 0
                }

            proxy_sock = socket.socket()
            proxy_addr = proxy.split(':')

            proxy_sock.settimeout(PROXY_TIMEOUT)

            try:
                proxy_sock.connect((proxy_addr[0], int(proxy_addr[1])))

                print("[ Run %d/%d #%d ] Proxy '%s' succeeded." % (run, runs, idx, proxy))
            except (OSError, socket.timeout):
                print("[ Run %d/%d #%d ] Proxy '%s' failed." % (run, runs, idx, proxy))

                proxy_stats[proxy]['fails'] += 1

                if proxy_stats[proxy]['fails'] == runs:
                    proxies.pop(idx)

            proxy_sock.close()

    favored_proxies = open('favored.json', 'w')

    favored_proxies.write(json.dumps(proxies, indent = 4))
    favored_proxies.close()
