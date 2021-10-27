from django.shortcuts import render
from flask import render_template
# def get_html_content(request):
#     import requests
#     city = request.GET.get('city')
#     city = city.replace(" ", "+")
#     USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
#     LANGUAGE = "en-US,en;q=0.5"
#     session = requests.Session()
#     session.headers['User-Agent'] = USER_AGENT
#     session.headers['Accept-Language'] = LANGUAGE
#     session.headers['Content-Language'] = LANGUAGE
#     html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text
#
#     return html_content

# def home(request):
#     result = None
#     if 'city' in request.GET:
#         # fetch the weather from Google.
#         html_content = get_html_content(request)
#         from bs4 import BeautifulSoup
#         soup = BeautifulSoup(html_content, 'html.parser')
#         result = dict()
#         # extract region
#         result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
#         # extract temperature now
#         result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
#         # get the day, hour and actual weather
#         result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split(
#             '\n')
#     return render(request, 'core/core.html', {'result': result})

def get_html_content(request):
    import requests
    drama = request.GET.get('drama')
    drama = drama.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={drama}').text

    return html_content

def home(request):
    result = None
    if 'drama' in request.GET:
        html_content = get_html_content(request)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()

        try:
            result['name'] = soup.find("strong", attrs={"class": "_text"}).text
            result['story'] = soup.find("span", attrs={"class": "desc _text"}).text
            result['ratio'] = soup.find("em", attrs={"class": "value"}).text
            img = soup.find("div", {"class":"detail_info"})
            result['image'] = img.find("img")["src"]
            
            # result['res2'] = soup.find("div",{"class":"cm_info_box scroll_img_vertical_105_148"}).select('li > div > a > div > img')
            # result['res2'] = soup.find("div",{"class":"cm_info_box scroll_img_vertical_105_148"}).select('img')
            res = soup.find("div",{"class":"cm_info_box scroll_img_vertical_105_148"}).select('img')
            result['res3'] = str(res).replace(',',"").replace(']',"").replace('[',"")
            
      
        except Exception as e:
            # print()
            return  render(request, 'core/exception.html')
        
    return  render(request, 'core/core.html', {'result': result})

