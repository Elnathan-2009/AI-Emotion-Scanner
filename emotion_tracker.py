import cv2
from deepface import DeepFace

def get_camera():
    # Try external webcam first (index 1)
    cap = cv2.VideoCapture(1)
    if cap.isOpened():
        print("Using external webcam")
        return cap

    # Fallback to default camera (index 0)
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        print("Using built-in camera")
        return cap

    # No camera found
    print("No camera available")
    return None

cap = get_camera()

if cap is None:
    exit()

frame_count = 0
emotion = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    status = "Absent"
    focus = ""

    try:
        # Run emotion detection every 20 frames (performance boost)
        if frame_count % 20 == 0:
            results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        if results:
            status = "Present"

            for face in results:
                x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
                emotion = face['dominant_emotion']

                # Draw box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Emotion text
                cv2.putText(frame, emotion, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    except:
        status = "Absent"

    # Focus logic
    if emotion in ["sad", "angry", "fear"]:
        focus = "Low Focus"
    elif emotion != "":
        focus = "Focused"

    # Display system info
    cv2.putText(frame, f"Status: {status}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    if emotion:
        cv2.putText(frame, f"Emotion: {emotion}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    if focus:
        cv2.putText(frame, f"Focus: {focus}", (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("AI Focus Tracker", frame)

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()