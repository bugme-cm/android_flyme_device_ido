import common
import edify_generator

def WritePolicyConfig(info):
  try:
    file_contexts = info.input_zip.read("META/file_contexts")
    common.ZipWriteStr(info.output_zip, "file_contexts", file_contexts)
  except KeyError:
    print "warning: file_context missing from target;"

def InstallSuperSU(info):
    supersu = info.input_zip.read("META/UPDATE-SuperSU.zip")
    common.ZipWriteStr(info.output_zip, "su/UPDATE-SuperSU.zip", supersu)

def FlashSUperSU(info):
    info.script.AppendExtra(('ui_print("flash Supersu...");'))
    info.script.AppendExtra(('package_extract_dir("su", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "unzip", "/tmp/supersu/UPDATE-SuperSU.zip", "META-INF/com/google/android/*", "-d", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "sh", "/tmp/supersu/META-INF/com/google/android/update-binary", "dummy", "1", "/tmp/supersu/UPDATE-SuperSU.zip");'))

def InstallDap(info):
    supersu = info.input_zip.read("META/dap.zip")
    common.ZipWriteStr(info.output_zip, "dap/dap.zip", supersu)

def FlashDap(info):
    info.script.AppendExtra(('ui_print("flash Dap...");'))
    info.script.AppendExtra(('package_extract_dir("dap", "/tmp/dap");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "unzip", "/tmp/dap/dap.zip", "META-INF/com/google/android/*", "-d", "/tmp/dap");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "sh", "/tmp/dap/META-INF/com/google/android/update-binary", "dummy", "1", "/tmp/dap/dap.zip");'))

def FullOTA_InstallEnd(info):
    WritePolicyConfig(info)
    InstallSuperSU(info)
    FlashSUperSU(info)
    InstallDap(info)
    FlashDap(info)