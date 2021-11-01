'''
GET /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.example.com
Accept-Language: ru-ru
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
'''

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
1	GET
Метод HTTP запроса GET используется для получения информации с сервера по указанному URI. HTTP запросы,
использующие метод GET должны получать только данные и не должны оказывать никакого влияния на эти данные.

2	HEAD
Принцип работы метода HEAD в HTTP запросе аналогичен методу GET, но метод HEAD не передает тело сообщения (HTTP объект).

3	POST
HTTP запрос POST используется для отправки данных на HTTP сервер, например, когда вы заполняете HTML форму на сайте.

4	PUT
HTTP запросы с методом PUT сохраняются под запрашиваемым URI. То есть метод PUT используется для замены контента.

5	DELETE
Метод DELETE при HTTP запросе позволяет запросить сервер удалить данные ресурса, указанного в URI.

6	CONNECT
HTTP запрос с методом CONNECT позволяет установить  туннель к серверу, который указан в URI.

7	OPTIONS
HTTP запрос с методом OPTION позволяет получить параметры для связи с ресурсом.

8	TRACE
При HTTP запросе с методом TRACE можно отследить то, что происходит с вашими запросами.
'''