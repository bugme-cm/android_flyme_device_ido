#!/system/bin/sh
if [ -f /system/etc/recovery-transform.sh ]; then
  exec sh /system/etc/recovery-transform.sh 21817344 732aa5afd4c84cb2ffe1514379cb4697cb784225 18823168 374f891d6d580fa3eb91b527d730ce9e148743f2
fi

if ! applypatch -c EMMC:/dev/block/bootdevice/by-name/recovery:21817344:732aa5afd4c84cb2ffe1514379cb4697cb784225; then
  applypatch -b /system/etc/recovery-resource.dat EMMC:/dev/block/bootdevice/by-name/boot:18823168:374f891d6d580fa3eb91b527d730ce9e148743f2 EMMC:/dev/block/bootdevice/by-name/recovery 732aa5afd4c84cb2ffe1514379cb4697cb784225 21817344 374f891d6d580fa3eb91b527d730ce9e148743f2:/system/recovery-from-boot.p && log -t recovery "Installing new recovery image: succeeded" || log -t recovery "Installing new recovery image: failed"
else
  log -t recovery "Recovery image already installed"
fi
