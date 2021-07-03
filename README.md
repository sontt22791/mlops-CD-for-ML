[![Build and package RoBERTa-sequencing to Dockerhub](https://github.com/sontt22791/mlops-CD-for-ML/actions/workflows/main.yml/badge.svg)](https://github.com/sontt22791/mlops-CD-for-ML/actions/workflows/main.yml)

# mlops-CD-for-ML

## CD for ML
phần này về ý tưởng thì giống vs repos serving model using docker (https://github.com/sontt22791/mlops-serving-model-using-docker)

theo mình hiểu mục đích của phần này là: thay vì chỉ tạo docker images và push lên docker repos => thì mình 
nên lưu các thành phần của images đó (docker file, source code,..) để khi cần update sẽ dễ dàng hơn.

Tuy nhiên mỗi lần update code,... thì sẽ cần build lại docker images
=> vì vậy CD đã xuất hiện để khi update code thì images sẽ đc tự động build và upload lên docker repos

## tạo project theo cách manual trước

```
1. tạo dockerfile
2. copy model, server.py vào docker và run (download model ở https://github.com/onnx/models/tree/master/text/machine_comprehension/roberta)
```

Note: 
1. trong sách code phần app.py đang sai phần inputs => fai fix lại mới đc
2. trên win có thể dùng git bash để run curl

### build and run docker:
(file images khá nặng ~ 4gb nên khi dùng xong nên remove đi)
```
docker build -t alfredodeza/roberta .
docker run -it -p 5000:5000 --rm alfredodeza/roberta
(-rm để remove container sau khi stop
-d để ko hiện ra bash shell)
```

### Infrastructure as Code for Continuous Delivery of ML Models
phần này do chưa có acc azure nên mình chưa practice đc.

Flow của bước này là thay vì upload model lên github (size lớn), model nên được storage ở chỗ khác, và sẽ đc download về khi github actions run (trong sách tác giả lưu ở Registering model của azure ml => vì vậy sẽ cần authentication trước khi down về)

sau khi build xong, images sẽ được push lên Docker Hub hoặc GitHub Container Registry

mình đã thay đổi phần download model, thay vì lưu model trong azure ml thì mình đã download trực tiếp bằng
wget url_model, cụ thể:
```
1. mình nhận thấy lệnh run trong workflow cũng dùng như cli bình thường, vì vậy mình đã dùng wget để download model
2. do step đầu tiên của flow là clone repos về, vì vậy khi download model ở bước 1 thì model đc đc lưu ở ./
=> vì vậy cần move sang folder webapp (hoặc sửa Dockerfile để copy)
3. mình sử dụng Github package thay vì Docker Hub => vì vậy cần fai setup cho Github package theo các bước:
- tạo Personal access tokens (PAT): vào setting => vào develop setting => Personal access tokens => Generate new token => copy token (token này chỉ hiện 1 lần duy nhất khi tạo)
- vào repos => chọn setting => chọn secrets => khai báo variable GH_REGISTRY (https://github.com/sontt22791/mlops-CD-for-ML/settings/secrets/actions)
4. setup để login vào github package + build dockerfile => push
note: tag của images fai match vs tên acc và repos

Sau khi run xong, vào github package và có thể pull images về docker
https://github.com/sontt22791/mlops-CD-for-ML/pkgs/container/flask-roberta

để pull images về local từ github package, cần fai login github package ở local trước (https://github.community/t/push-or-pull-on-ghcr-package-results-in-error-when-authenticating-with-an-oauth-app/131660)
docker login ghcr.io -u sontt22791
```

## ONNX là gì?
https://viblo.asia/p/pytorch-tutorial-deploy-mo-hinh-pytorch-len-web-browser-su-dung-onnxjs-YWOZroLRlQ0

```
là 1 framework trung gian dùng để biểu diễn 1 model AI đc train từ các fw khác như tensorflow, pytorch,caffe,..

=> vì vậy sau khi train và save model xong, có thể load model đó lên và convert sang ONNX để sử dụng
```

