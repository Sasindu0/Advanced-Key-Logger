# Advanced-Key-Logger
Welcome to the Advanced-Key-Logger repo. A keylogger is a simple program that records your keyboard and mouse inputs.
This keylogger has additional features,
* Take a screenshot every 10 seconds
* Collect necessary system information
* Send a email to the attacker every 10 seconds with collected information

## Disclaimer: 
This code is provided for educational purposes only. Distributing or using this code for malicious purposes is strictly prohibited. The developer assumes no responsibility for any misuse of this code.

By using this code, you acknowledge and agree to the following:
* You are responsible for understanding the potential impact of this code.
* You will use this code in a legal and ethical manner.
* You will not distribute this code to third parties without their knowledge and consent.


## Requirements
* Install following libraries
1. Python 3.10.4
2. requests
3. pynput
4. PIL
5. email

* This script works only for Windows operating systems.

## Simple Explanation about the files
* **KeyLogger.py:** The script with all additional features.
* **SimpleKeyLogger.py:** The script for only key logging function using different old library called *keyboard*.
* **set.bat:** Simple script for hide the keylogger executable and make automatically execute when windows startup.