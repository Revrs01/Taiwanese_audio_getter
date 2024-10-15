Taibun Correction Audio Getter
---
## Why we need this ?
Audio is stored inside Taibun's server `140.116.153.134`, we don't want to move it to our server since audio is saved to Taibun's server after taking a test for student. 
You should place this repo into `C:\Program Files\Taiwanese_Correction\Taiwanese_Correction_v2`, same layer as `Taiwanese_Correction_frontend`

## RUN
```bash
docker compose up --build -d
```

## STOP
```bash
docker compose down
```