# # Setup detectron2 logger
# import detectron2
# from detectron2.utils.logger import setup_logger

# setup_logger()

# # import some common libraries
# import os
# import numpy as np
# import cv2
# import uuid

# # import some common detectron2 utilities
# from detectron2 import model_zoo
# from detectron2.engine import DefaultPredictor
# from detectron2.config import get_cfg
# from detectron2.data import MetadataCatalog
# from detectron2.utils.visualizer import Visualizer

# cfg = get_cfg()

# cfg.merge_from_file(
#     model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml")
# )
# cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
# cfg.MODEL.ROI_HEADS.NUM_CLASSES = 13
# cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.6  # set threshold for this model
# cfg.MODEL.RETINANET.NMS_THRESH_TEST = 0.5
# cfg.DATASETS.TEST = ("deepfashion",)
# cfg.MODEL.DEVICE = "cpu"

# MetadataCatalog.get("deepfashion").thing_classes = [
#     "short_sleeved_shirt",
#     "long_sleeved_shirt",
#     "short_sleeved_outwear",
#     "long_sleeved_outwear",
#     "vest",
#     "sling",
#     "shorts",
#     "trousers",
#     "skirt",
#     "short_sleeved_dress",
#     "long_sleeved_dress",
#     "vest_dress",
#     "sling_dress",
# ]

# predictor = DefaultPredictor(cfg)

# bts = ["Jungkook", "Suga", "J-Hope", "RM", "Jimin", "V", "Jin"]
# bts_score = {
#     0: [1, 7, 5, 7, 1, 1],  # "Jungkook"
#     1: [2, 6, 4, 2, 6, 5],  # "Suga"
#     2: [5, 3, 7, 4, 3, 7],  # "J-Hope"
#     3: [7, 1, 1, 5, 4, 4],  # "RM"
#     4: [3, 5, 3, 6, 2, 3],  # "Jimin"
#     5: [6, 2, 2, 1, 7, 6],  # "V"
#     6: [4, 4, 6, 3, 5, 2],  # "Jin"
# }


# def convert_class(pred_class):
#     if pred_class == 2 or pred_class == 3:
#         item = 0  # "outwear"
#     elif pred_class == 1 or pred_class == 10:
#         item = 1  # "long_sleeved_top"
#     elif pred_class == 0 or pred_class == 9:
#         item = 2  # "short_sleeved_top"
#     elif pred_class == 4 or pred_class == 5 or pred_class == 11 or pred_class == 12:
#         item = 3  # "sleeveless_top"
#     elif pred_class == 7:
#         item = 4  # "long_pants"
#     elif pred_class == 6 or pred_class == 8:
#         item = 5  # "short_pants"
#     return item


# def inference(img_path):
#     im = cv2.imread(img_path)
#     outputs = predictor(im)

#     labels = []
#     # imgs = []

#     # convert & save labels
#     pred_classes_tensor = outputs["instances"].to("cpu").pred_classes
#     for i in pred_classes_tensor:
#         labels.append(convert_class(int(i)))

#     # save crop images
#     # boxes = {}
#     # for coordinates in outputs["instances"].to("cpu").pred_boxes:
#     #     coordinates_array = []
#     #     for k in coordinates:
#     #         coordinates_array.append(int(k))
#     #     boxes[uuid.uuid4().hex[:].upper()] = coordinates_array

#     # for k, v in boxes.items():
#     #     crop_img = im[v[1] : v[3], v[0] : v[2], :]
#     #     imgs.append(crop_img)

#     return cal_mem_score(labels)


# def cal_mem_score(labels):
#     score = [0] * 7
#     for label in labels:
#         for mem in bts_score:
#             score[mem] += bts_score[mem][label]

#     return bts[score.index(max(score))]


# if __name__ == "__main__":
#     img_path = "./v_5.jpeg"
#     print(inference(img_path))
``