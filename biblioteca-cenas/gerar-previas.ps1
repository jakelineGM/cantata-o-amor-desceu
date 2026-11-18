# Gera _previa.jpg em cada pasta da biblioteca: um quadro de cada vídeo, numerado (ver _indice.txt).
$Base = Split-Path -Parent $MyInvocation.MyCommand.Path
$ff = "$env:USERPROFILE\.editor-video\bin\ffmpeg.exe"; if (-not (Test-Path $ff)) { $ff = "ffmpeg" }
$fp = "$env:USERPROFILE\.editor-video\bin\ffprobe.exe"; if (-not (Test-Path $fp)) { $fp = "ffprobe" }
Get-ChildItem $Base -Directory | ForEach-Object {
  $dir = $_.FullName; $tmp = Join-Path $env:TEMP ("prev_" + $_.Name); Remove-Item $tmp -Recurse -ErrorAction SilentlyContinue; New-Item -ItemType Directory $tmp | Out-Null
  $files = Get-ChildItem $dir -Filter *.mp4 | Sort-Object Name; $k = 0; $idx = @()
  foreach ($f in $files) {
    $k++; $d = [double](& $fp -v error -show_entries format=duration -of csv=p=0 $f.FullName); $t = [math]::Round($d/3,2)
    & $ff -v error -y -ss $t -i $f.FullName -frames:v 1 -vf "scale=320:180,drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='$k':x=6:y=6:fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.6" (Join-Path $tmp ("{0:D4}.jpg" -f $k))
    $idx += "{0,4}  {1}  ({2:N0} s)" -f $k, $f.Name, $d
  }
  $idx | Set-Content (Join-Path $dir "_indice.txt") -Encoding UTF8
  if ($k -gt 0) { & $ff -v error -y -framerate 1 -i (Join-Path $tmp "%04d.jpg") -vf "tile=6x$([math]::Ceiling($k/6))" -frames:v 1 (Join-Path $dir "_previa.jpg") }
  Remove-Item $tmp -Recurse -ErrorAction SilentlyContinue
}
