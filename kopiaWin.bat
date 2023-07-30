@echo off
rem 12.2020 kopia wd elements
rem format .bat i uruchom jako administrator, na samsung dysk przenosny
ROBOCOPY "D:\wdkopia0719\2fszystko19\SZYSFROWANIE319" "E:\wdkopia0719\2fszystko19\SZYSFROWANIE319" /E /ZB /COPYALL /DCOPY:T /R:2 /W:1 /XA:SH /V /TEE /XJ /XJD /XJF /MT:6 /log:"C:\Logs\wdkopia030722.txt"