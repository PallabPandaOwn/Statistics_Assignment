
# coding: utf-8

# ## 2.1. Problem Statement: STATISTICS 1

# ### Question - 1. You survey households in your area to find the average rent they are paying. Find the standard deviation from the following data:
# $1550, $1700, $900, $850, $1000, $950.

# In[3]:


import statistics as st
from functools import reduce
# Create the dataset for the same
rent = [1550, 1700, 900,850, 1000,950]
# Calculate the mean of the list
mean = sum(rent)/len(rent)
print ("Mean is : ", mean)
# Calculate the variance
diff_mean = list(map(lambda x : (x - mean)**2 , rent))
var = sum(diff_mean)/len(rent)
print ("Variance is : ", var)
# Calculate the standard deviation
sd = var ** 0.5
print ("Standard Deviation is : ", sd)


# ### Question 2. Find the variance for the following set of data representing trees in California (heights in feet):
# 3, 21, 98, 203, 17, 9

# In[4]:


trees = [3, 21, 98, 203, 17, 9]
# Calculate mean 
mean = sum(trees)/len(trees)
# Calculate the variance
diff_mean = list(map(lambda x : (x - mean)**2 , trees))
var = sum(diff_mean)/len(trees)
print ("Variance is : ", var)


# ### Question 3. In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed in two subjects and 3 failed in three subjects. Find the probability distribution of the variable for number of subjects a student from the given class has failed in.

# In[5]:


print ("Total number of students in the class : 100")
print ("Probability of failing in {} subjects : {}".format(0, 80/100))
print ("Probability of failing in {} subjects : {}".format(1, 10/100))
print ("Probability of failing in {} subjects : {}".format(2, 7/100))
print ("Probability of failing in {} subjects : {}".format(3, 3/100))


# ### Based on the above data the probability distribution can be shown as below
# 
#  PROBABILITY | 0   | 1   | 2   | 3   |
# -------------|-----|-----|-----|-----|
#  P(X)        | 0.8 | 0.1 | 0.07| 0.03| 

# ### 2.2. Problem Statement: STATISTICS 2

# In[12]:


import math


# ### FORMULA TO CALCULATE BINOMIAL DISTRIBUTION IS :
# P (‘k’ successes in ‘n’ trials) = C(n,k)sk(1−s)(n−k) 
# 
# s = the probability of success and 
# 
# (1-s) = the probability of failure (or complement of the event)
# 
# n = Total number of trials
# 
# K = number of specific events we want to obtain
# 
# Also nCr represents selection of r events from n, it can be written as: nCk = n!/k!(n−k)!     

# ### A test is conducted which is consisting of 20 MCQs (multiple choices questions) with every MCQ having its four options out of which only one is correct. Determine the probability that a person undertaking that test has answered exactly 5 questions wrong.

# In[13]:


n = 20        # number of samples
s = 5
k = 15

# Probability of success 
p = 1/4
# Proability of Failure
q = 1 - p

# Percentage computation
# 20!/15!(5!) * ((1/4) ** 15) * ((3/4) ** 5)

array = [i for i in range(1,21)]
n_fact = reduce(lambda x,y : x * y, array)
pass_fact = reduce(lambda x,y : x * y, array[0:15])
fail_fact = reduce(lambda x,y : x * y, array[0:5])

# Probaility of 5 failures
prob= (n_fact/(pass_fact*fail_fact)) * (p ** k ) * (q ** s)
print ("PRoabailty to get 5 wrong is : ", prob)


# ### A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5 times.

# In[14]:


n = 50
#success count
k = 5
# Failure
s = 50 -k    # 45

# Probabilty of success 
p = 1/5    # As it is A to E, there are only 5 possibilties
# Probiblity of failure
q = 1 - p

# Compute the probavilty
prob = (math.factorial(n) / (math.factorial(k) * math.factorial(s))) * (p ** k) * (q ** s)
print ("PRoabailty to get D 5 times is : ", prob)


# ### Two balls are drawn at random in succession without replacement from an urn containing 4 red balls and 6 black balls. Find the probabilities of all the possible outcomes.

# Total Number of balls : 10<br>
# Probabilty of two reds    : RR : P(R) * P(R) : (4/10) * (3/9) &emsp; : 2/15 &emsp; :This because without replacement<br>
# Probabilty of red & black : RB : P(R) * P(B) : (4/10) * (6/9) &emsp; : 4/15 &emsp; :This because without replacement<br>
# Probabilty of black & red : BR : P(B) * P(R) : (6/10) * (4/9) &emsp; : 4/15 &emsp; :This because without replacement<br>
# Probabilty of two blacks  : BB : P(B) * P(B) : (6/10) * (5/9) &emsp; : 1/3  &emsp;&nbsp;&nbsp; :This because without replacement<br>
# <br>
# <br>
# Probabilty of 2 Reds &emsp;  &emsp; &emsp;  &emsp;         : 2/15        : 2/15<br>
# Probabilty of 1 red and 1 black : 4/15 + 4/15 : 8/15<br>
# Probabilty of 3 blacs &emsp; &emsp; &emsp;  &emsp;         : 1/3         : 1/3
# 

