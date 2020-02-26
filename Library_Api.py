#################################################################################################
############ Projet 'Ma petite Librairie' -- Meidi KADRI
#################################################################################################

import requests
import json

##################################################################################################
############## Question 1
##################################################################################################

rBooks = requests.get('https://demo.api-platform.com/books?order[publicationDate]=desc&page=1')
if rBooks.status_code == 200 :
    dataBooks = rBooks.json()
    for i in range(10) :
        titre = dataBooks['hydra:member'][i]['title']
        date = dataBooks['hydra:member'][i]['publicationDate']
        print(f'Titre : {titre} - {date}')
else : 
    print('Error')

##################################################################################################
############## Question 2
##################################################################################################

searchAuthor = 'Dr. Kaitlyn Ratke'
rAuthor = requests.get('https://demo.api-platform.com/books?author=' + searchAuthor)

if rAuthor.status_code == 200 :
    datAuthor = rAuthor.json()
    for i in range(len(datAuthor['hydra:member'])) :
        titre = datAuthor['hydra:member'][i]['title']
        print(f'Titre de l\'auteur {searchAuthor} est {titre}')
else :
    print('Error')

##################################################################################################
############## Question 3
##################################################################################################

searchComment = '1d52ba85-97c8-4cc3-b81a40582f3aff64'
rComment = requests.get('https://demo.api-platform.com/books/'+ searchComment + '/reviews?page=1')

if rComment.status_code == 200 :
    dataComment = rComment.json()
    for i in range(len(dataComment['hydra:member'])) :
        comment = dataComment['hydra:member'][i]['body']
        print(f'Commentaire n°{i+1} : {comment}')
else :
    print('Error')

##################################################################################################
############## Question 4
##################################################################################################

searchAddComment = '1b08c9ab-6254-4015-ad14-bac3e5c008df'
dataToload = {
"body": "Beat Da Street !",
"rating": 5,
"author": "Meidi",
"publicationDate": "2020-01-10T08:12:07.907Z",
"book": "/books/" + searchAddComment
}
postComment = requests.post('https://demo.api-platform.com/reviews', json = dataToload)

##################################################################################################
############## Question 5
##################################################################################################

postJSON = postComment.json()
postid = postJSON['@id'].split('/')[-1]

putDataComment = {
"body": "Yeah it's like I said, BEAT DA STREET Men !!!!",
"rating": 5,
"author": "Meidi",
"publicationDate": "2020-01-10T08:12:07.907Z",
"book": "/books/" + searchAddComment
}

putComment = requests.put('https://demo.api-platform.com/reviews/' + postid, json = putDataComment)