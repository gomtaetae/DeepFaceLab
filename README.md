# Face Swap Configuration Guide

## 학습 과정 결과

### 학습 300번 이미지 사진 60개 좌우상하 반전 학습
처음 결과:
![image](https://github.com/user-attachments/assets/048e225a-036d-406c-80f3-f1c3b0366e77)

### 학습 300번 이미지 사진 300개 좌우상하 반전 학습
두번째 결과:
![image](https://github.com/user-attachments/assets/ab7e1d28-acbd-44b3-8eba-a201d4a109e7)

### 학습 500번 이미지 사진 300개 좌우상하 반전 학습
세번째 결과:
![image](https://github.com/user-attachments/assets/58337dae-167c-4e52-943d-ddb0ebefa763)

-------------------------------------

## 실행 명령어

### 1. DeepFaceLab 환경 설정

cd ./DeepFaceLab/
.venv/Scripts/activate



# 비디오 변환
python main.py videoed extract-video --input-file 7.mp4 --output-dir data_src

# DRS 얼굴 나누기
python main.py extract --input-dir data_src --output-dir data_src/aligned

# DST 얼굴 나누기
python main.py extract --input-dir data_dst --output-dir data_dst/aligned

# 라스트 학습 명령어
python main.py train \
    --training-data-src-dir data_src/aligned \
    --training-data-dst-dir data_dst/aligned \
    --model-dir model \
    --model SAEHD \
    --gpu 0 \
    --autobackup 1 \
    --write-preview-history y \
    --target-iteration 5000 \
    --flip-src y \
    --flip-dst y \
    --batch-size 8 \
    --resolution 128 \
    --face-type wf \
    --ae-architecture liae-ud \
    --ae-dimensions 256 \
    --encoder-dimensions 64 \
    --decoder-dimensions 64 \
    --decoder-mask-dimensions 32 \
    --masked-training y \
    --eyes-mouth-priority y \
    --uniform-yaw-distribution n \
    --blur-mask y \
    --use-gpu y \
    --use-adabelief y \
    --use-learning-rate-dropout n \
    --enable-random-warp y \
    --random-hue-saturation-light 0.0 \
    --gan-power 2.0 \
    --gan-patch-size 16 \
    --gan-dimensions 16 \
    --face-style-power 0.0 \
    --background-style-power 0.0 \
    --color-transfer rct \
    --enable-gradient-clipping n \
    --enable-pretraining n

# 학습 데이터 합성
python main.py merge \
    --input-dir data_dst \
    --output-dir data_dst/merged \
    --output-mask-dir data_dst/merged_mask \
    --aligned-dir data_dst/aligned \
    --model-dir model \
    --model SAEHD

# 동영상 변환
python main.py videoed video-from-sequence \
    --input-dir data_dst/merged \
    --output-file data_dst/final_video6.mp4 \
    --reference-file data_dst/"1-1.mp4"


------------------------------------


# DeepFaceLab Training Configuration

## 1. GPU 선택
**질문:** `[0] Which GPU indexes to choose?`  
**설명:** 사용할 GPU를 선택합니다. GTX 1660 SUPER는 사용 가능한 GPU로 `0`을 입력하여 선택합니다.  
**추천 설정:** `0`

## 2. 자동 백업
**질문:** `[0] Autobackup every N hour ( 0..24 ?:help )`  
**설명:** 몇 시간마다 훈련 모델을 자동으로 백업할지 설정합니다.  
**추천 설정:** `1` (한 시간 간격으로 백업)

## 3. 미리보기 기록
**질문:** `[n] Write preview history ( y/n ?:help )`  
**설명:** 훈련 중 생성된 미리보기 이미지를 기록할지 여부입니다.  
**추천 설정:** `y` (훈련 과정을 나중에 분석 가능)

## 4. 미리보기 이미지 선택
**질문:** `[n] Choose image for the preview history ( y/n )`  
**설명:** 미리보기 기록에 특정 이미지를 저장할지 여부입니다.  
**추천 설정:** `n` (필요하지 않음)

## 5. 목표 반복 횟수
**질문:** `[0] Target iteration`  
**설명:** 훈련을 몇 번 반복할지 설정합니다.  
**추천 설정:** `5000` (적당한 시작 값)

## 6. SRC 얼굴 랜덤 플립
**질문:** `[n] Flip SRC faces randomly ( y/n ?:help )`  
**설명:** 소스 이미지를 수평으로 뒤집을지 설정합니다.  
**추천 설정:** `y` (다양한 각도로 학습 가능)

## 7. DST 얼굴 랜덤 플립
**질문:** `[y] Flip DST faces randomly ( y/n ?:help )`  
**설명:** 대상 이미지를 수평으로 뒤집을지 설정합니다.  
**추천 설정:** `y` (학습 다양성 증가)

## 8. 배치 크기
**질문:** `[4] Batch_size`  
**설명:** 한 번에 학습할 데이터 수를 설정합니다.  
**추천 설정:** `8` (GTX 1660 SUPER에 적합, VRAM 부족 시 4로 설정)

## 9. 해상도
**질문:** `[128] Resolution`  
**설명:** 학습 이미지의 해상도를 설정합니다.  
**추천 설정:** `128` (GTX 1660 SUPER에서 적합한 크기)

**해상도 깨질 때:**
```plaintext
resolution: 256
ae_dims: 512
e_dims: 128
d_dims: 128
d_mask_dims: 64
```

## 10. 얼굴 타입
**질문:** `[f] Face type ( h/mf/f/wf/head ?:help )`  
**설명:** 학습할 얼굴 영역의 유형을 설정합니다.  
**추천 설정:** `wf` (자연스러운 결과)

## 11. AE 아키텍처
**질문:** `[liae-ud] AE architecture`  
**설명:** AutoEncoder의 구조를 설정합니다.  
**추천 설정:** `liae-ud` (고품질 변환)

## 12. AutoEncoder/Encoder/Decoder 차원
**추천 설정:**  
- `AutoEncoder`: 256  
- `Encoder`: 64  
- `Decoder`: 64  
- `Mask`: 32  

## 13. 마스킹
**질문:** `[y] Masked training ( y/n ?:help )`  
**추천 설정:** `y`

## 14. 눈과 입 우선 학습
**질문:** `[n] Eyes and mouth priority ( y/n ?:help )`  
**추천 설정:** `y`

## 15. Yaw 분포
**질문:** `[n] Uniform yaw distribution of samples ( y/n ?:help )`  
**추천 설정:** `n`

## 16. 마스크 블러링
**질문:** `[n] Blur out mask ( y/n ?:help )`  
**추천 설정:** `y`

## 17. GPU 최적화
**질문:** `[y] Place models and optimizer on GPU ( y/n ?:help )`  
**추천 설정:** `y`

## 18. AdaBelief 옵티마이저
**질문:** `[y] Use AdaBelief optimizer? ( y/n ?:help )`  
**추천 설정:** `y`

## 19. 학습률 드롭아웃
**질문:** `[n] Use learning rate dropout ( n/y/cpu ?:help )`  
**추천 설정:** `n`

## 20. 랜덤 왜곡
**질문:** `[y] Enable random warp of samples`  
**추천 설정:** `y`

## 21. Hue/Saturation/Light
**추천 설정:** `0.0`

## 22. GAN 관련 설정
**추천 설정:**  
- `GAN 파워`: 2.0  
- `GAN 패치 크기`: 16  
- `GAN 차원`: 16  

## 23. 스타일 파워
**추천 설정:** `0.0`

## 24. 색상 전이
**추천 설정:** `rct`

## 25. Gradient Clipping
**추천 설정:** `n`

## 26. 프리트레이닝
**추천 설정:** `n`

