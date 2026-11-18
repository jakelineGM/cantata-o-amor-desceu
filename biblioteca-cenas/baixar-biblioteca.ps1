# Baixa a biblioteca de cenas listada em catalogo-cenas.csv (mesma pasta deste script).
# Uso: clique com o botão direito > Executar com PowerShell. Pode rodar de novo: pula o que já baixou.
$Base = Split-Path -Parent $MyInvocation.MyCommand.Path
$log = Join-Path $Base "_download-log.txt"
$itens = Import-Csv -Path (Join-Path $Base "catalogo-cenas.csv") -Delimiter ';' -Encoding UTF8
$n = 0
foreach ($i in $itens) {
  $n++
  $dir = Join-Path $Base $i.pasta; $out = Join-Path $dir $i.arquivo
  New-Item -ItemType Directory -Force $dir | Out-Null
  if ((Test-Path $out) -and ((Get-Item $out).Length -gt 100000)) { continue }
  Write-Host "[$n/$($itens.Count)] $($i.pasta)\$($i.arquivo)"
  & curl.exe -s -L --retry 3 -m 1800 -A "Mozilla/5.0" -o $out $i.url
  $len = if (Test-Path $out) { (Get-Item $out).Length } else { 0 }
  if ($len -lt 100000) { Remove-Item $out -ErrorAction SilentlyContinue; Add-Content $log "FALHOU $($i.arquivo)" }
  else { Add-Content $log "ok $($i.pasta)\$($i.arquivo) $len" }
}
Add-Content $log "FIM $(Get-Date)"
