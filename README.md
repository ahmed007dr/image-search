# image-search
image search from google refernce exel shet
Steps:

Step 1: Install the library by using: pip install bing-image-downloader

Step 2:

from bing_image_downloader import downloader
downloader.download(query_string, limit=100,  output_dir='dataset', 
adult_filter_off=True, force_replace=False, timeout=60)
That's it! All you would need to do is to add your image topic to the query_string.

Note:

Parameters that you can further tweak:

query_string : String to be searched.

limit : (optional, default is 100) Number of images to download.

output_dir : (optional, default is 'dataset') Name of output dir.

adult_filter_off : (optional, default is True) Enable of disable adult filteration.

force_replace : (optional, default is False) Delete folder if present and start a fresh download.

timeout : (optional, default is 60) timeout for connection in seconds.

Further Reference: https://pypi.org/project/bing-image-downloader/

