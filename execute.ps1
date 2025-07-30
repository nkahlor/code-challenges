param(
    [string]$ScriptName
)
$solutionsPath = Join-Path $PSScriptRoot "solutions"

if (-not (Test-Path $solutionsPath)) {
    Write-Host "Solutions folder not found: $solutionsPath" -ForegroundColor Red
    exit 1
}

# Get all .py files in the solutions folder
$pyFiles = Get-ChildItem -Path $solutionsPath -Filter *.py

if ($pyFiles.Count -eq 0) {
    Write-Host "No Python scripts found in $solutionsPath" -ForegroundColor Red
    exit 1
}

if ($ScriptName) {
    $targetScript = $pyFiles | Where-Object { $_.Name -eq $ScriptName }
    if (-not $targetScript) {
        Write-Host "Specified script not found: $ScriptName" -ForegroundColor Red
        exit 1
    }
}
else {
    # Extract numbers from filenames and select the highest
    $targetScript = $pyFiles | Sort-Object {
        if ($_ -match '\d+') { [int]($matches[0]) } else { 0 }
    } -Descending | Select-Object -First 1
}

Write-Host "Running script: " -NoNewline -ForegroundColor Cyan
Write-Host "$($targetScript.Name)" -ForegroundColor Yellow
Write-Host ("=" * 50) -ForegroundColor DarkGray

$baseName = $targetScript.BaseName
$executionTime = Measure-Command {
    pipenv run python -m "solutions.$baseName" | Out-Host
}

Write-Host ("=" * 50) -ForegroundColor DarkGray
if ($executionTime.TotalSeconds -ge 1) {
    Write-Host "Execution time: $([math]::Round($executionTime.TotalSeconds, 3)) seconds" -ForegroundColor Green
}
elseif ($executionTime.TotalMilliseconds -ge 1) {
    Write-Host "Execution time: $([math]::Round($executionTime.TotalMilliseconds, 2)) ms" -ForegroundColor Green
}
else {
    Write-Host "Execution time: $([math]::Round($executionTime.TotalMilliseconds * 1000, 0)) μs" -ForegroundColor Green
}