# The new config inherits a base config to highlight the necessary modification
_base_ = '/kaggle/working/mmdetection/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('seal',)
data = dict(
    train=dict(
        img_prefix='/kaggle/working/containner_data-2/train/',
        classes=classes,
        ann_file='/kaggle/working/containner_data-2/train/_annotations.coco.json'),
    val=dict(
        img_prefix='/kaggle/working/containner_data-2/valid/',
        classes=classes,
        ann_file='/kaggle/working/containner_data-2/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='/kaggle/working/containner_data-2/test/',
        classes=classes,
        ann_file='/kaggle/working/containner_data-2/test/_annotations.coco.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = '/kaggle/input/checkpoints/rcnn_mstrain-poly_3x.pth'