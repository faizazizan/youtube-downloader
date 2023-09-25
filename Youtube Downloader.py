#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytube

# Ask the user to enter the URL of the YouTube video
video_url = input('Enter the URL of the YouTube video: ')

try:
    # Create an instance of the YouTube video
    video_instance = pytube.YouTube(video_url)

    # Get the highest resolution stream
    stream = video_instance.streams.get_highest_resolution()

    # Download the video
    stream.download()
    print(f"Video downloaded successfully as '{video_instance.title}'")
except Exception as e:
    print(f"An error occurred: {e}")


# In[ ]:





# In[ ]:




