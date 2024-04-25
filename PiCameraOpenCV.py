
from picamera2 import Picamera2  # required for camera module v3
import cv2 as cv

class PiCameraOpenCV():

    def __init__(self,camera_settings):

        self.controls = None
        self.is_open = True
        self.active_config =  camera_settings['Camera_Active_Config']
        try:
            self.cap = Picamera2()
            
            main = self._configure_res_mode(camera_settings,'main')
            
            lores = self._configure_res_mode(camera_settings,'lores')
            
            raw = self._configure_res_mode(camera_settings,'raw')

            self.config = self.cap.create_video_configuration(raw=raw,main=main,lores=lores)

            #request optimal image size
            self.cap.align_configuration(self.config)
            self.cap.configure(self.config)

            if 'Camera_Controls' in camera_settings:
                self.controls = camera_settings["Camera_Controls"]
                for control in self.controls:
                    self.cap.set_controls(control)
            
            self.cap.start()

        except:
            self.is_open = False
        return
    def grab_meta_data(self):

        return self.cap.capture_metadata();
    #private method
    def _configure_res_mode(self,camera_settings,mode):
        mode_setting = {}

        if mode in camera_settings:
            if "Horz_Res" in camera_settings[mode]:
                if camera_settings[mode]["Horz_Res"] != 0:
                    mode_setting['size'] = (camera_settings[mode]["Horz_Res"],camera_settings[mode]["Vert_Res"])

            if "fmt" in camera_settings[mode]:
                mode_setting['format'] = camera_settings[mode]["fmt"]
        return mode_setting
    def get_mode(self):

        return self.active_config

    # 'main' or 'lores'
    def set_mode(self,main_or_lores):
        self.active_config = main_or_lores
        return
    def read(self):

        if self.is_open:
            dst = self.cap.capture_array(self.active_config)

            if(self.active_config.find('lores')!=-1):
                dst=cv.cvtColor(dst, cv.COLOR_YUV2BGR_I420)
            
        return self.is_open,dst
    def isOpened(self):

        return self.is_open
    
    def release(self):
        if self.is_open:
            self.cap.close()
        self.is_open = False
        return
    

    # purely for compatibility at the moment
    def set(self,var,val):

        if var == cv.CAP_PROP_FRAME_WIDTH:
            # do nothing
            pass
        elif var==cv.CAP_PROP_FRAME_HEIGHT:
            pass
        elif var == cv.CAP_PROP_FPS:
            pass

        return 
    
