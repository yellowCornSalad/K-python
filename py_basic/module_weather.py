# read module

from flask import Flask
# import links to read
from urllib import request
from bs4 import BeautifulSoup

# create web server
app = Flask(__name__)
@app.route("/")

def hello():
    # read weather from '기상청' with urlopen()
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeautifulSoup를 이용해 페이지 분석
    soup = BeautifulSoup(target, "html.parser")

    # search location tag
    output = ""
    for location in soup.select("location"):
        # search & print <city>, <wf>, <tmn>, <tmx>
        output += "<h3>{}</h3>" .format(location.select_one("city").string)
        output += "날씨: {}<br/>" .format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                    location.select_one("tmx").string\
                        )
        output += "<hr/>"
    return output