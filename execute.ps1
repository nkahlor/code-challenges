param(
    [int]$problemNumber
)

$baseDir = (Get-Location).Path
$solutionFile = Get-ChildItem -Path "./solutions" -File |
Where-Object { $_.Name -like "${problemNumber}*.py" } |
Select-Object -First 1

if (-not $solutionFile) {
    Write-Host "No solution file found for problem $problemNumber"
    exit 1
}

$relativePath = $solutionFile.FullName.Substring($baseDir.Length).TrimStart('\', '/')
$relativePath = $relativePath -replace '^\\solutions\\', '' -replace '\\', '.'
$moduleName = [System.IO.Path]::ChangeExtension($relativePath, $null) -replace '\\', '.'
$moduleName = $moduleName.TrimEnd('.')
$moduleName = $moduleName -replace '-', '_'

Write-Host "Running Python module: $moduleName"

pipenv run python -m $moduleName
