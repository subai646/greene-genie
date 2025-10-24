"""
Build script to create standalone executable for Greene Genie
This script uses PyInstaller to create a Windows .exe file
"""
import os
import subprocess
import sys

def build_executable():
    """Build the Greene Genie executable"""
    
    print("=" * 60)
    print("Greene Genie - Build Executable")
    print("=" * 60)
    print()
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
    except ImportError:
        print("✗ PyInstaller is not installed")
        print("\nInstalling PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")
    
    print()
    print("Building executable...")
    print("This may take a few minutes...")
    print()
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=GreeneGenie",
        "--add-data=GK Logo.png;.",
        "--clean",
        "wave_greeter.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print()
        print("=" * 60)
        print("✓ Build completed successfully!")
        print("=" * 60)
        print()
        print("Your executable is located at:")
        print("  dist\\GreeneGenie.exe")
        print()
        print("You can now share this .exe file with your clients!")
        print("They just need to run it - no Python installation required.")
        print()
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed with error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    build_executable()

