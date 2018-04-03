import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	#frameを表示
	cv2.imshow('camera capture', frame)

	#10msecキー入力待ち
	k = cv2.waitKey(10)
	#Escキーを押されたら終了
	if k == 27:
		break

#キャプチャを終了
cap.release()
cv2.destroyAllWindows()
