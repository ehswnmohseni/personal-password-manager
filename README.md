# Personal Password Manager (for Windows)!

This is a Python-based password manager designed to securely store and retrieve your sensitive information 
-   This is a simple **Python application** designed to securely store and manage your passwords.
-   Your passwords are **encrypted** and stored within the application.
-   To access the application, you must pass both password and **facial recognition** authentication.
-   For security reasons, the application operates entirely **offline**.
-   To enhance security, the file encryption is updated every **24 hours**.
- If the application detects a potential hacking attempt, it will **delete** all critical files.

**Personal Password Manager** uses [cryptography](https://github.com/pyca/cryptography) library for data encryption and [deep face library](https://github.com/serengil/deepface/) for facial detection.

# Install on Windows :

Here's how to install the project step by step :
1. if you have git to install project 

    git clone https://github.com/ehswnmohseni/personal-password-manager.git
    
2. to open project file :
	
    cd personal-password-manager

3. to install requirements 
    
    pip install -r requirements.txt

4. to run project 

    python main.py

5. for open the program you need skip face recognition for this Copy your desired facial image and name it 'pattern.jpg'. Save it to the following address C:\Users\{your_pc}\Pictures\images\pattern.jpg

6. Please also save a copy of your image key as 'key.jpg' in the same folder as the previous image.

7. and open face.py in project with your ide to change the pictures address :
 
in face.py line 13,14 modify the address with your OS name like this 

     pattern = C:\Users\ehsan\Pictures\images\pattern.jpg
     image = C:\Users\ehsan\Pictures\images\key.jpg

replace your OS name with ehsan


> Please ensure that the face saved as 'pattern' is identical to the
> face saved as 'key'. Both images should be of the same person and will
> be used to unlock the program. Note that the 'key' image will be
> deleted after each successful login.

8. for first login your password is **admin** after login you can change your password.

**now you can use personal password manager in windows!**

## add password to your password manager 

after login you can enter "add" syntax to add new password to your passwords list 
first : enter name of password for example instagram 
then : enter password you like 

## change login password 

after login you can enter "change" syntax to change your login password
first : Enter your current password
then : Enter your new password

## see list of password

after login you can enter "list" syntax to see your all passwords 
when you input the password name, the program will return the password to you

> Please note that the password will be available to you for ten seconds

## exit from program 

you can enter "exit" syntax to exit from password manager
