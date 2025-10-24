"""
Quick test script to verify the Wave Greeter works
"""
import sys
import subprocess

def test_imports():
    """Test if required modules are available"""
    print("Testing required modules...")
    
    try:
        import tkinter as tk
        print("✓ tkinter is available")
        return True
    except ImportError:
        print("✗ tkinter is NOT available")
        print("  Install with: conda install tk")
        return False

def test_display():
    """Test if tkinter can create a window"""
    print("\nTesting display capabilities...")
    
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Don't show the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
        print(f"✓ Display detected: {screen_width}x{screen_height}")
        return True
    except Exception as e:
        print(f"✗ Display test failed: {e}")
        return False

def main():
    print("=" * 60)
    print("Wave Greeter - System Test")
    print("=" * 60)
    print()
    
    # Test imports
    imports_ok = test_imports()
    
    # Test display
    display_ok = test_display()
    
    print("\n" + "=" * 60)
    if imports_ok and display_ok:
        print("✓ All tests passed!")
        print("\nYou can now run the greeter with:")
        print("  python wave_greeter.py")
        print("\nOr use the batch file:")
        print("  run_greeter.bat")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
    print("=" * 60)

if __name__ == "__main__":
    main()