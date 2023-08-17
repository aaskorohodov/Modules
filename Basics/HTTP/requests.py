"""
GET /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.example.com
Accept-Language: ru-ru
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
"""

'''
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 88
Content-Type: text/html
Connection: Closed

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
'''


'''
*Note, that each method can actually be processed in any way on the server, but still they are intended to work this way

GET
The GET-request is used to retrieve information from the server at the specified URI. Http-requests,
which using the GET-method should only receive data and should not have any effect on that data.

HEAD
The idea of the HEAD method in an HTTP is similar to GET, but HEAD does not transfer the message body (HTTP object).

POST
An POST request is used to send data to an HTTP server, such as when you fill an HTML form on a website.

PUT
PUT is used to replace the content.

DELETE
The DELETE method on an HTTP request allows you to request the server to delete the resource data specified in the URI.

CONNECT
An HTTP request with the CONNECT method allows you to establish a tunnel to the server specified in the URI.

OPTIONS
An HTTP request with the OPTION method allows you to get parameters for communicating with a resource.

TRACE
When making an HTTP request with the TRACE method, you can track what is happening with your requests.
'''