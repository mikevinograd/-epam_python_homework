"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
>>> count_dots_on_i("https://example.com/")
59
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib.request

def count_dots_on_i(url: str) -> int:
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        i = 0
        for char in html:
            # print(type(char))
            if char == 'i':
                i += 1
        return html.count("i")
    except:
        raise ValueError("Unreachable {url}")
print(count_dots_on_i('https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen'))