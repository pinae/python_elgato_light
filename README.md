# python_elgato_light
Control Elgato WiFi lights from python

This is basically sample code using the library `leglight`. 
It is tested with the Elgato "Ring Light" but it should also work with the 
"Key Light" and the "Key Light Air". 

You have to pair the Lamps with your WiFi network using the Elgato Control Center App.

## Virtualenv
By installing `leglight` in a virtualenv you make sure not to mess with the python 
packages of your OS. On Linux the commands are as follows:

```bash
python3 -m venv env
source env/bin/activate
pip install -U pip wheel
pip install -r requirements.txt
```

If you want to omit the virtualenv just use the last command. It installs the library.

## Usage
Just run the scripts using the `python` of your virtualenv:

```bash
python standard_setting.py
```

The `broadcast_setting.py` prints some additional information like this:

```plaintext
Elgato Light DW50J1A10436 @ 192.168.178.31:9123
{
 'address': '192.168.178.31', 
 'port': 9123, 
 'name': '', 
 'server': '', 
 'productName': 'Elgato Ring Light', 
 'hardwareBoardType': 201, 
 'firmwareBuildNumber': 143, 
 'firmwareVersion': '1.0.4', 
 'serialNumber': 'DW50J1A10436', 
 'display': '', 
 'isOn': 1, 
 'isBrightness': 35, 
 'isTemperature': 3700.0
}
```
