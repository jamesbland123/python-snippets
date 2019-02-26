""" Whois IP lookup using requests library """
import requests

def getWhois(ip_addr):
    url = "http://ip-api.com/xml/" + ip_addr
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    address = getWhois("107.184.107.239")
    print(address)