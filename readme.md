Author : Adrian Shikwambana(Consume Github API)  

Instructions  
1. Git Clone The Project  
2. Create your own virtual environment :  
    a) You can create virtual environment using the latest version of python on your machine using:  
    - mkvirtualenv "name of the virtualenv" without the quotation  marks
    b) You can create virtual environment specifying the python version you want:  
    - mkvirtualenv -p $(which python3.7) "name of your virtualenv" without the quotation marks.  
    c) Activate your virtual environment:  
    - workon "name of your virtualenv" without quotation marks  
3. Install the requirements using:  
    pip install -r requirements.txt in your shell.  

Accessing Your Github repos  
- You can either use your credentials or use an access token.
1. Generate a github token, see link to generate a token:  
    https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token  
2. You can use your credentials but they are depreciated.  

Running the application  
1. Open the env.sh file   
2. Paste in your access token or  
3. Use your credentials and paste in your username and password  
4. Before opening your text editor, open your terminal and source your environment variables, using :  
- source env.sh  
5. open the project and run it with a text editor of your choice.  




