
#######################
# Straw Poll Bulk Bot #
# @CodeChrisB         #
#######################
# You can change the Questions and Answers underneath
# Keep in mind that the quotation marks --> "" are 
# necessary, and should not be removed.
#If you only want 2 answers leave the others blank --> ""
YourQuestion = "Do you love me?"
FirstAnswer ="Yes"
SecondAnswer ="No"
ThridAnswer ="Maybe"
FourthAnswer ="A bit"
FifthAnswer ="Love? Your my soulmate"
SixthAnswer ="No I'd rather die"
SeventhAnswer = "#Friendzone"
EighthAnswer = "Bro,no"
NinthAnswer = ""
BulkNumber =1000 # How often do you want to send your question?



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
            "poll-submit": "create"
        }
        return body
        

