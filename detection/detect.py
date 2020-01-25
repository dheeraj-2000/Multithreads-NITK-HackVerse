from clarifai.rest import ClarifaiApp ,Video
import unicodedata

app = ClarifaiApp(api_key="1ed137256fde4eb08dc79847c0506eef")





#general model
model = app.public_models.general_model
# givefilename
response = model.predict_by_filename('/home/som/Desktop/leopard.jpg')

#if url is given
#response = model.predict_by_url(url='https://i.pinimg.com/236x/db/9e/5c/db9e5ce4fe74df303529e02345584b42--habitats-state-parks.jpg')
model1 = app.models.get('animals')
model1.model_version = '0b3770d9cc8e47b7b1d3799831b31c1e'
custom_response = model1.predict_by_filename('/home/som/Desktop/leopard.jpg')
#custom_response = model1.predict_by_url(url='https://i1.wp.com/npnews24.com/wp-content/uploads/2018/12/image.png')


#print(custom_response)
model = app.models.get('general-v1.3')
#video = Video(filename='/home/som/Downloads/video1.mp4')

#print(response.encode)

concepts = response['outputs'][0]['data']['concepts']
concepts2 = custom_response['outputs'][0]['data']['concepts']
for concept in concepts:
           print(concept['name'].encode('ascii','ignore'),) 