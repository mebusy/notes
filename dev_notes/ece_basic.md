[](...menustart)

- [Basic Electronics For Beginners](#7410fe92490df7c6dd5b98e039e1e174)
    - [Electricity](#656e43581640c08d44b1eb0228846623)
    - [Resistors](#d6df7f2e127bb9b8363cb35de92256fc)
    - [LED](#53e0dbc06e48e3d381ac224fa8bae3df)
    - [Potentiometer](#95d3f279bc717c9008a09a17c0bebe62)
    - [Capacitors](#d2b1424142f79db620855ab8b666e28c)
    - [Diodes](#dfcc5315f4c70a99d2103f74cfa1ac6e)
    - [Transistors](#3ab62a78a6c53ea42fec023a55b3a3e3)
    - [Integrated Circuits](#7bf2084fde7f81e2912434fdfffb4148)

[](...menuend)


<h2 id="7410fe92490df7c6dd5b98e039e1e174"></h2>

# Basic Electronics For Beginners

<h2 id="656e43581640c08d44b1eb0228846623"></h2>

## Electricity

- there are 2 types of electrical signals
    - AC (alternating current)
        - the electricity flows throughout the circuit is constantly reversing.
        - the rate of reversal is measured in Hertz.
    - DC (direct current)
        - the electricity flows in one direction, between the power and groud.
        - you can test is by reading a battery with a volting meter


<h2 id="d6df7f2e127bb9b8363cb35de92256fc"></h2>

## Resistors

- Voltage, Current, Resistance
- Resistor color
    - ![](https://www.circuits-diy.com/wp-content/uploads/2019/08/how-to-read-resistor-values.png)
- Power
    - if apply too much voltage to the resistor,  the resistor can get hot and burn up.
    - so you need to control how much power you deliver to a resistor
    - let's the power rating(额定功率) of the resistor is P', then
        ```
        P' = V·I = V²/R
        R·P' = V²
        V = √(R·P') 
        ```
- Series vs Parallel
    - resisitors connected in Parallel(并联)
        ```
        R = (1/R₁ + 1/R₂ + ...)⁻¹
        ```
<h2 id="53e0dbc06e48e3d381ac224fa8bae3df"></h2>

## LED
    - light emitting diode (发光二极管)
    - monochromatic light sources, they generate light of one specific wavelength
    - a typical led has a voltage drop of 2V, and the amount of current usually flows to it vary between 0.1mA~20mA.

<h2 id="95d3f279bc717c9008a09a17c0bebe62"></h2>

## Potentiometer
    - a variable resistor
    - a device where you can adjust the resistance of a circuit.
    - ![](https://www.digikey.com/-/media/Images/Article%20Library/TechZone%20Articles/2021/May/The%20Fundamentals%20of%20Digital%20Potentiometers%20and%20How%20to%20Use%20Them/article-2021may-the-fundamentals-of-digital-fig2.jpg?la=en&ts=a24aae58-168d-4fc7-aecb-f7a0054db6e3)

- Solar Cells(太阳能电池)
    - converts light energy into electricity.
    - os it is a power source, more specifically  a DC power source.


<h2 id="d2b1424142f79db620855ab8b666e28c"></h2>

## Capacitors

- a component that stores electricity and then discharges it into the circuit when there is a drop in electricity.
    - think of it as a water storage tank that release water when there is a drought to ensure a steady stream.
- electrolytic capacitors are typically polarized, that means `-` pin needs to be connected to the groud side of the circuit, and the `+` pin must be connected to power. 
    - if it is connected backwards, it won't work correctly.


<h2 id="dfcc5315f4c70a99d2103f74cfa1ac6e"></h2>

## Diodes

- components which are polarized, they only allow electricall current to pass through them in one direction.
    - this is useful in that it can be placed in a circuit to prevent electricity from flowing in the wrong direction.
- typically results 0.7V voltage drop


<h2 id="3ab62a78a6c53ea42fec023a55b3a3e3"></h2>

## Transistors

- takes in a small electrical current as its base pin and amplifies it such that a much larger current can pass between its collector and emitter pins.
    - the amount of current that passes between these 2 pins is proportional to the voltage being applied at the base pin.
- 2 basic type of transistors, they have opposite polarity between collector and emitter.
    1. NPN
    2. PNP
- BJT
    - ![](https://i0.wp.com/ettron.com/wp-content/uploads/2020/07/image-1.jpg?resize=333%2C281&ssl=1)

<h2 id="7bf2084fde7f81e2912434fdfffb4148"></h2>

## Integrated Circuits

- pin order
    - ![](http://www.mobilecellphonerepairing.com/counting-legs-or-pins-of-ic.html)


