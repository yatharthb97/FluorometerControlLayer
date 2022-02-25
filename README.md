# Fluorometer Control Layer

Control Layer Software for in-house fluorometer of KG biophysics lab at TIFR-Hyderabad.

Author: Yatharth Bhasin (yatharth1997+git@gmail.com)

License: Undefined (not released for free usage)

Execute Software using:

```bash
python ./run.py #On windows
./run.py        # On linux
```



## Configuration

The Configuration for the operation is loaded using a `json` file in the same directory as `run.py`. Any valid `json` file (with a `.json`) extension can be used. 

***Note:***

1. The file must have `"config"` in its name. In case of multiple files containing the keyword `"config"`, the file is selected in alphabetical order.
2. Missing fields are automatically added and a warning message is generated.
3. When no configuration file is found, the system generates one with the name: `autogenerated_config.json`.
4. Unknown fields will generate a warning message.

### Configuration file at a glance
todo


## Meta Data Collection



## Plotting Interface / GUI



## TODO

1. Add sleep lock that prevents OS from putting PC to sleep.
2. Add desktop shortcut mechanism.