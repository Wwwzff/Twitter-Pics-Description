import pymongo

def searchbykeyword(keyword):
    conn = pymongo.MongoClient('127.0.0.1',27017)
    db = conn.MiniProject3
    my_set = db.twitterAPI
    for info in my_set.find({"$or":[{"twitter ID":keyword},{"Descriptor":keyword}]}):
        print(info)

def picsperfeed():
    conn = pymongo.MongoClient('127.0.0.1',27017)
    db = conn.MiniProject3
    my_set = db.twitterAPI
    b = my_set.aggregate([{"$group":{"_id":"average","value":{"$avg":"$Pictures"}}}])
    print(list(b)[0])

def mostFrequent():
    conn = pymongo.MongoClient('127.0.0.1',27017)
    db = conn.MiniProject3
    my_set = db.twitterAPI
    c = my_set.aggregate([{"$group":{"_id":"$Descriptor","Frequency":{"$sum":1}}}])
    print(list(c)[0])


searchbykeyword('black')
picsperfeed()
mostFrequent()