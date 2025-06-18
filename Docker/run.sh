# 호스트에서 DISPLAY 변수와 X 권한 공유
xhost +local:root
docker run -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --name antlr-gui \
  antlr-zsh-env

