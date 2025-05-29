from django.http import HttpResponse

def index(request):
    # return HttpResponse("<h1>메인 페이지입니다.</h1>")
    url = """
        <html> 
        <head>
        </head>
        <body>
            <h1>메인 페이지입니다.</h1>
            <div>
                <a href = "http://127.0.0.1:8000/movies">인터스텔라 페이지입니다.</a>
                <a href = "http://127.0.0.1:8000/movies">기생충 페이지입니다.</a>
                <a href = "http://127.0.0.1:8000/movies">토이스토리 페이지입니다.</a>
            </div>
        </body>
        </html>
        """
    return HttpResponse(url)

def a(request):
    return HttpResponse("<h1>A페이지입니다.</h1>")

def b(request):
    return HttpResponse("<h1>B페이지입니다.</h1>")
    return HttpResponse("오늘의 영화 추천")

def c(request):
    return HttpResponse("<h1>C페이지입니다.</h1>")

def introduce(request):
    return HttpResponse("<h1>소개 페이지입니다.</h1>")