import requests
city = "Moscow,RU"
city_id = 524901
appid = '8ab76178d44d7ceb58b676c18fb9bb33'


def weather_report():
    n = 0
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'id': city_id, 'units': 'metric',
                                                                                      'lang': 'ru', 'APPID': appid})
        dictdata = res.json()
        datalist = []
        icondict = {
            '01d': '\uE04A', '01n': '\U0001F311', '02d': '\U0001F325',    '02n': '\U0001F325', '03d': '\uE049',
            '03n': '\uE049', '04d': '\uE049', '04n': '\uE049', '09d': '\U0001F327', '09n': '\U0001F327',
            '10d': '\U0001F326', '10n': '\U0001F326', '11d': '\U0001F329', '11n': '\U0001F329',
            '13d': '\u2744', '13n': '\u2744', '50d': '\U0001F32B', '50n': '\U0001F32B'
                    }

        for i in dictdata['list']:
            datetime = i['dt_txt']
            temp = round(i['main']['temp'], 1)
            feelslike = round(i['main']['feels_like'], 1)
            wind = round(i['wind']['speed'], 1)
            weatherdescription = i['weather'][0]['description']
            iconcode = i['weather'][0]['icon']
            datalist.append(datetime)
            datalist.append(temp)
            datalist.append(feelslike)
            datalist.append(wind)
            datalist.append(weatherdescription)
            datalist.append(iconcode)
            n += 1
            if n == 5:
                break

        if datalist[5 or 11 or 17 or 23 or 29] == '04d' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '04n' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '09d' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '09n' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '10d' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '10n' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '11d' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '11n' in datalist:
            reportcomment = 'Сегодня возможен дождь, прихвати зонтик на всякий.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '13d' in datalist:
            reportcomment = 'Сегодня, возможно, будет снежок.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '13n' in datalist:
            reportcomment = 'Сегодня, возможно, будет снежок.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '50d' in datalist:
            reportcomment = 'Возможно, будет туман. Будь осторожнее.'
        elif datalist[5 or 11 or 17 or 23 or 29] == '50n' in datalist:
            reportcomment = 'Возможно, будет туман. Будь осторожнее.'
        else:
            reportcomment = 'Осадков не ожидается.'

        reportmessage = (
                f'{datalist[0]}\nТемпература на улице {datalist[1]}°C,\nощущается как {datalist[2]}°C.\n'
                f'Скорость ветра {datalist[3]}м/с.\nСостояние погоды - {datalist[4]} {icondict[datalist[5]]}, \n\n' +
                f'{datalist[6]}\nТемпература на улице {datalist[7]}°C,\nощущается как {datalist[8]}°C.\n'
                f'Скорость ветра {datalist[9]}м/с.\nСостояние погоды - {datalist[10]} {icondict[datalist[11]]}, \n\n' +
                f'{datalist[12]}\nТемпература на улице {datalist[13]}°C,\nощущается как {datalist[14]}°C.\n'
                f'Скорость ветра {datalist[15]}м/с.\nСостояние погоды - {datalist[16]} {icondict[datalist[17]]}, \n\n' +
                f'{datalist[18]}\nТемпература на улице {datalist[19]}°C,\nощущается как {datalist[20]}°C.\n'
                f'Скорость ветра {datalist[21]}м/с.\nСостояние погоды - {datalist[22]} {icondict[datalist[23]]}, \n\n' +
                f'{datalist[24]}\nТемпература на улице {datalist[25]}°C,\nощущается как {datalist[26]}°C.\n'
                f'Скорость ветра {datalist[27]}м/с.\nСостояние погоды - {datalist[28]} {icondict[datalist[29]]}, \n\n' +
                f'{reportcomment}'
                         )
        return reportmessage
    except Exception as e:
        print("Exception (forecast):", e)
