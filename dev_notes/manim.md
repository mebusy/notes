
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple

docker run --rm -it --entrypoint="manim" -v `pwd`/output:/media -v `pwd`:/work  manim:v1  /work/example_scenes.py SquareToCircle -pl


在RUN apt-get update之前添加

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo 'deb http://mirrors.163.com/debian/ jessie main non-free contrib' > /etc/apt/sources.list && \
echo 'deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib' >> /etc/apt/sources.list && \
echo 'deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib' >> /etc/apt/sources.list



