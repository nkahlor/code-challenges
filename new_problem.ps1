$solutionsDir = "solutions"

if (-not (Test-Path $solutionsDir)) {
    Write-Output "Directory 'solutions' does not exist. Creating it."
    New-Item -ItemType Directory -Path $solutionsDir | Out-Null
}

$files = Get-ChildItem -Path $solutionsDir -Filter "*.py" | ForEach-Object {
    if ($_ -match "(\d{3})\.py") {
        [int]$matches[1]
    }
} | Sort-Object -Descending

if ($files.Count -eq 0) {
    $nextNumber = 1
}
else {
    $nextNumber = $files[0] + 1
}

$fileName = "{0:D3}.py" -f $nextNumber
$filePath = Join-Path $solutionsDir $fileName


$content = @"
def solve() -> int:
    return 0


if __name__ == "__main__":
    print(solve())
"@

# Write file
Set-Content -Path $filePath -Value $content -Encoding UTF8
Write-Output "Created $fileName in $solutionsDir"
