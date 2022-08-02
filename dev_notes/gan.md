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

---

- Generator
    - Learning
        - noise ξ → **Generator** → X̂ (that can compose an image) → **Discriminator** → Ŷ<sub>d</sub> → Cost<sub>output Ŷ</sub>
        - use Cost to update the parameters θ<sub>g</sub> of the Generator.
    - It learns the probability of features X
        - P(X<sub>features</sub> | Y<sub>class</sub>)
        - if you're generating lots of  different classes, you can pass into a class of generator
    - The generator takes as input *noise* (random features)
- loss function: BCE
    - Binary Cross Entropy function, or BCE for short, is used for training GANs. 
    - It's useful for these models, because it's especially designed for classification tasks, where there are 2 categories like, real and fake. 
    - Logistic Regression
- Training GANs: 
    - Distriminator
        - noise ξ → **Generator** → X̂ (that can compose an image) **+ X (both real and fake examples)** → **Discriminator** → Ŷ<sub>d</sub> → Cost<sub>output Ŷ</sub>
        - use Cost to update the parameters θ<sub>d</sub> of the Discriminator.
    - Generator
        - noise ξ → **Generator** → X̂ (that can compose an image) → **Discriminator** → Ŷ<sub>d</sub> → Cost<sub>output Ŷ</sub>
        - use Cost to update the parameters θ<sub>g</sub> of the Generator.
- GANs train in an alternating fashion, it's important to keep in mind that **both models should improve together** and should be kept at similar skill levels from the beginning of training. 
    - if you had a discriminator that is superior than the generator, like super, super good, you'll get predictions from it telling you that all the fake examples are 100% fake. Well, that's not useful for the generator, the generator doesn't know how to improve. Everything just looks super fake, there isn't anything telling it to know which direction to go in.
    - Meanwhile, if you had a superior generator that completely outskills the discriminator, you'll get predictions telling you that all the generated images are 100% real. 


- [Inputs to a Pre-trained GAN](https://colab.research.google.com/github/https-deeplearning-ai/GANs-Public/blob/master/C1W1_(Colab)_Inputs_to_a_pre_trained_GAN.ipynb)


