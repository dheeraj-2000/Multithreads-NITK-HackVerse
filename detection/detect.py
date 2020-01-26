from clarifai.rest import ClarifaiApp ,Video
import unicodedata

def detect_animals (D):
    count = 0
    app = ClarifaiApp(api_key="YOUR_APK")





    #general model
    model1 = app.public_models.general_model
    # givefilename
    #response = model.predict_by_filename('/home/som/Desktop/leopard.jpg')

    #if url is given
    #response = model.predict_by_url(url='https://i.pinimg.com/236x/db/9e/5c/db9e5ce4fe74df303529e02345584b42--habitats-state-parks.jpg')
    #model1 = app.models.get('animals')
    #model1.model_version = '0b3770d9cc8e47b7b1d3799831b31c1e'

    custom_response = [0 for i in range(1,11)]
    for i in range (1,11):
        custom_response[i-1] = model1.predict_by_filename('Picture' + str(i) + '.jpg')
        #custom_response = model1.predict_by_url(url='https://i1.wp.com/npnews24.com/wp-content/uploads/2018/12/image.png')


    #print(custom_response)
    #model = app.models.get('general-v1.3')
    #video = Video(filename='/home/som/Downloads/video1.mp4')

    #print(response.encode)

    #concepts = response['outputs'][0]['data']['concepts']
    for i in range (10):
        concepts2 = custom_response[i]['outputs'][0]['data']['concepts']
        if count > 0:
            break
        for concept in concepts2:
            if concept['name'] == 'animal' and concept["value"] >= 0.70 or concept['name'] == 'cheetah' and concept["value"] >= 0.70 or concept['name'] == 'leopard' and concept["value"] >= 0.70 or concept['name'] == 'elephant' and concept["value"] >= 0.70 or concept['name'] == 'mammal' and concept["value"] >= 0.70 or concept['name'] == 'wildlife' and concept["value"] >= 0.70 :
               D[concept['name']] = D[concept['name']] + 1
               print(concept['name'].encode('ascii','ignore'),concept['value']) 
               count = count+1
               #print(count)
    
    return D,count
