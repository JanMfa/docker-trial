# DESIGN
Based on the requirements, I have created the following components:
1. App - consists of the API, where it is the main application
2. Tests - where the testing occurs
3. Resources - where the sample image or video is located
The two components above can be run using command line:
1. Python command line:
    a) python app.py
    b) pthon tests.py 
2. Docker command line that can be run with .sh provided:
    a) On windows: 
        bash run.sh AND bash run_test_in_docker.py
    b) On linux:
        sh run.sh AND sh run_test_in_docker.py
The design consideration mostly comes from the requirements of the project, which is Dockerized API, written in Flask that supports large file (5GB+) uploads.
First of all, I created the API that allows uploading data to the server using Flask. I believe that instead of uploading the whole file at the same time, it is better to upload the file in chunks for big filed like 5GB+. Currently the upload API does not support of uploading 5GB+. The python API is a POST request API that also consists of the front end, where the user can upload their files.
After running the above command, go to your browser and type "http://localhost:5000/upload", click the "Choose File" button, choose the file to be uploaded and press "Upload".
Upon success, you will be able to see the file on app.py path saved in Docker volume or host folder mounted into the container.  
At the end, go to the tests.py file, and change the filename to be the name of the file you uplaoded. Then, run the test file inside the test folder. This test will call the GET request, and made sure your file is saved. 

# HOWTO:
1. Run python app.py or bash run.sh on Poweshell 
2. Go to your browser and type "http://localhost:5000/upload"
3. After the UI load, click the "Choose File" button, choose the file to be uploaded and press "Upload".
4. Upon success, you will be able to see the file on app.py path saved in Docker volume or host folder mounted into the container.  
5. At the end, go to the tests.py file, and change the filename.

# Conclusion
There is some issue with the current implementation, it is not able to save the file. With the given time, I was not able to debug the issue. If given more time, I would like to solve this issue. Additionally, I mentioned in the design section that to upload a huge file of data, I believe that it is better to upload file in chunks. This could be done using file streaming. The current implementation is to upload the file at one time, this is not a good design for large file because there server might crash and unable to handle the request.