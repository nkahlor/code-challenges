param(
    [int]$n = 5,
    [string]$script = $null
)

$executeCommand = if ($script) { ".\execute.ps1 $script" } else { ".\execute.ps1" }
Write-Host "Running " -NoNewline -ForegroundColor Cyan
Write-Host "$executeCommand" -NoNewline -ForegroundColor Yellow
Write-Host " $n times..." -ForegroundColor Cyan
Write-Host ("=" * 50) -ForegroundColor DarkGray

$executionTimes = @()

for ($i = 1; $i -le $n; $i++) {
    Write-Host "Run $i/$n" -ForegroundColor Cyan
    
    $executionTime = Measure-Command {
        # Run execute.ps1 with optional script argument
        if ($script) {
            & ".\execute.ps1" $script | Out-Host
        }
        else {
            & ".\execute.ps1" | Out-Host
        }
    }
    
    $executionTimes += $executionTime.TotalMilliseconds
    
    # Format execution time like execute.ps1
    if ($executionTime.TotalSeconds -ge 1) {
        Write-Host "Run time: $([math]::Round($executionTime.TotalSeconds, 3)) seconds" -ForegroundColor Green
    }
    elseif ($executionTime.TotalMilliseconds -ge 1) {
        Write-Host "Run time: $([math]::Round($executionTime.TotalMilliseconds, 2)) ms" -ForegroundColor Green
    }
    else {
        Write-Host "Run time: $([math]::Round($executionTime.TotalMilliseconds * 1000, 0)) μs" -ForegroundColor Green
    }
    
    if ($i -lt $n) {
        Write-Host ("-" * 30) -ForegroundColor DarkGray
    }
}

Write-Host ("=" * 50) -ForegroundColor DarkGray

# Calculate statistics
$meanTime = ($executionTimes | Measure-Object -Average).Average
$minTime = ($executionTimes | Measure-Object -Minimum).Minimum
$maxTime = ($executionTimes | Measure-Object -Maximum).Maximum

Write-Host "Benchmark Results:" -ForegroundColor Cyan
Write-Host "Number of runs: " -NoNewline -ForegroundColor Cyan
Write-Host "$n" -ForegroundColor Yellow

# Format mean time
Write-Host "Mean execution time: " -NoNewline -ForegroundColor Cyan
if ($meanTime -ge 1000) {
    Write-Host "$([math]::Round($meanTime / 1000, 3)) seconds" -ForegroundColor Green
}
elseif ($meanTime -ge 1) {
    Write-Host "$([math]::Round($meanTime, 2)) ms" -ForegroundColor Green
}
else {
    Write-Host "$([math]::Round($meanTime * 1000, 0)) μs" -ForegroundColor Green
}

# Format min time
Write-Host "Min execution time: " -NoNewline -ForegroundColor Cyan
if ($minTime -ge 1000) {
    Write-Host "$([math]::Round($minTime / 1000, 3)) seconds" -ForegroundColor Green
}
elseif ($minTime -ge 1) {
    Write-Host "$([math]::Round($minTime, 2)) ms" -ForegroundColor Green
}
else {
    Write-Host "$([math]::Round($minTime * 1000, 0)) μs" -ForegroundColor Green
}

# Format max time
Write-Host "Max execution time: " -NoNewline -ForegroundColor Cyan
if ($maxTime -ge 1000) {
    Write-Host "$([math]::Round($maxTime / 1000, 3)) seconds" -ForegroundColor Green
}
elseif ($maxTime -ge 1) {
    Write-Host "$([math]::Round($maxTime, 2)) ms" -ForegroundColor Green
}
else {
    Write-Host "$([math]::Round($maxTime * 1000, 0)) μs" -ForegroundColor Green
}