# Setup

To correctly train locally, copy the `./config.example.yaml` to `./config.yaml`
and replace the `path` variable with the **absolute path** of the dataset.

Then run the `train.py`

The structure of the path must be the following: 

- path
    - images
        - train
            - 1.png
            - ...
        - val 
            - 1.png
            - ...
    - labels
        - train
            - 1.txt
            - ...
        - val 
            - 1.txt
            - ...

Additionally, this must be following the YOLO format

# Training results

It takes approx 15 min to run 100 epochs

Training results for batch 25 where much better
Training results for batch 27 much better and trained over 25
