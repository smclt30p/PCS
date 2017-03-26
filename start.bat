set PYTHONPATH=%CD%
if EXIST installed (
    start pythonw ui\Main.py
    exit
) else (
    start python ui\Main.py
)