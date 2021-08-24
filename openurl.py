import urllib.request
import urllib.parse

def main():
    url = "http://httpbin.org/get"

    result = urllib.request.urlopen(url)

    print("return code___________")
    print("Result code: {0}".format(result.status))
    print("headers______________")
    print(result.getheaders())
    print("return data")
    print(result.read().decode('utf-8'))



if __name__ == "__main__":
    main()