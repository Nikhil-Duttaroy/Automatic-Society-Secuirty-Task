# Facial-Recognition
This a Facial Recognition Software Developed for Housing Society security.

### Main Features
1. Add Residents of the society to ML Model
2. Automatic Detection of Society Members along with Entry Timestamp and Temperature.
3. Adding Images , Timestamp , Name ,Address , Phone Number of New Visitors.
4. Representation of FlatNo With time and temperature in Table and Charts.

### Prerequisites
1. Python 3.8.x
2. OpenCv
3. Flask
4. Mysqlite Db


### How to use
1. Open App.py (This will open a Website with the User interface).
2. Access Admin Panel (username=admin , password=1234).
   * Click on Add to dataset option and fill up the form with user details.
   * After Filling the Form the Camera with take Pictures of the Person(Tip:Person Should look in each direction for atleast 10secs).
   * After Adding all the Users use the train option and wait for the ml model to train.
   * After this we are all set to go.
3.Access the home page and use the Detect Button for Facial Recognition.
   * Every User Detected will be Reflected in the User details tab of the admin Panel.

##### Make Sure to Export the Database in the Folder.
