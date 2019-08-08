
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple

docker run --rm -it --entrypoint="manim" -v `pwd`/output:/media -v `pwd`:/work  manim:v1  /work/example_scenes.py SquareToCircle -pl



