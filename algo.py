


def sortRequest (request, dataCenterLatence, cacheDic, videoDic, weightVideoDic):
    """ cacheDic : dico indexé par les endpoints, valeur doublet cache et latence entre le cache
                   et le endpoints
        videoDic :dico indexé par les endpoints, valeurs liste id des vidéos qu'il
        veut regarder.
        request : matrice request[endpoint][idVideo] = nombre de requetes
        weightVideoDic
        """

    savedTime = []

    for endpoint, idVideos in videoDic.items():

        for idVideo in idVideos:

            endpointCacheandLatence = cacheDic[endpoint]

            for tuples in endpointCacheandLatence:

                    idcache, latenceCacheEndpoint = tuples

                    saveTime = dataCenterLatence[endpoints] -  latenceCacheEndpoint
                    saveTime = saveTime * request[endpoint][idVideo]
                    saveTime = saveTime / weightVideoDic[idVideo]

                    savedTime.append([savedTime, endpoint, idcache, idVideo])

    savedTime = sorted(saveTime, reverse=True)

    return savedTime

def affectation(savedTime, capacityCacheConst, cacheDic, videoDic,
                nbCache, nbEndpoints, weightVideoDic):

    capacityCache = []
    for i in range(nbCache):
        capacityCache[i] = capacityCacheConst

    affected = {}

    for endpoint in range (nbEndpoints):

        videoEndPoint = {}

        for idVideo in videoDic[endpoint]:

            videoEndPoint[idVideo] = False

        affected[endpoint] = videoEndPoint


    cacheResult = {}

    for i in range (nbCache):
        cacheResult [i] = []

    for tuples in savedTime :

        savedTime, endpoint, idCache, idVideo = tuples

        if capacityCache[idCache] - weightVideoDic[idVideo] >= 0:

            cacheEndpoint = cacheDic[endpoint]

            i = 0
            find = False :

            while find == False and i < len(cacheEndpoint):

                subIdCache = cacheEndpoint[i][0]

                if idVideo in cacheResult[subIdCache] :
                    find = True

                i += 1

            if find == False :

                capacityCache[idcache] -= weightVideoDic[idvideo]
                affected[endpoint][idVideo] = True
                cacheResult[idCache].append(idVideo)

        return cacheResult
