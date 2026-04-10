import platform
import sys
import os

def main():
    # প্রসেসর এবং ওএস ডিটেকশন
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    # ইউজারকে জানানো (আপনার প্রজেক্টের ব্র্যান্ডিং হিসেবে কাজ করবে)
    print(f"[*] Detecting System: {system} ({machine})")
    
    # এখানে আপনার মূল yt-dlp লজিক
    import yt_dlp
    try:
        yt_dlp.main(sys.argv[1:])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
