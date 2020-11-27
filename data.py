
#######################
# Straw Poll Bulk Bot #
# @CodeChrisB         #
#######################
# You can change the Questions and Answers underneath
# Keep in mind that the quotation marks --> "" are 
# necessary, and should not be removed.
#If you only want 2 answers leave the others blank --> ""
YourQuestion = "Wer ist die gröẞere Bitch"
FirstAnswer ="Max"
SecondAnswer ="Lisa"
ThridAnswer =""
FourthAnswer =""
FifthAnswer =""
SixthAnswer =""
SeventhAnswer = ""
EighthAnswer = ""
NinthAnswer = ""
BulkNumber =1000000000 # How often do you want to send your question?



###########################
#      Do not change      #
#  the values underneath. #
###########################
class Data:
    def __new__(self):
        body = {
            "poll-title": YourQuestion,
            "options-option-1": FirstAnswer,
            "options-option-2": SecondAnswer,
            "options-option-3":ThridAnswer,
            "options-option-4": FourthAnswer,
            "options-option-5": FifthAnswer,
            "options-option-6": SixthAnswer,
            "options-option-7": SeventhAnswer,
            "options-option-8": EighthAnswer,
            "options-option-9": NinthAnswer,
            "f154f5e7fac7ead116b8382d45a2fe8d9": "y",
            "poll-submit": "create"
        }
        return body
        

