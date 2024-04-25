# Picamera2-as-Opencv-Class
Class for interfacing Picamera2 into Opencv

example usage


    from PiCameraOpencCV import PiCameraOpencCV
    import cv2 as cv
    # settings are defined in a dictionary
    camera_settings = { 
            # for 'main' mode (required)
            "Camera_Active_Config" : 'main',
            "main":{
                "Horz_Res":1280,  
                "Vert_Res":720,
                "fmt":"RGB888",
                },
             # for 'lores' mode (optional)
             "lores":{
                "Horz_Res":640,  
                "Vert_Res":360,
                "fmt":"YUV420",
            },
            # for raw (optional) -> used to force a particular sensor mode
            "raw":{
                "Horz_Res":2304,  
                "Vert_Res":1296 
            },
            "Camera_Controls":[
        
                {"AfMode":0,"LensPosition":10},
                {"FrameRate":30}
            ],
    }

    # interface replicates opencv functionality 
    cap = PiCameraOpencCV(camera_settings)

    while cap.isOpened():
        success,frame = cap.read()

        if success:
            cv.imshow('hello!',frame)
        
    cap.release()
