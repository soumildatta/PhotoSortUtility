# PhotoSortUtility
This is a very simple script to make my life easier when transferring images from my camera to my computer while having an organized folder structure. It automates sorting RAW and JPEG files into a raw and jpeg folder. It does not delete the original files in case something goes wrong, but simply copies the files into their respective jpeg or raw folders. The original files can safely be deleted after inspeting whether the process was completed successfully. Currently, this script is not too generalizable. The folder hierarchy needs to be similar to the example below. 

Made this available in case this helps you save time like it helps me!

## Example folder hierarchy
The script works when it is in the same folder that contains the other photos folder. These photo folders will contain jpeg and raw files that will then be sorted.
```
photos
├── sortPics.py (this script)
├── PhotoFolder1
|   ├── *.jpeg
|   └── *.raw
├── PhotoFolder2
|   ├── *.jpeg
|   └── *.raw
...
```

## Requirements
* Have the folder hierarchy as shown above
* Have python3 installed on your computer

## Run Script 
To run this script, make sure the script is in your photos folder, and outside the subfolders as shown in the example folder hierarchy above. Open a terminal and `cd` into the photos directory and run the script with `python sortPics.py`. Your files will now be sorted and the originals can be deleted after inspection.

## Contributing 
To contribute to this project, follow these steps:
1. Fork the repo
2. Clone the project to your local machine
3. Commit changes to your own branch
4. Push your work to your fork
5. Submit a Pull request so your changes can be reviewed


