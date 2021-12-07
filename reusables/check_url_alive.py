import urllib.request
import time


def check_website(website, timeout=30):
    startTime = time.time()
    while time.time() - startTime <= timeout:
        try:
            print(urllib.request.urlopen(website).getcode())
            return True
        except:
            pass
    return False


if __name__ == "__main__":
    website = "https://www.stackoverflow.com"
    plugin_website = "http://127.0.0.1:8051/"
    print(check_website(plugin_website, timeout=120))
