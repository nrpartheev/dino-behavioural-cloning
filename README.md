# CHROME DINO GAME - BEHAVIOURAL CLONING

#### Behavioral cloning 101
Behavioral cloning is one of the feild of supervised learning in which we train the model on observed state and the respective actions for it. Whenever the trained model is provided with a new state the model will find a probability for each action and the action with the highest probability is considered the predict one.

Behavioural cloning in video games can be seperated into 3 goals
- Short term (CNN) --> Dino game --> this repo  
- Medium term (CNN + LSTM) --> snake game --> check out the repo in my profile 
- Long term 

## Short term goals (i.e Jumping in Dino game)

It is not a secret that the dinosaur in the chrome game has to jump over the cactus just by looking at a single frame.. We don't have to carry the information from the previous frame.. but there are other game like snake game in which we must carry the information from the previous frames. This is because we have to find out the present snake direction to predict the future action. 

## Project info
- STEP 1 : Data collection
- STEP 2 : Model training
- STEP 3 : Model prediction 

## STEP 1:

For training the model we have to use data the is collected while playing the game.. it is really important for different people to play that game.. this is to reduce the bias that is created if we use the same players data..

the file data_collection.py is used for collecting the data.

## STEP 2:

Model training is present in the .ipynb file.. The code is not different from that of a classification model. we are using a ALEXNET for this purpose after we use Yolo-v8 to remove the noise..

## STEP 3:

The downloaded model in the .h5 file can be used for predicting the action for each frame.



