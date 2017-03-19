cd /D "%~dp0"
@powershell -ExecutionPolicy Bypass "powershell -NoProfile -ExecutionPolicy Bypass -Command \"iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))\";
$env:Path = [System.Environment]::GetEnvironmentVariable(\"Path\",\"Machine\") + \";\" + [System.Environment]::GetEnvironmentVariable(\"Path\",\"User\");
choco install python3 -y;
$env:Path = [System.Environment]::GetEnvironmentVariable(\"Path\",\"Machine\") + \";\" + [System.Environment]::GetEnvironmentVariable(\"Path\",\"User\");
pip3 install demjson requests bs4 PyQt5 lxml"
@powershell (New-Object -ComObject Wscript.Shell).Popup("""All dependencies installed, try to start PCS now with start.bat""",0,"""Done""",0x0)
