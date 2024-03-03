(defun c:import-image ()
  (setq image_def "C:/Users/wuyx0/Desktop/coda/autoalign/pics2/1.jpg") ; Set the image file path

  (setq insertion_point '(0 0 0)) ; Prompt for the insertion point
  (setq angle0 0)
  (setq scale_factor 2560) ; 设置缩放比例

  (setvar "FILEDIA" 0) ; 禁用文件对话框

  ;(command-silent "_.-IMAGE" "ATTACH" image_def insertion_point scale_factor angle0)
  
  (command "_.ATTACH" image_def insertion_point scale_factor angle0) ; 插入图片
  
  (setvar "FILEDIA" 1) ; 禁用文件对话框
  
  
)
