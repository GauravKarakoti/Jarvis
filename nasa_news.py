import requests



Api_Key = "8G1A4Q4AhrCLqcnw33aD44n1zodeijxRwOojrtb0"




def NASANEWS(Date):
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params = {'date':str(Date)}
    r = requests.get(Url,params = Params)
    Data = r.json()
    info = Data['explanation']
    Title = Data['title']
    Image_url = Data['url']
    Image_r = requests.get(Image_url)
    Filename = str(Date) + '.jpg'
    with open(Filename,) as f:
        f.write(Image_r.content)