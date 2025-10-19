# WEBSCRAP THE BCV FOR CURRENCY PRICE

## Instructions

1. Add your credentials.json from the sheets API to the src folder
2. Create a .env file in the root folder (BCV-WS-SHEETS) and fill the following variables within:

- SHEET_ID="Insert here yout GOOGLE SHEET ID (followed by /d/ in the url)"

3. Add the name of your sheet to the variable SHEET_NAME in main.py

4. Remember to create your venv folder `python -m venv venv` and activate it Windows-bash: `source ./venv/Script/activate` OS: `source venv/bin/activate` Powershell: `./venv/Script/Activate.ps1`

5. Install the dependencies: `pip install -r requirements.txt`
6. Run the code and follow the prompts: `python main.py`

Remember to deactivate the venv at the end: `deactivate`
