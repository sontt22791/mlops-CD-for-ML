﻿# mlops-CD-for-ML

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
phần này do chưa có acc azure nên mình chưa practice đc. flow của bước này là thay vì upload model lên github (size lớn), model nên được storage ở chỗ khác, và sẽ đc download về khi github actions run (trong sách tác giả lưu ở Registering model của azure ml => vì vậy sẽ cần authentication trước khi down về)

sau khi build xong, images sẽ được push lên Docker Hub hoặc GitHub Container Registry

## ONNX là gì?
https://viblo.asia/p/pytorch-tutorial-deploy-mo-hinh-pytorch-len-web-browser-su-dung-onnxjs-YWOZroLRlQ0

```
là 1 framework trung gian dùng để biểu diễn 1 model AI đc train từ các fw khác như tensorflow, pytorch,caffe,..

=> vì vậy sau khi train và save model xong, có thể load model đó lên và convert sang ONNX để sử dụng
```

