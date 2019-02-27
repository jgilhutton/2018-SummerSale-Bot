import requests
from re import search
from time import sleep,clock

hostnameApi = 'community.steam-api.com'
hostnameCommunity = 'steamcommunity.com'
cookies = {}
scores = {'1':585,'2':1170,'3':2340,'4':4680}
token = ''
planeta = 12
verify = True
setTimer = True
preTime = 0
errores = 0

def joinPlanet(id,token):
    headersJoinPlanet = {
        'Host': hostnameApi,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://steamcommunity.com',
        'DNT': '1',
        'Connection': 'close',
    }
    postdata = 'id={}&access_token={}'.format(id,token)
    res = requests.post('https://community.steam-api.com/ITerritoryControlMinigameService/JoinPlanet/v0001/',
    headers = headersJoinPlanet,
    data = postdata,
    verify = verify
    )
    return res

def getCurrentPlanet(token):
    headersGetPlayerData = {
        'Host': hostnameApi,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://steamcommunity.com',
        'DNT': '1',
        'Connection': 'close',
    }
    postdata = 'access_token={}'.format(token)
    res = requests.post('https://community.steam-api.com/ITerritoryControlMinigameService/GetPlayerInfo/v0001/',
    headers = headersGetPlayerData,
    data = postdata,
    verify = verify
    )
    regex = '(?i)(?<="active_planet":")\d{1,2}(?=","time_on_planet")'
    currentPlanet = search(regex,res.text)
    if currentPlanet:
        return int(currentPlanet.group())
    else:
        return False

def getToken():
    headersGetToken = {
        'Host': hostnameCommunity,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    }
    res = requests.get('https://steamcommunity.com/saliengame/gettoken',
                        cookies = cookies,
                        headers= headersGetToken,
                        verify = verify
                        )
    token = search('(?<="token":")[a-f,0-9]{32}(?=",")',res.text)
    if token.group(): return token.group()
    else: return False

def joinZone(position,token):
    headersJoinZone = {
        'Host': hostnameApi,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://steamcommunity.com',
        'DNT': '1',
        'Connection': 'close',
    }
    postdata = 'zone_position={}&access_token={}'.format(position,token)
    res = requests.post('https://community.steam-api.com/ITerritoryControlMinigameService/JoinZone/v0001/',
    headers = headersJoinZone,
    data = postdata,verify = verify)
    return res

def getNotification():
    headersNotification = {
        'Host': hostnameCommunity,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'close',
    }
    res = requests.get('https://steamcommunity.com/actions/GetNotificationCounts',
                        cookies = cookies,
                        headers = headersNotification,
                        verify = verify
    )
    return res

def reportScore(score,token):
    headersScore = {
        'Host': hostnameApi,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://steamcommunity.com',
        'DNT': '1',
        'Connection': 'close',
    }
    postdata = 'access_token={}&score={}&language=spanish'.format(token,score)
    res = requests.post('https://community.steam-api.com/ITerritoryControlMinigameService/ReportScore/v0001/',
    headers=headersScore,
    data = postdata,
    verify = verify
    )
    return res

def leavePlanet(id,token):
    headersLeavePlanet = {
        'Host': hostnameApi,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://steamcommunity.com',
        'DNT': '1',
        'Connection': 'close',
    }
    postdata = 'access_token={}&gameid={}'.format(token,id)
    res = requests.post('https://community.steam-api.com/IMiniGameService/LeaveGame/v0001/',verify = verify,data=postdata,headers=headersLeavePlanet)
    return res

def getPlanetInfo(id):
    headersPlanetInfo = {
        'Host': hostnameApi,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'Origin': 'https://steamcommunity.com',
        'DNT': '1',
        'Connection': 'close',
    }
    res = requests.get('https://community.steam-api.com/ITerritoryControlMinigameService/GetPlanet/v0001/?id={}&language=spanish'.format(id),
    headers=headersPlanetInfo,verify = verify)
    planetData = res.text
    regex = '(?s)(?P<zona>(?<=zone_position":)\d+(?=,"leader))(?:.*)(?P<dificultad>(?<=difficulty":)[1-4](?=,"captured))(?:.*)(?P<capturado>(?<=captured":).{4,5}(?=,"capture_progress"))'
    planetData = planetData.split('boss_active":false')
    zonas = []
    for i in planetData:
        zona = search(regex,i)
        if zona and zona.group('capturado') == 'false':
            data = {'idZona':zona.group('zona'),'dificultad':zona.group('dificultad')}
            zonas.append(data)
    return sorted(zonas,key = lambda x: x['dificultad'],reverse = True)

def chooseBestPlanet():
    headersPlanetInfo = {
        'Host': hostnameApi,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': '*/*',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://steamcommunity.com/saliengame/play',
        'Origin': 'https://steamcommunity.com',
        'DNT': '1',
        'Connection': 'close',
    }
    res = requests.get('https://community.steam-api.com/ITerritoryControlMinigameService/GetPlanets/v0001/?active_only=1&language=spanish',
    headers=headersPlanetInfo,verify = verify)
    regex = '(?s)(?P<id>(?<="id":")\d{1,2}(?=","state))(?:.*)(?P<nombre>(?<="name":").+(?=","image_filename"))(?:.*)(?P<porcentaje>(?<="capture_progress":)0\.\d+(?=,"total_joins))'
    planets = []
    for planet in res.text.split('}]},{'):
        data = search(regex,planet)
        if data:
            planets.append({'nombre':data.group('nombre'),'idPlanet':data.group('id'),'progreso':data.group('porcentaje')})
    planetsSorted = sorted(planets, key = lambda x: float(x['progreso']))
    return planetsSorted[0]

if not token:
    token = getToken()
    print('Token:',token)

currentPlanet = getCurrentPlanet(token)
print('Planeta actual: {}'.format(currentPlanet))
# if currentPlanet:
#     leavePlanet(currentPlanet,token)

if not planeta:
    planetaData = chooseBestPlanet()
    planeta = int(planetaData['idPlanet'])
    planetaNombre = planetaData['nombre']
    print('Entrando en planeta {}, id={}'.format(planetaNombre,planeta))
else:
    print('Entrando en planeta {}'.format(planeta))

joinPlanet(planeta,token)
pretime = 0.0
clock()

while True:
    try:
        zonas = getPlanetInfo(planeta)
        zonaActual = zonas[0]
        print('Jugando en zona',zonaActual['idZona'],'con dificultad',zonaActual['dificultad'])

        while True:
            c = 0
            joinZone(zonaActual['idZona'],token)
            sleep(10)
            for _ in range(4):
                getNotification()
                sleep(30)
            getNotification()
            while True:
                update = reportScore(scores[zonaActual['dificultad']],token).text
                if update == '{"response":{}}':
                    if c == 3: 
                        raise
                    c += 1
                    sleep(2)
                    continue
                else:
                    print(update)
                    break

    except KeyboardInterrupt:
        break
    except Exception as e:
        errores += 1
        if errores == 1000:
            exit()
        print('Posible zona completa. Cambiando de zona...',type(e),e)
        continue
