# Camera Kivy

This is a sample project demonstrating how to implement a camera using Kivy, a Python framework for developing mobile applications. The application is designed to run on mobile devices using Pydroid.

This project was developed as part of a school assignment.

## Requirements

- Python 3
- Kivy 2.0.0 or higher
- Pydroid 3 (Android app for running Python scripts on mobile devices)
- Pydroid 3 Permission Plugin

## Installation in Pydroid

### Step 1: Install Pydroid 3

Download and install the Pydroid 3 app from the Google Play Store: [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)

### Step 2: Install the Pydroid 3 Permission Plugin

Download and install the Pydroid 3 Permission Plugin from the Google Play Store: [Pydroid 3 Permission Plugin](https://play.google.com/store/apps/details?id=ru.iiec.pydroidpermissionsplugin)

### Step 3: Install Kivy in Pydroid 3

Open Pydroid 3 and open the terminal (you can find it in the side menu). In the terminal, run the following commands to install Kivy:

```sh
pip install kivy
```

### Step 4: Grant Camera Access

To ensure the application can access the camera, you need to grant camera permissions to the Pydroid 3 Permission Plugin:

1. Open the "Settings" app on your Android device.
2. Go to "Apps" or "Applications".
3. Find and select "Pydroid 3 Permission Plugin".
4. Tap on "Permissions".
5. Make sure the "Camera" permission is enabled.


## Usage

1. Download the code from the repository.
2. Open the `main.py` file in Pydroid 3.
3. Run the file.

The application will open the camera and display the live feed. Pressing the "capture" button will save an image on the device.