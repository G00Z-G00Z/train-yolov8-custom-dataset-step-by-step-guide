# train-yolov8-custom-dataset-step-by-step-guide

<p align="center">
<a href="https://www.youtube.com/watch?v=m9fH9OWn8YM">
    <img width="600" src="https://utils-computervisiondeveloper.s3.amazonaws.com/thumbnails/with_play_button/yolov8_object_detection.jpg" alt="Watch the video">
    </br>Watch on YouTube: Train Yolo V8 object detector on your custom data | Step by step guide !
</a>
</p>

## Setup 

Install the dependecies

```sh
pip install -r ./requirements.txt
```

## dataset

If you want to train yolov8 with the same dataset I use in the video, this is what you should do:

1. Download the [downloader.py](https://raw.githubusercontent.com/openimages/dataset/master/downloader.py) file.
2. Download the object detection dataset; [train](https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv), [validation](https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv) and [test](https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv).
2. Go to **prepare_data** directory.
4. Execute **create_image_list_file.py**.
5. Execute **downloader.py**.

```sh
python downloader.py $IMAGE_LIST_FILE --download_folder=$DOWNLOAD_FOLDER
```

6. Execute **create_dataset_yolo_format.py**, changing **DATA_ALL_DIR** by **$DOWNLOAD_FOLDER**.

# Problem log

## Model is not being trained with a loss of 'nan'

The issue is [discussed here](https://github.com/ultralytics/ultralytics/issues/280). The problem is with the compatibility of the GPU. You may have a problem or may not. 

To solve it set the `amp=False` option in the training of the model:

```python
results = model.train(
    data="config.yaml",
    epochs=1,
    amp=False,
)  # train the model
```

However, you could try it without it to see if you have compatible CPU!

