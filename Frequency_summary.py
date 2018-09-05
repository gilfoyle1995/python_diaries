import nltk as n
import string
import pandas as pd
import arindam_project as x


class FrequencySummarizer(object):
    '''
    FrequencySummarizer creates an object with min_cut and max_cut with
    default settings 0.1 and 0.9
    stopwords is taken from nltk.corpus

    attribute:
        compute_freq
    '''
    def __init__(self , min_cut = 0.1 , max_cut = 0.9):
        self.min_cut = min_cut
        self.max_cut = max_cut
        self.stopwords = set(n.corpus.stopwords.words('english') + list(string.punctuation) + [u" 's",'"'])

    def compute_freq(self , word_sent):
        '''
        input: word_sent 
        assume word_sent is strings

        output: dictionary of frequency of each words other than stopwords 
        & punctuations and spaces

        '''
        freq = {}
        word_sent  = word_sent.split(" ")

        for w in word_sent:
            if w not in self.stopwords:
                if freq.get(w , 0) != 0:
                    freq[w] += 1
                else:
                    freq[w] = 1
        
        m = float(max(freq.values()))
        freq_filter = {}
        for word in freq.keys():
            freq_filter[word] = freq[word] / m
            if freq_filter[word] >= self.max_cut or freq_filter[word] <= self.min_cut:
                del freq_filter[word]
        return freq_filter.copy()
    
    def summarizer(self, article , num):
        '''
        input: article , n(int)
        assume article to be a tuple 

        output: summarized text

        '''
        import nltk as n
        from heapq import nlargest
        text = article
        
        sentences = n.sent_tokenize(text)
        #print(sentences[7])
        word_sent = [n.word_tokenize(s.lower()) for s in sentences]

        self.freq = self.compute_freq(text)
        #print(self.freq)
        ranking = {}

        for i,sentences in enumerate(word_sent):
            for word in sentences:
                #print(word)
                if word in self.freq:
                    if ranking.get(i , 0) == 0:
                        ranking[i] = self.freq[word]
                    else:
                        ranking[i] += self.freq[word]
        
        #df = pd.Series(ranking)
        #df_sorted = df.sort_values(ascending = False)
        #top_elements = df_sorted.head(num)
        
        sentences = n.sent_tokenize(text)
        sentences_index = nlargest(num , ranking , key = ranking.get)
        return [sentences[j] for j in sentences_index]        




f = FrequencySummarizer()
#word = 'First lady Melania Trump underwent a medical procedure to “treat a benign kidney condition” Monday morning at Walter Reed National Military Medical Center and is expected to remain hospitalized for the rest of the week.“The procedure was successful and there were no complications,” Stephanie Grisham, the first lady’s communications director, said in astatement. “Mrs. Trump is at Walter Reed National Military Medical Center and will likely remain there for the duration of the week. The first lady looks forward to a full recovery so she can continue her work on behalf of children everywhere.”Early Tuesday, President Trump noted that the first lady was “doing really well” and could be released from thehospital in as soon as two days.“Our great First Lady is doing really well,” Trump wrotein a tweet. “Will be leaving hospital in 2 or 3 days. Thank you for so much love and support!”The earlier statement from Grisham vaguely described the procedure as “an embolization procedure to treat a benign kidney condition” but offered no additional details aboutthe first lady’s condition or treatment. Grisham declined to provide additional information or answer questions about the procedure, saying that the first lady is entitled to privacy.In embolization, doctors insert a catheter as part of a procedure to purposely block a blood vessel and cut off the blood supply to the affected area. This can be done by sending a coil or a substance down the catheter.The catheter is usually inserted in the femoral artery in the thigh and then threaded through the aorta to the renal artery and then to a smaller blood vessel.The most likely reason for such a procedure is to treat a benign\xa0tumor known as an angiomyolipoma, according to Mohamad E. Allaf, vice chairman of the\xa0urology department at the Johns Hopkins University School of Medicine.Such tumors are usually found by accident, when doctors are taking images for another reason, he said. But if there is bleeding from the vessels, symptoms can include bruising, front and back pain in the kidney area or lightheadedness, he said.Typically, doctors will merely takeperiodic images of a tumor smaller than four centimeters.\xa0But if it is larger, or hasmany\xa0blood vessels feeding it, they might choose the embolization procedure or even surgery, he\xa0said.A less likely reason for the treatment would be the discovery of a vascular abnormality or a weakness in a blood vessel that presents the possibility of rupture, Allaf said. The latter can be caused by previous trauma such as a car accident or a biopsy, he said.Embolization usually is an outpatient procedure or requires just one night in the hospital, he said. “The fact that she’s in the hospital for [the remainder of the]week says to me there’s a little more to the story,” he said.That could mean that doctors are checking for a lung disease associated with angiomyolipomas, he said. Some patientsdo not react well to the embolization itself and doctors may be keeping the first lady there as a precaution, he said.President Trump headed to Walter Reed, in Bethesda, Md., on\xa0Monday afternoon to visit his\xa0wife.“Heading over to Walter Reed Medical Center to see our great First Lady, Melania. Successful\xa0procedure, she is in good spirits. Thankyou to all of the well-wishers!” he wrote in a tweet.The hospitalization comes as Melania Trump, 48, has taken a higher-profile role in the White House in recent weeks. In late April, she hosted her first state dinner in honor of French President Emmanuel Macron andhis wife, Brigitte, and attended the funeral of former first lady Barbara Bush in Houston.Last week, Trump gave a speech in the Rose Garden to announce a new campaign that she’scalling “Be Best.” The first lady has been working to raise awareness of online bullyingand encourage children to be kind to one another, along with highlighting programs that foster the well-being of children. The president sat in the front row as she spoke. BrianMurphy contributed to this report.'
url = input("Enter Any URL from Washington post: ").strip()
article = x.getWashPostText(url , 'p')
word = article[0]
title = article[1]

summary = f.summarizer(word , 2)

summarized_text = ""
for sentence in summary:
    summarized_text += sentence+'/n'
summarized_text = summarized_text[:-1]

print(title)
print("")
print(summarized_text)






    

