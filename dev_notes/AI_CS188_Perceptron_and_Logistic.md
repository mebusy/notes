[](...menustart)

- [21. Perceptrons and Logistic Regression](#277ba134a739723dd3ce2fadba0049b6)

[](...menuend)


<h2 id="277ba134a739723dd3ce2fadba0049b6"></h2>

# 21. Perceptrons and Logistic Regression

The recent lectures was about probabilistic models. And if we train a probabilistic model over all variables that we might care about, we can then reuse that probabilistic model to make decisions for specific queries. For example, what's the probability of a class label y given some feature values f₁, ..., f<sub>n</sub>.

And that was one way you could reuse those models. And that's what we saw with naive Bayes for a specific type of Bayes net, you can use it to answer conditional queries about a class label.

Today we're going to look at solving that kind of problem, where we have a set of features and we want to output the decision on what class might be represented by those features. But we're **not going to learn a full probabilistic model**. We're gonna **focus on just the decision of going from features** to what the class label might be and **ignore learning a full probabilistic model**, which has some pros and cons. 

If you want a full probabilistic model you're not going to get it with the mothods from today. But if all you care about is that decision, today's method will zone in more on the particulars of that decision.


[lecture pdf](https://github.com/mebusy/cs188_fa18/blob/master/fa18_cs188_lectures_pdf/FA18_cs188_lecture21_perceptron_and_logistic_regression_1pp.pdf)


