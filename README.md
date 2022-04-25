# Restaurant Finder

Restaurant Finder is a console application that helps very busy and very hungry people to find a restaurant that fits
their full calendar with meetings.  
When the application starts, the list of the now opened restaurant is displayed. The user has five options.

* The first option is pressing 1 to find all opened restaurants with specific times and days. Next, the user needs to
  specify the time (HH:MM), and after that, need to enter the number of day in the week (counting as a real programmer,
  0
  is Monday).
* The second option is to press 2 to find all information about a specific restaurant. The application will prompt the
  user to enter the restaurant's name and that he wishes to know more about the restaurant.
* The third option is to press 3 to find a restaurant with specific cuisine. Upon pressing 3, the application will
  display
  the list of all types of cuisines, and the user can choose his favorite cooking style. After entering the style, the
  application will display the list of all restaurants with specified cuisine.
* The fourth option is just pressing enter, and the application will display once again all opened restaurants.
* The last option is to press four, and the application will exit.

### Running the application

The application was developed and tested with python 3.10. Therefore, no extra packages need to be installed to run the
application.
If you don't have installed python 3.10, you don't need to install it. You can just build a docker image and run it.

##### Docker
1. Go to the project's root directory, where the docker file location is.
2. build docker image ``docker build -t <image-tag> .``
3. run application ``docker run -t <image-tag>``

##### Terminal
1. Go to the project's root directory, where the file **main.py** is located.
2. ``python3 ./main.py``