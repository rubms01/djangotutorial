from django.http import HttpResponse

def index(request):
    url = """
        <html> 
        <head>
        </head>
        <body>
            <h1>메인 페이지입니다.</h1>
            <div>
                <a href = "http://127.0.0.1:8000/a">A 페이지입니다.</a>
                <a href = "http://127.0.0.1:8000/b">B 페이지입니다.</a>
                <a href = "http://127.0.0.1:8000/c">C 페이지입니다.</a>
                <a href = "http://127.0.0.1:8000/movies">영화 소개개 페이지입니다.</a>
            </div>
        </body>
        </html>
        """
    return HttpResponse(url)

def a(request):
        apage = """
        <html> 
        <head>
        </head>
        <body>
            <h1>A 페이지입니다.</h1>
        </body>
        </html>
        """
        return HttpResponse(apage)

def b(request):
        bpage = """
        <html> 
        <head>
        </head>
        <body>
            <h1>B 페이지입니다.</h1>
        </body>
        </html>
        """
        return HttpResponse(bpage)


def c(request):
        cpage = """
        <html> 
        <head>
        </head>
        <body>
            <h1>C 페이지입니다.</h1>
        </body>
        </html>
        """
        return HttpResponse(cpage)

def introduce(request):
        introduce_page = """
        <html> 
        <head>
        </head>
        <body>
            <h1>영화 페이지입니다.</h1>
        </body>
        </html>
        """
        return HttpResponse(introduce_page)