# ImageRecognition
This project is developed to use the IBM Watson's API to carry out image recognition

The keynotes of the project is:-

1) Gather images of objects you want to work on

2) Once accumulated, then feed those images to IBM Watson API

3) Once, the IBM Watson is trained then you can give in images you want to search and check its probability against the given parameters



Procedural steps to be carried out:-

1) Make an account on IBM Cloud, create a project under the Vision API
2) Go to service credentials, and then create new credentials to get the api keys
3) Gather url of images you want to work on, and then using image_retriever.py download them in a folder
    
    -> python image_retriever.py url_file.txt File_Name
4) Once the folders are ready, compress them into a zip file
5) Upload these zip file to the IBM CLoud using this command in the terminal

    -> curl -X POST -F "batman_positive_examples=@Batman.zip" -F "superman_positive_examples=@Superman.zip" -F "wonderwoman_positive_examples=@WonderWoman.zip" -F "aquaman_positive_examples=@Aquaman.zip" -F "name=Credentials-1" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key={api_key}&version=2016-05-20"

    (Change the parameters accordingly)

6) While IBM cloud is training you can check the progress using this command in the terminal

    -> curl -X GET "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/{classifier_id}?api_key={api_key}&version=2016-05-20"

    (Change the parameters accordingly)

7) Once the IBM Cloud is done training then you can use the following command in the terminal

    -> curl -X GET -H "Accept-Language: en" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key={api_key}&url={url}&classifier_ids={classifier_id}&owner=me&threshold=0&version=2016-05-20"
    
     (Change the parameters accordingly)
     
     
Further Reference :- 

A complete descriptive video on how to properly carry out this project -
  
  https://www.youtube.com/watch?v=FYZld6SSCnY 
  
  
If there is any problem mail me at - anand1996aditya@gmail.com
