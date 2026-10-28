Set-Location (Split-Path -Parent $PSScriptRoot)
python -m unittest discover -s tests -v