# ### 2.3. Problem Statement: STATISTICS 3

# ### Blood glucose levels for obese patients have a mean of 100 with a standard deviation of 15. A researcher thinks that a diet high in raw cornstarch will have a positive effect on blood glucose levels. A sample of 36 patients who have tried the raw cornstarch diet have a mean glucose level of 108. Test the hypothesis that the raw cornstarch had an effect or not.

# Hypothesis: <br><br>
# H0 : 𝜇 = 100 <br>
# HA : 𝜇 > 100<br>
# <br><br>
# Population mean = 100 <br>
# Population Standard Deviation = 15<br>
# <br>
# Sample size = 36<br>
# mean = 108<br>
# <br>
# Use the Z statics as SD for population is given<br>
# z = (sample mean - population mean)/ (standard Deviation/square root of sample size)<br><br>
# Alpha = 0.05

# In[18]:


Z_stat = (108-100)/(15/(36)**0.5); Z_stat


# P value from the Z table table : 0.9993
# Z-critical value = 1.645
# 
# ### CONCLUSION
# Clearly the Z computed value is greater than the Z-critical Value, indicating it is in the rejection area.<br>
# Also the p value is greater than the Alpha value.<br>
# As a result the null hypothesis will be rejected.

# ### In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple random sample of 100 voters are surveyed from each state. 
# 
# ### What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?

# The above is a Propotion Problem<br>
# <br>
# P1 = Propotion of Republicans in the First state = 0.52<br>
# P2 = Propotion of Republicans in the Second state = 0.47<br>
# p1 = Propotion of Democrats in the First state = 0.48<br>
# p2 = Propotion of Democrats in the Secons state = 0.53<br>
# <br>
# Check whether the sample sizes are big. Remeber p1 = 1 - P1 and p2 = 1 - P2<br>
# n1P1 = 100 * 0.52 = 52<br>
# n1(1 - P1) = 100 * 0.48 = 48<br>
# n1P2 = 100 * 0.47 = 47<br>
# n1(1 - P2) = 100 * 0.53 = 53<br>
# <br>
# Clearly the sample sizes are big enough<br>
# <br>
# Difference in means = E(p1 - p2) = P1 - P2 = 0.52 - 0.47 = 0.05<br>
# <br>
# Standard Deviation Formula is :<br>
# σd = sqrt{ [P1(1 - P1) / n1 ] + [ P2(1 - P2) / n2 ] } 
# 

# In[19]:


sd = (((0.52 * 0.48)/100) + ((0.47 * 0.53)/100)) ** 0.5; sd


# Compute the Z score for the same
# z (p1 - p2) = (x - μ p1 - p2 ) / sd

# In[20]:


z_score = (0 - 0.05) / sd; z_score


# ### The value from the Z-table for -0.071 is 0.24.

# ### You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard deviation is 209. How well did you score on the test compared to the average test taker?

# In[22]:


Z = (1100 - 1026)/209
Z


# ### Your score 0.354 from the mean

# ### 2.4. Problem Statement: STATISTICS 4

# Is gender independent of education level? A random sample of 395 people were surveyed and each person was asked to report the highest education level they obtained. The data that resulted from the survey is summarized in the following table:<br>
# <br>High School Bachelors Masters Ph.d. Total<br>
# Female 60 54 46 41 201<br>
# Male 40 44 53 57 194<br>
# Total 100 98 99 98 395<br>
# <br>
# Question: Are gender and education level dependent at 5% level of significance? In other words, given the data collected above, is there a relationship between the gender of an individual and the level of education that they have obtained?<br>

# ![Problem_Statement_1_Solution](Picture\ChiSquareAssignment.png)

# ### PROBLEM STATEMENT 2
# 
# Using the following data, perform a oneway analysis of variance using α=.05. Write up the results in APA format.
# <br><br>
# [Group1: 51, 45, 33, 45, 67]<br>
# [Group2: 23, 43, 23, 43, 45]<br>
# [Group3: 56, 76, 74, 87, 56]<br>

# ![Problem_Statement_2_Solution](Picture\AnnovaAssignment1.png)

# ### PROBLEM STATEMENT 3
# 
# Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25.

# ![Problem_Statement_3_Solution](Picture\AnnovaAssignment2.png)
