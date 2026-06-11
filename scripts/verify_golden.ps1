# Golden Master 검증 — GREEN baseline vs REFACTOR 후 회귀 검출
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..

Write-Host "=== Golden Master Verification ===" -ForegroundColor Cyan
Write-Host "Expected: 24 (Dual-Track) + 6 (CLI golden) = 30 passed"
Write-Host ""

python -m pytest tests/ -v --tb=short
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "FAIL: Golden master broken. Stop REFACTOR." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "OK: Golden master intact." -ForegroundColor Green
