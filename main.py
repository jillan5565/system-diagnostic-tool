import shutil
import psutil

print("🔍 Starting System Diagnostic...\n")

# 1. فحص المعالج
def check_cpu():
    return psutil.cpu_percent(interval=1)

# 2. فحص الرام
def check_ram():
    ram = psutil.virtual_memory()
    return ram.percent

# 3. فحص القرص
def check_disk():
    total, used, free = shutil.disk_usage("/")
    return (used / total) * 100

# 4. فحص سرعة الإنترنت مع معالجة التعليق
def check_internet_speed():
    print("⏳ Checking internet speed (this may take a few seconds)...")
    try:
        import speedtest
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        return download, upload
    except Exception as e:
        print(f"⚠️ Skipped speedtest: {e}")
        return None, None

# تنفيذ الفحوصات
cpu = check_cpu()
ram = check_ram()
disk = check_disk()
download, upload = check_internet_speed()

# طباعة التقرير النهائي
print("\n" + "="*30)
print("🔧 System Diagnostic Report")
print("="*30)
print(f"CPU Usage:      {cpu}%")
print(f"RAM Usage:      {ram}%")
print(f"Disk Usage:     {disk:.2f}%")

if download is not None and upload is not None:
    print(f"Download Speed: {download:.2f} Mbps")
    print(f"Upload Speed:   {upload:.2f} Mbps")
else:
    print("Internet Speed: N/A (Failed or Skipped)")

print("="*30)
print("✅ Diagnostics Completed Successfully!\n")