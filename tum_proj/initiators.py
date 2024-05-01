import ioc

def std_initiation():
    ioc.provide('GitHub.Request.Parser', 'html.parser')
    ioc.provide('GitHub.Request.Header', {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'})