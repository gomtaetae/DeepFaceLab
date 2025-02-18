 cd .\DeepFaceLab\ 

.\.venv\Scripts\activate


비디오변환
python main.py videoed extract-video --input-file 7.mp4 --output-dir data_src

drs 얼굴나누기
python main.py extract --input-dir data_src --output-dir data_src/aligned

dst 얼굴나누기
python main.py extract --input-dir data_dst --output-dir data_dst/aligned

라스트 학습 명령어
python main.py train --training-data-src-dir data_src/aligned --training-data-dst-dir data_dst/aligned --model-dir model --model SAEHD


학습데이터 합성
python main.py merge --input-dir data_dst --output-dir data_dst/merged --output-mask-dir data_dst/merged_mask --aligned-dir data_dst/aligned --model-dir model --model SAEHD


동영상 변환
python main.py videoed video-from-sequence --input-dir data_dst/merged --output-file data_dst/final_video6.mp4 --reference-file data_dst/"1-1.mp4" 

final_video -> 변경할 비디오 이름
"my original_video.mp4" 원본 동영상 이름


-------------------------------------
1. GPU 선택
질문: [0] Which GPU indexes to choose?
설명: 사용할 GPU를 선택합니다. GTX 1660 SUPER는 사용 가능한 GPU로 0을 입력하여 선택합니다.
추천 설정: 0

2. 자동 백업
질문: [0] Autobackup every N hour ( 0..24 ?:help )
설명: 몇 시간마다 훈련 모델을 자동으로 백업할지 설정합니다.
추천 설정: 1 (한 시간 간격으로 백업)

3. 미리보기 기록
질문: [n] Write preview history ( y/n ?:help )
설명: 훈련 중 생성된 미리보기 이미지를 기록할지 여부입니다.
추천 설정: y (훈련 과정을 나중에 분석 가능)

4. 미리보기 이미지 선택
질문: [n] Choose image for the preview history ( y/n )
설명: 미리보기 기록에 특정 이미지를 저장할지 여부입니다.
추천 설정: n (필요하지 않음)

5. 목표 반복 횟수
질문: [0] Target iteration
설명: 훈련을 몇 번 반복할지 설정합니다.
추천 설정: 5000 (적당한 시작 값)

6. SRC 얼굴 랜덤 플립
질문: [n] Flip SRC faces randomly ( y/n ?:help )
설명: 소스 이미지를 수평으로 뒤집을지 설정합니다.
추천 설정: y (다양한 각도로 학습 가능)

7. DST 얼굴 랜덤 플립
질문: [y] Flip DST faces randomly ( y/n ?:help )
설명: 대상 이미지를 수평으로 뒤집을지 설정합니다.
추천 설정: y (학습 다양성 증가)

8. 배치 크기
질문: [4] Batch_size
설명: 한 번에 학습할 데이터 수를 설정합니다.
추천 설정: 8 (GTX 1660 SUPER에 적합, VRAM 부족 시 4로 설정)

9. 해상도
질문: [128] Resolution
설명: 학습 이미지의 해상도를 설정합니다.
추천 설정: 128 (GTX 1660 SUPER에서 적합한 크기)

해상도 깨질때
resolution: 256
ae_dims: 512
e_dims: 128
d_dims: 128
d_mask_dims: 64

10. 얼굴 타입
질문: [f] Face type ( h/mf/f/wf/head ?:help )
설명: 학습할 얼굴 영역의 유형을 설정합니다.
h: 전체 머리
mf: 대부분 얼굴
f: 얼굴만
wf: 넓은 얼굴
head: 얼굴과 목 포함
추천 설정: wf (자연스러운 결과)

11. AE 아키텍처
질문: [liae-ud] AE architecture
설명: AutoEncoder의 구조를 설정합니다.
추천 설정: liae-ud (고품질 변환)

12. AutoEncoder/Encoder/Decoder 차원
질문: [256] AutoEncoder dimensions, [64] Encoder dimensions, [64] Decoder dimensions, [32] Decoder mask dimensions
설명: 모델의 각 부분의 차원 크기를 설정합니다.
추천 설정:
AutoEncoder: 256
Encoder: 64
Decoder: 64
Mask: 32

13. 마스킹
질문: [y] Masked training ( y/n ?:help )
설명: 얼굴 외곽만 학습하도록 설정합니다.
추천 설정: y

14. 눈과 입 우선 학습
질문: [n] Eyes and mouth priority ( y/n ?:help )
설명: 눈과 입을 더 정확히 학습하도록 우선순위를 설정합니다.
추천 설정: y

15. Yaw 분포
질문: [n] Uniform yaw distribution of samples ( y/n ?:help )
설명: Yaw(얼굴 각도) 샘플 분포를 균등하게 설정할지 여부입니다.
추천 설정: n
(얼굴 각도가 여러개일때 y로 하면 좋음)

16. 마스크 블러링
질문: [n] Blur out mask ( y/n ?:help )
설명: 마스크 경계를 흐릿하게 설정합니다.
추천 설정: y

17. GPU 최적화
질문: [y] Place models and optimizer on GPU ( y/n ?:help )
설명: 모델과 최적화 과정을 GPU에 올릴지 설정합니다.
추천 설정: y

18. AdaBelief 옵티마이저
질문: [y] Use AdaBelief optimizer? ( y/n ?:help )
설명: 더 나은 안정성과 수렴 속도를 위한 AdaBelief를 사용할지 설정합니다.
추천 설정: y

19. 학습률 드롭아웃
질문: [n] Use learning rate dropout ( n/y/cpu ?:help )
설명: 학습률 드롭아웃을 사용할지 설정합니다.
추천 설정: n

20. 랜덤 왜곡
질문: [y] Enable random warp of samples
설명: 샘플에 랜덤 왜곡을 추가하여 다양한 학습 데이터를 생성합니다.
추천 설정: y

21. Hue/Saturation/Light
질문: [0.0] Random hue/saturation/light intensity ( 0.0 .. 0.3 ?:help )
설명: 랜덤 색조, 채도, 밝기 강도를 설정합니다.
추천 설정: 0.0 (초보자 설정)

22. GAN 관련 설정
질문: [0.0] GAN power, [16] GAN patch size, [16] GAN dimensions
설명: GAN 학습 강도와 크기를 설정합니다.
추천 설정:
GAN 파워: 2.0
GAN 패치 크기: 16
GAN 차원: 16

23. 스타일 파워
질문: [0.0] Face style power, [0.0] Background style power
설명: 얼굴 및 배경 스타일 학습 강도를 설정합니다.
추천 설정: 0.0 (스타일 변경 필요 없을 경우)

24. 색상 전이
질문: [none] Color transfer for src faceset
설명: 소스 이미지의 색상을 대상 이미지 스타일에 맞춥니다.
추천 설정: rct

25. Gradient Clipping
질문: [n] Enable gradient clipping ( y/n ?:help )
설명: Gradient 폭발을 방지합니다.
추천 설정: n (VRAM 충분 시)

26. 프리트레이닝
질문: [n] Enable pretraining mode ( y/n ?:help )
설명: 모델을 일반적인 데이터로 사전 학습합니다.
추천 설정: n (필요 시만 y)
