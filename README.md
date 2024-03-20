# basket-event-detection
![child vs bot in basketball](https://github.com/ianmparker/basket-detection/assets/18231849/4aa94c81-fa3c-4e42-96bb-93e25cafea5e)

--------------------------------------------------
**Overview:**

This repository contains a YOLO model trained on a dataset of basketball images. 

The model is aplied to a video to detect the position of a basketball and hoop.

With those positions the shot_detector.py file determines whether a shot attempt has been made. 

-------------------------------------------------


**How To Run this Project:**

 - Follow the instructions in 'main.py' to train the model and prepare for shot detection.
 - Run 'shot_detector.py' for shot detection analysis.
 - Please ensure you have the required Python packages installed, including OpenCV, numpy, and ultralytics' YOLO.

You can use this model on a video of yourself shooting around by replacing the path of "shootaround.mov" with the path of your own video. 

![image](https://github.com/ianmparker/basket-detection/assets/18231849/c8bdd6e5-11e9-437d-8c90-be8f244fe5c9)


----------------------------
**SCREENSHOTS**


![shot attempt](https://github.com/ianmparker/basket-detection/assets/18231849/7207e7af-b7b7-4fee-ba02-d2a023c8e0b5)

Shot Attempt Detected with Ball Trajectory Traced

![shot made](https://github.com/ianmparker/basket-detection/assets/18231849/18fcae1a-0c40-4cb9-b1ca-53171fcd9f60)

Shot Made Detected with Scoreboard Updated

------------------------------
**Next Steps:**

I plan to continue expanding on this project by training the model on a different dataset that contains additional classes.

An example of a dataset containing additional classes is https://universe.roboflow.com/mathieulec/basketball-5dtuv/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true![image](https://github.com/ianmparker/basket-detection/assets/18231849/4763d106-cc1b-4c69-a9ec-4ea1e7ea9c8f)

This dataset contains classes for 'Ball', 'Made', 'Person', and 'Rim' which I should be able to use to dected things like rebounds, fouls, etc...

------------------------------

My LinkedIn : https://www.linkedin.com/in/ian-parker-596011142/

References: 
 - https://github.com/nitinhemaraj/Basketball-shot-detection
 - https://www.youtube.com/watch?v=WgPbbWmnXJ8



-----------------------------------------

