import time

def track_download_progress():
    progress_steps = [20, 40, 60, 80, 100]
    
    for progress in progress_steps:
        if progress < 100:
            print(f"Downloading... {progress}%")
            time.sleep(1)
        else:
            print("Download Complete")

print("Starting download...")
track_download_progress()

print("\n" + "="*30)

def track_download_fast():
    progress_steps = [20, 40, 60, 80, 100]
    
    for progress in progress_steps:
        if progress < 100:
            print(f"Downloading... {progress}%")
            time.sleep(0.5)
        else:
            print("Download Complete")

print("Fast download simulation:")
track_download_fast()

def track_custom_download(steps):
    for step in steps:
        if step < 100:
            print(f"Downloading... {step}%")
            time.sleep(0.3)
        else:
            print("Download Complete")

print("\nCustom progress:")
custom_steps = [10, 30, 50, 75, 90, 100]
track_custom_download(custom_steps)