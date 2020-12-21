
# GPU Accelerate on MacOSX

- PyTorch AMD (not support MacOSX)
    - The official AMD instructions on building Pytorch is [here](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#pytorch)

- OpenCL 
    - [GPU-Accelerated Machine Learning on MacOSX](https://towardsdatascience.com/gpu-accelerated-machine-learning-on-macos-48d53ef1b545)
    - [Deep Learning on a Mac with AMD GPU](https://fabrice-daniel.medium.com/deep-learning-on-a-mac-with-amd-gpu-4be1f18944a)

- Mac-optimized TensorFlow
    - CATUION: much slower than  tensorflow docker verison, no idea why...
    - To get started, visit Apple’s [GitHub repo](https://blog.tensorflow.org/2020/11/accelerating-tensorflow-performance-on-mac.html) for instructions to download and install the Mac-optimized TensorFlow 2.4 fork.
    ```bash
    python3.8 -m venv tf_osx
    source tf_osx/bin/activate

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/apple/tensorflow_macos/master/scripts/download_and_install.sh)"
    ```
    - select compute device
    ```bash
    # Import mlcompute module to use the optional set_mlc_device API for device selection with ML Compute.
    from tensorflow.python.compiler.mlcompute import mlcompute

    # Select CPU device.
    mlcompute.set_mlc_device(device_name=‘cpu’) # Available options are 'cpu', 'gpu', and ‘any'.
    ```

- TensofFlow docker 
    ```bash
    docker pull tensorflow/tensorflow:latest
    docker run --rm -v `pwd`:/scripts  tensorflow/tensorflow:latest python /scripts/tf_test.py
    ```







