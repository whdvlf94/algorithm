from datetime import datetime

class Photo(object):
    def __init__(self, name:str, city:str, time:str):
        self.name = name
        self.city = city
        self.time = time

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city


def solution(S):
    data = {}
    photos = []
    s = S.split("\n")
    for i in s:
        name, city, time = i.split(",")
        photo = Photo(name.replace(" ",""), city.replace(" ",""), time.replace(" ",""))
        photos.append(photo)

    for i in photos:
        city = i.get_city()
        if data.get(city) is None:
            data[city] = []        
        data[city].append(i)

    answer = ""
    for i,v in enumerate(photos):
        city_photos = data[v.get_city()]
        city_photos.sort(key=lambda x: datetime.strptime(x.time, "%Y-%m-%d%H:%M:%S"))
        counter = city_photos.index(v)+1
        if len(city_photos) >= 10:
            counter = f"0{counter}"
            if counter == 10:
                counter.strip("0")
        answer += f"{v.get_city()}{counter}.{v.get_name().split('.')[1]}" + "\n"
    return answer


S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'

print(solution(S))