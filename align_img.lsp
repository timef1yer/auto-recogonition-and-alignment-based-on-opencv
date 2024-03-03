; 设置图像文件路径
;(setq image_path "C:/Users/wuyx0/Desktop/coda/autoalign/pics2/1.jpg")

; 获取附加的图像对象


; 设置对齐点坐标
(setq source_point (getpoint "\nEnter source alignment point: "))
(setq target_point (getpoint "\nEnter target alignment point: "))

; 关闭 "APPLOAD" 弹框
(setvar "APPLOAD-CONTROL" 1)

(setq image_obj (entlast))

; 获取图像对象的句柄
(setq image_handle (cdr (assoc 5 (entget image_obj))))
; 调用对齐命令，将图像对齐到指定的点

; 关闭 "APPLOAD" 弹框
(setvar "APPLOAD-CONTROL" 0)

(command "-ALIGN" image_handle "" source_point target_point "")

; 保存脚本
;(command "-SAVEAS" "C:/Users/wuyx0/Desktop/coda/autoalign/align_script.scr")