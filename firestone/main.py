import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from video_id import video_id
from datetime import datetime
cred = credentials.Certificate("kien-226a6-firebase-adminsdk-b0z33-c932174696.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# start_t = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
# stop_t = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
# db.collection('car').document('mediumspeed').set({'owner':'bach', 'color':'green', 'type':'kia'})
# db.collection('car').document('highspeed').set({'owner':'kien', 'color':'red', 'type':'mustang'})
# db.collection('car').document('lowspeed').set({'owner':'hung', 'color':'blue', 'type':'bus'})
# db.collection('car').document('lowspeed').update({'price':1000})
# db.collection('car').document('mediumspeed').update({'price':2000})
db.collection('car').document('highspeed').collection('kien').document('mycar').set({'price':5000})
# car_q= db.collection('car').where("price", "<", 5000).get()
name = 'gimbaldemo'
car_q = db.collection(name).where('status', '==', 'waitFTQC').get()
#print(car_q)
array =[]
for car_q in car_q:
    car_feild = car_q.to_dict()
    #print(car_q.id)
    array.append(car_q.id)
textfile = open("a_file.txt", "w")
for element in array:
    textfile.write(element + " ")
textfile.close()
print(array)
    # db.collection('car').document(car_q.id).update({'owner':'hihi','year': 1098})

'''
video="video1"
vid = video_id(video) #tao ra collection video moi khi muon doi ten
data_video ={
     vid[0]:1,vid[1]:'green',
     vid[2]:10,vid[3]: 10,
     vid[4]:10,
     vid[5]:10,vid[6]: 12,
     vid[7]:10,vid[8]:10
     }

#
id = '893610149013'
data ={
     "prototype":2,
     "qcResult.qcTestBay.VideoAnalytics.893610149013_0.ITF":10,
     "qcResult.qcTestBay.VideoAnalytics.893610149013_0.Max.dx":10,
     "qcResult.qcTestBay.VideoAnalytics.893610149013_0.Max.dy":10,
     "qcResult.qcTestBay.VideoAnalytics.893610149013_0.Max.Horizon":10,
     "qcResult.qcTestBay.VideoAnalytics.893610149013_0.SDx":10,
     "qcResult.qcTestBay.VideoAnalytics.893610149013_0.SDy":11

}
gimbal_893610149013 = db.collection('gimbaldemo').document(id)
gimbal_893610149013.update(data)
#db.collection('gimbaldemo').document('893610149013').set({'owner':'bach', 'color':'green', 'type':'kia'})
#db.collection('gimbaldemo').document('872767007673').set({'owner':'bach', 'color':'green', 'type':'kia'})
'''
# scan new owner -> tim duoc document cuar owner -> update lai bang document do


