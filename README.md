This git repo is basically Part 1 of the 3-Part full-stack data science project of Human Activity Recogntion. The entire project was designed with one particular use case in mind: an simple iOS App consuming phone sensor data (accelerometer, gyroscope, etc..) fetched from the phone itself and utilizing a trained ML model to make inference from those fetched data about the activity of the human being

**Part 1:** Collecting phone sensor data wirelessly with basic iOS App (built with Kivy) and Websocket Server
**Part 2:** Building and Fine Tuing Neural Net Model with Keras/TensorFlow and "Weight and Bias"
**Part 3:** Deploying Keras Model on iOS device (CoreML and TF Lite) (upcoming)

########################################################################################################################################################

# PART 1: DATA COLLECTION
I have almost very little experience with Kivy and Websocket when I had this idea of collecting data wirelessly. This part of the project would not have been possible without the turtorial from: [link text](https://www.youtube.com/watch?v=uv8PciALzSI)


A couple of lessons and modification I had achieved throghout this part:
- Learn about different communication prototcol of edge devices
- Change the sampling rate of the sensor data and include extra attribute/features on the client script to make it more similar to a public HAR dataset
- Change the server script to stop the streaming period after certain amount of time and write to a JSON file

