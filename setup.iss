#define AppName "PCS"
#define AppVersion "v1.8"
#define AppPublisher "smclt30p"
#define AppURL "https://github.com/smclt30p/PCS"
#define PyExe "python-3.6.1.exe"

[Setup]
AppId={{3E28F9A8-9940-4066-A149-96663AB24797}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
AppPublisherURL={#AppURL}
AppSupportURL={#AppURL}
AppUpdatesURL={#AppURL}
DefaultDirName={userappdata}\{#AppName}
DefaultGroupName={#AppName}
AllowNoIcons=yes
LicenseFile=LICENSE.txt
OutputDir=build\
OutputBaseFilename=pcs-setup-{#AppVersion}
SetupIconFile=ui\res\icon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Components]
Name: "main"; Description: "PCS Script files"; Types: full compact custom; Flags: fixed
Name: "python"; Description: "Python 3.6.1/pip 9.0.1 (system wide)"; Types: full custom;

[Files]
;Source: "depresolv.py"; DestDir: "{app}"; Flags: replacesameversion 
;#Source: "start.bat"; DestDir: "{app}"; Flags: replacesameversion
Source: "core\*.*";Excludes:"*__pycache__*"; DestDir: "{app}\core"; Flags: replacesameversion recursesubdirs; Components: main
Source: "ui\*.*"; Excludes:"*__pycache__*, src/*"; DestDir: "{app}\ui"; Flags: replacesameversion recursesubdirs; Components: main
Source: "updater\*.*"; Excludes:"*__pycache__*";DestDir: "{app}\updater"; Flags: replacesameversion recursesubdirs; Components: main
Source: "plugins\*.*";Excludes:"*__pycache__*"; DestDir: "{app}\plugins"; Flags: replacesameversion recursesubdirs; Components: main
Source: "depresolv.py"; DestDir: "{app}"; Flags: replacesameversion; Components: main
Source: "start.bat"; DestDir: "{app}"; Flags: replacesameversion; Components: main
Source: "py\{#PyExe}"; DestDir: "{app}\py\"; Flags: replacesameversion; AfterInstall: InstallPython; Components: python

[Code]
procedure InstallPython;
var
  ResultCode: Integer;
begin
  if not Exec(ExpandConstant('{app}\py\{#PyExe}'), '/quiet InstallAllUsers=1 PrependPath=1', '', SW_SHOWNORMAL,
    ewWaitUntilTerminated, ResultCode)
  then
    MsgBox('Python failed to install! Please install manually from Python.org, selecting "Add to PATH"!', mbError, MB_OK);
end;


[Icons]
Name: "{group}\{cm:UninstallProgram,{#AppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\PCS"; Filename: "{app}\start.bat"; IconFilename: "{app}\ui\res\icon.ico"

