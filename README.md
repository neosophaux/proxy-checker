# proxy-checker
A simple and basic proxy checking tool that will sort the fast and responsive proxies out of a list of proxies.

### Usage
`python3 check.py PROXY_LIST.json NUM_RUNS`

It will output a list of proxies that succeeded at least once into a file called 'favored.json' in the current directory. To edit the timeout before it fails the proxy simply edit `PROXY_TIMEOUT` in the python file.
