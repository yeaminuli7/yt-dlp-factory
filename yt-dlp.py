import yt_dlp
import sys

def main():
    try:
        yt_dlp.main(sys.argv[1:])
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
