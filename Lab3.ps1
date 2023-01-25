function getIP{
(Get-NetIPAddress).ipv4address | Select-string "10."
}

$IP = getIP
$USER = $env:USERNAME
$HOSTNAME = HOSTNAME
$PS = $HOST.Version.Major
$DATE = Get-Date

Write-Host("This machine's IP address is: $IP
User is:  $USER
Hostname is:  $HOSTNAME
Powershell Version is:  $PS
Today's Date is $DATE")

$BODY = ("This machine's IP address is $IP.  The user is $USER.  Hostname is $HOSTNAME.
Powershell version is $PS.")

Send-MailMessage -to "leonardf@ucmail.uc.edu" -from "zachrlew@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)