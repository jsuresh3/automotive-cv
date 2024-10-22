import os
import ultralytics
from ultralytics import YOLO
import cv2


video_path = '../test_videos/test.mp4'
video_path_out = '../test_videos/test_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame.shape[1], frame.shape[0]))

model_path = f'../models/yolov8m.pt'

# Load a model
  # load a custom model
model = YOLO(model_path)

color_map = {
      0: (0, 0, 255),
      1: (0, 255, 0),
      2: (255, 0, 0),
      3: (0, 255, 255),
      4: (255, 255, 0),
      5: (255, 0, 255),
      6: (255, 255, 255),
      7: (0, 0, 0),
      8: (128, 128, 128),
    # Add more colors if needed
}



while ret:

    cv2.putText(frame, (f"YOLOv8-s-run-"), (0, 0),cv2.FONT_HERSHEY_SIMPLEX, 1.3, color_map[8], 3, cv2.LINE_AA)
    results = model(frame)[0]
    threshold = 0.3
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold and class_id < 8:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper()+" "+(f'{score*100:.2f}'), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, color_map[int(class_id)], 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()