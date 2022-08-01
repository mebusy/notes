# GAN

## Week 1

- [Pre-trained Model Exploration](https://colab.research.google.com/github/https-deeplearning-ai/GANs-Public/blob/master/C1W1_(Colab)_Pre_trained_model_exploration.ipynb)

### Intro to GANs

- Generative Adversarial Network
    - Generator
        - learns to make *fakes* that look *real*
        - you can think of the generator as a painting forger
        - the generator actually isn't very sophisticated. It doesn't know how to produce real looking artwork. Additionally, the generator isn't allowed to see the real images.
        - feed in a *noise vector*,  output a image
    - Discriminator
        - learns to distinguish *real* from *fake*
        - you can think of the discriminator as an art inspector
        - doesn't know what's ream and what's fake in the beginning, but is allowed to look at the real artwork, jumbled up with the fakes ones as well, and he doesn't know which one is which. That's for him to figure out and learn how to decide.
        - The discriminator is a **classifier**.

- Summary
    - The generator's goal is to fool the discriminator
    - The discriminator's goal is to distinguish between real and fake
    - They learn from the competition with each other
    - At the end, *fakes* look *real*


