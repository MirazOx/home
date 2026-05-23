import urllib.request
import urllib.error
import sys

URLS = [
    "http://localhost:8080/",
    "http://localhost:8080/about/",
    "http://localhost:8080/writing/",
    "http://localhost:8080/archive/",
    "http://localhost:8080/research/",
    "http://localhost:8080/academic/",
    "http://localhost:8080/interventions/",
    "http://localhost:8080/credentials/",
    "http://localhost:8080/services/",
    "http://localhost:8080/beyond/",
    "http://localhost:8080/beyond/coffee/",
    "http://localhost:8080/projects/attention-ledger/",
    "http://localhost:8080/projects/bachelor-economy/",
    "http://localhost:8080/projects/high-performance-learning/",
    "http://localhost:8080/projects/design-your-degree/",
    "http://localhost:8080/projects/easeparenting/",
    "http://localhost:8080/projects/floodlines/"
]

def test_url(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            code = response.getcode()
            if code == 200:
                print(f"PASS: {url} (200 OK)")
                return True
            else:
                print(f"FAIL: {url} returned status {code}")
                return False
    except urllib.error.HTTPError as e:
        print(f"FAIL: {url} HTTP Error: {e.code}")
        return False
    except urllib.error.URLError as e:
        print(f"FAIL: {url} URL Error: {e.reason}")
        return False
    except Exception as e:
        print(f"FAIL: {url} Error: {str(e)}")
        return False

def main():
    print("Starting verification of redesign page endpoints...\n")
    success = True
    for url in URLS:
        if not test_url(url):
            success = False
    
    if success:
        print("\nAll tested pages are serving successfully (200 OK)!")
        sys.exit(0)
    else:
        print("\nSome pages failed to serve. Please check logs.")
        sys.exit(1)

if __name__ == "__main__":
    main()
