function Green {
    process { Write-Host $_ -ForegroundColor Green }
}

function Yellow {
    process { Write-Host $_ -ForegroundColor Yellow }
}

function Blue {
    process { Write-Host $_ -ForegroundColor Blue }
}

$WelcomeText = @"

<-- Welcome to the Blitz Machine Tagging Server -->

This was built by team Blitz (NSUT) for submission in the Myntra Hackerramp 2021.
Hope you like it!
"@

$RepoText = @"

-> Here is the repo: https://github.com/Illusion47586/blitz-tf

"@

$ExitText = @"

<-- Exiting the Blitz Machine -->
Hope you liked our project!

"@

# Welcome
Write-Output $WelcomeText | Green
Write-Output $RepoText | Blue

# Setup
Write-Output @"
<-- Installing Dependencies -->

"@ | Yellow
.\Scripts\pip.exe install --upgrade pip
.\Scripts\pip.exe install -r .\requirements.txt

# Running
Write-Output @"

<-- Running the project -->
"@ | Yellow
Write-Output "-> You can stop the project any time by pressing CTRL+C." | Blue
.\Scripts\python.exe .\run_debug.py

# Exit
Write-Output $ExitText | Green