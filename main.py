from log_in_info import logInInfo
import pandas as pd

class DoctorReview:

    def __init__(self, review, chatbot):
        self.review = review
        self.chatbot = chatbot
        self.rate_field = ["Competence", "Communication skills", "Professionalism",
                           "Availability and accessibility", "Patient-centered care",
                           "Continuity of care", "Evidence-based practice"]
   
    def DoctorReviewScore(self):
        res = []
        prev_text = ""
        for data in self.chatbot.ask_stream(
            "rate the doctor in %s respectively into a single number-only list based on "
            "below text from 1 to 10 only without any explaination: " %(self.rate_field) + self.review,
            "and return into a single list"
        ):
            # message = data["message"][len(prev_text):]
            # print(message, end="", flush=True) # print the message
            # print(data, end="", flush=True)
            res.append(data)
            # res.append(message)
            # prev_text = data["message"]
        return res
    
    def return_Review_Score_In_Single_List(self):
        res = self.DoctorReviewScore()
        nums = [int(x) for x in res if x.isdigit()]
        print(nums)
        # output validation
        if len(nums) != len(self.rate_field):
            print("Error: the number of scores is not equal to the number of fields")
            return None
        return nums
    
if __name__ == "__main__":
    # API keys
    info = logInInfo("REPLACE W/ YOUR API KEY!")
    chatbot_info = info.connectAPI()

    # single test sample
    # sample1 = "Dr. Smith is a great doctor. He is very knowledgeable and always takes the time to explain things to me. He is very caring and compassionate. I would highly recommend him to anyone."
    # DoctorRev = DoctorReview(sample1, chatbot_info)
    # revResult = DoctorRev.return_Review_Score_In_Single_List()
    # print("==========")
    # print(revResult)

    # change the file path
    df_20 = pd.read_csv("/Users/yiqunhu/Documents/JHU RA 2023 Spring/GPTLabeler/GPTLabeler/comment_20.csv", header=0, usecols=['commentText'])
    print("---------------- Start ----------------")
    # save the results into original data
    df_20['resultsScore'] = df_20['commentText'].apply(lambda x: DoctorReview(x, chatbot_info).return_Review_Score_In_Single_List())
    print(df_20)
    df_20.to_csv('/Users/yiqunhu/Documents/JHU RA 2023 Spring/GPTLabeler/GPTLabeler/comment_20_results_v3.csv', index=False)
    print("---------------- Done ----------------")