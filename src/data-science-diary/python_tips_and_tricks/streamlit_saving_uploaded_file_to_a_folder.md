# Streamlit: _Saving uploaded file(s) to a folder_

The following code snippet was adapted from the 
[video: _How To Save File Uploads to A Directory in Streamlit Python_](https://youtu.be/UyWEo-q4BGY?t=742) 
by @JCharisTech.

## Screenshot

![image](https://user-images.githubusercontent.com/10201242/130351917-42499d55-d19d-43b9-a2d5-e3d8827a3fa6.png)

## Adapted Version

The function `save_uploaded_file()` takes in the `uploadedfile` as an input (along with optional input, `folder="tempDir"`) 
and returns a status (`success` or `error`) based on whether the file was saved or not, under the desired folder.

Here, `uploadedfile` is defined as (an example):

```python
uploadedfile = st.file_uploader("Upload an image", type=["png", "jpeg", "jpg"])
```

### Code

```python
import os
import streamlit as st
from typing import Union, Optional, List
from streamlit.uploaded_file_manager import UploadedFile

SomeUploadedFiles = Optional[Union[UploadedFile, List[UploadedFile]]]

def save_uploaded_files(uploaded_content: SomeUploadedFiles, folder: str="tempDir"):
    if uploaded_content is not None:
        if isinstance(uploaded_content, list) and uploaded_content:
            for uf in uploaded_content:
                save_uploaded_file(uploadedfile=uf, folder=folder)
        elif isinstance(uploaded_content, UploadedFile):
            save_uploaded_file(uploadedfile=uploaded_content, folder=folder)

def save_uploaded_file(uploadedfile: UploadedFile, folder: str="tempDir"):
    """Saves an uploaded file to a local directory on the server side."""
    filename = uploadedfile.name
    save_path = os.path.join(folder, filename)
    if (not os.path.exists(folder)) and (not os.path.isdir(folder)):
        os.makedirs(folder)
    with open(save_path, "wb") as f:
        f.write(uploadedfile.getbuffer())
    if os.path.isfile(save_path):
        return st.success("Saved file: {filename} in folder {folder}".format(
            filename=filename, folder=folder))
    else:
        return st.error("File was not saved.")
```

## References

- https://docs.streamlit.io/en/stable/api.html#display-progress-and-status
- https://discuss.streamlit.io/t/how-to-download-local-folder/3717
- https://youtu.be/UyWEo-q4BGY?t=742
- https://github.com/streamlit/streamlit/blob/develop/lib/streamlit/elements/file_uploader.py
