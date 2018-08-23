# text-analysis


Python3
pip3 install nltk --user

Clone the repository, step into it, go to python3 interpreter and test:

sentsim = MihalceaSentSimBNC()
sentsim.download_nltk_resources()
text1 = "The trainee program provides me with the knowledge and skills I need to do my job well"
text2 = "I have the opportunity for active practice through the trainee program (e.g., using knowledge form sessions, projects in the job"
res = sentsim.similarity(text1, text2)
print("Text1: {}\nText2: {}\n{}".format(text1, text2, res))
