# DTDC-Shipment-tracker

This is a script which automatically checks the current status of your shipment. This works with the [DTDC](https://www.dtdc.in/) (India) website.

The script may not work with the current version of the website and browser (chrome here), as they change periodically. It is just a demo of how many things could be automated with python.  

What it does is, it fetches the shipment tracking number from an image of the invoice using tesseract OCR and then using selenium, it checks the current status of the shipment and saves a screenshot of it.

This is the [Sample Video](https://www.youtube.com/watch?v=k2Xk5HjsvWY&feature=youtu.be) 

This tracker uses following python modules which need to be installed from PyPI:

 - [Selenium](https://pypi.org/project/selenium/)
 - [pytesseract](https://pypi.org/project/pytesseract/)
 - [Selenium-Screenshot](https://pypi.org/project/Selenium-Screenshot/)
 
You will also need to install [tesseract](https://github.com/tesseract-ocr/tesseract) OCR executable on your computer.


> Written with [StackEdit](https://stackedit.io/).
