prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: prompt_b

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): It divides the prompt into organised structure and sections (i.e. Role, Task, Steps etc.), 
# allowing AI to recognise at one glance what the prompt is about.

# Your answer (Reason 2): It gives clear and precise instructions to AI by listing the desired output, 
# and also added the 'audience' and 'constraint' of output. 

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: prompt_a gives more detailed description of the background of the situation and the output, 
# which helps AI to better understand the context for analysis.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer: I would give a more detailed description of the output I want, borrowed from prompt_a on the part of presenting the findings to CEO
# in a way that is easy to understand and summarise everything in a short executive summary paragraph. 
# This provides clear and precise instructions to AI and allow an ideal response which is closer to my specifications.
# Following is my rewritten prompt_b:
""" 
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in a short executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise, free of technical jargon and easy to understand.
"""
