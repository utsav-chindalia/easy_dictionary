import string
import nltk
import pandas as pd
#nltk.download()
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tag import pos_tag
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from autocorrect import Speller



text = """window at which people bought tickets to Africa.
And he knew that Egypt was in Africa.
“Can I help you?” asked the man behind the
window.
“Maybe tomorrow," said the boy, moving away.
If he sold just one of his sheep, he'd have enough to
get to the other shore of the strait. The idea fright-
ened him.
“Another dreamer," said the ticket seller to his
assistant, watching the boy walk
away. "He doesn't
have enough money to travel."
While standing at the ticket window, the boy
had remembered his flock, and decided he should
back to being a shepherd. In two years he had
go
learned everything about shepherding: he knew
how to shear sheep, how to care for pregnant ewes,
and how to protect the sheep from wolves. He
knew all the fields and pastures of Andalusia. And
he knew what was the fair price for every one of his
animals.
He decided to return to his friend's stable by the
longest route possible. As he walked past the city's
castle, he interrupted his return, and climbed the
stone ramp that led to the top of the wall. From
there, he could see Africa in the distance. Someone
had once told him that it was from there that the
Moors had come, to occupy all of Spain.
He could see almost the entire city from where he
sat, including the plaza where he had talked with the
all
18
8
to
the
a
27"""

text1 = """AUGUST 15, 2021
U
c
I-Day ruminations:
Could Partition
have been avoided?
say tha
ing li
station at Chauri Chaura. He never consulted M
this decision, and so lost their trust.
In 1927 Jinnah, originally a Congressman, organised
an all-India meeting of Muslim outfits that produced the
‘Delhi Proposals'. Instead of a separate Muslim electorate,
these proposals reserved one-third of Cabinet seats for
C
Muslims; reserved seats for Muslims in Punjab and Ben-
gal in proportion to their population, and proposed new
provinces in Sind, Baluchistan and NWFP. Initially the
Congress accepted these proposals. But Madan Mohan In their 1
Malaviya's Hindu Mahasabha objected strongly, and the
RAW an
Congress caved. A golden opportunity was lost.
SWAMINOMICS
An alternative Motilal Nehru report in 1928 proposed
and Adi
SWAMINATHAN S ANKLESARIA AIYAR
reserved seats for Muslims in proportion to population in
joint electorates, but no reserved seats in the Central govern- the Indi
August 15 remains a day for contemplat- ment or religion-based reservations in Punjab and Bengal,
Himan
ing whether India's 1947 Partition was which would have meant Muslim majorities.
avoidable. Some say the British forced it. Jinnah then proposed a decentralised, federal India with
known
Any student of history will say this is uniform autonomy for all provinces, separate electorates,
laughably false.
RAW
and one-third Muslim representation in both provincial and
The most popular narrative says Jinnah's obduracy com- central Cabinets. These differences with Congress deepened effective
pounded by Congress' lack of spine caused Partition. But thereafter on both sides. Historian K K Aziz says that only this true
historians globally disagree strongly. Read an excellent ac- 15 of 33 proposals for Partition between 1931 and 1940 came Having
count in 'Our Hindu Rashtra' by journalist Aakar Patel. from Muslims — many Hindus wanted it too.
serving
Those who abhor Aakar as an anti-BJP
The Government of India Act, 1935
fanatic can read historians like Ram
created elected provincial governments. ruthle
Guha or Perry Anderson.
The Congress swept the provincial elec- gaged
In local elections starting 1909, the
tions in 1937. After this, says historian ates v
British Raj created separate electorates
Perry Anderson, Nehru saw the political
for Muslims - only Muslims could vote
battle as one between Congress and the the i
in these reserved seats, ensuring them a
British, with the Muslim League and loca
minimum representation. This was dif-
princes as mere fringe actors. Yet Con- ing
ferent from today's reserved seats for
gress membership was 97% Hindu. It
con
Dalits and tribals: all parties field Dalits
could not even find Muslim candidates WOI
and tribals in these seats. In the old Mus-
for 90% of reserved Muslim constituen- bu
lim electorates, Muslims voted almost
cies, which the Muslim League swept.
clc
entirely for the Muslim League, ignoring
In the post-war 1945-46 elections, the ar
supposedly secular Congress.
Muslim League won 446 of 495 provincial pi
Congress castigated separate elec-
Muslim seats, and every central seat. The с
torates as destructive of a national
Congress swept open seats. The results
ethos. Actually, this was realpolitik. In
were, alas, solidly communal.
a first-past-the-post electoral system,
An interim Cabinet was formed with
Muslims with one third of the popula-
Nehru as Prime Minister and Liaquat Ali
tion would win far less than one third POLITICS AT PLAY: It wasn't forced Khan as Finance Minister. Liaquat's budg.
of the seats. Separate electorates re- on India. Ultimately, it was as et imposed hefty taxes on industrialists.
duced Congress dominance.
much Nehru's choice as Jinnah's Most Congressmen called this anti-Hindu
Lala Lajpat Rai, fearless 'Lion of the
since the vast majority of industrialists were
Punjab', viewed power-sharing with Muslims through sepa- Hindu. Yet this was unwarranted communalism: the taxes
rate electorates as impossible, and proposed Partition. Hin- hit Parsis and Christians too, including the mighty Tatas.
dus would control the bulk of the subcontinent, while Mus- As Finance Minister, Liaquat could and did constantly
lims would get (a) the Pathan majority NWFP:(b) the western thwart proposals of Congress ministers entailing govern-
half of a communally divided Punjab; (c) Sind; and (d) the ment expenditure. This infuriated many Congress leaders,
eastern half of a communally divided Bengal. This pro- who said co-habitation with the Muslim League was im-
posal was made in 1924 before the word Pakistan had been possible. Hence Partition, which Congress deemed un-
invented. Yet it conformed exactly to Partition in 1947. thinkable till 1945, was quickly accepted by the Congress
Despite secular claims, the Congress was overwhelm- when Mountbatten proposed this in 1947 in return for
ingly Hindu. Muslims constituted less than 1% of its mem- handing over power within a few months.
bership in 1914, 2% in 1915 and 3% in 1916. Motilal Nehru Had Congress been willing to share power under Jinnah's
baldly called Congress a Hindu body. This changed with earlier proposals, the horrors of Partition could have been
Gandhi's takeover of Congress leadership. He allied with avoided. But would deepening communalism have plunged
Muslims, backing their Khilafat movement. But that alliance an undivided India into civil war? Probably, and so I think
ruptured when he called off his non-cooperation agitation Partition was the best solution. But it was not forced on India.
in 1922 after supposedly non-violent agitators burned a police It was ultimately Nehru's choice no less than Jinnah's.
"""

text2 = '''Reading Compre
Questions 1-3 are based on the following reading passage.
While new census data reveals that unemployment numbers are even direr than was previously suspected,
national newspaper suggests that the contraction in hiring at existing companies might result in more new
companies being founded. College graduates,
unable to find traditional jobs, instead opt to start their own businesses. Where a recession may seem an
unpropitious time for such a historically risky endeavor, with no better options, would-be entrepreneurs have
5 little to lose. Unfortunately
, this situation does not necessarily impact the economy positively. Though the
average number of new businesses started per year has been higher during the recession than it was before, the
proportion of high-value businesses
founded each year has declined. So even if a business manages to stay solvent
, it may not bring significant
returns. Also, because of an inevitable dearth of angel investors and venture capitalists, many new
10 entrepreneurs are putting their own money on the line. In certain ways, the choice between accepting a
traditional job and starting a business is not unlike the choice between renting and buying property. The latter
requires a significant initial outlay and carries
15 heavier risks, but the rewards can be equally substantial.
The primary purpose of the passage is to
(A) propose changes in the way the public generally interprets census data
(B) maintain that college students should form their own companies, especially during economic
recessions
(C) present a nuanced view of a contemporary economic issue
(D) evaluate the viability of low-versus high-value businesses under various environmental conditions
(E) draw an analogy between career decisions and real estate decisions, specifically the choice to rent or
buy property
According to the passage, the reason that many college graduates are choosing to launch their own companies in the
present economic climate is that
(A) they are hampered by the difficulty of finding outside investors
(B) they cannot easily land positions typically open to workers of their experience
(C) the prevalence of low-value companies has increased
(D) they are forced to decide between renting and buying property
(E) forecasts of the unemployment rate are likely to become less dire in coming years
can be inferred from the passage that over the course of the recent recession, the number of American high-value
businesses founded per year
(A) has fallen sharply
(B) has fallen moderately
(C) has risen sharply'''


def strip(speech):
    words = speech.split()                            #tokenize
    table = str.maketrans('','',string.punctuation) #remove punctation
    words = [w.translate(table) for w in words]
    words = [w.lower() for w in words]              #normalize to lower case
    words = [w for w in words if w.isalpha()]       #remove numerics
    return words

def remove_stop_words(speech):
    stop_words = set(stopwords.words('english'))
    stripped = [s for s in speech if s not in stop_words]
    return stripped

def lemmatizer(speech):
    wn = nltk.WordNetLemmatizer()
    w = [wn.lemmatize(word) for word in speech]
    return w

def remove_min_length_words(words):
    w = [word for word in words if len(word) > 3]
    return w

def remove_most_frequest_words(words):
    df = pd.read_csv("./unigram_freq.csv").query('count > 5000000') 
    w = [word for word in words if word not in list(df['word'])]
    return w

def stemm_words(words):
    # ps = PorterStemmer()
    # return [ps.stem(word) for word in words]
    # st = LancasterStemmer()
    # return [st.stem(word) for word in words]
    snowball_stemmer = SnowballStemmer('english')
    return [snowball_stemmer.stem(word) for word in words]
    

def remove_duplicates(words):
    return list(dict.fromkeys(words))

def auto_correct(words):
    spell = Speller(only_replacements=True)
    return [spell(w) for w in words]

def cleanText(text):
    stripped = strip(text)
    stripped_text = remove_stop_words(stripped)
    words = lemmatizer(stripped_text)
    # words = stemm_words(lemmatized_text)
    # words = auto_correct(words)
    words = remove_min_length_words(words)
    words = remove_duplicates(words)
    words = remove_most_frequest_words(words)
    print(words)
    print("----------------------------------------------------")
    print("Original length = ", len(text))
    print("New length = ",len(words))
    return words

if __name__ == "__main__":
    words = cleanText(text1)
# def extract_proper_nouns(speech):
#     tagged_sent = pos_tag(speech.split())
#     pn = [word for word,pos in tagged_sent if pos == 'NNP']
#     pn = [x.lower() for x in pn]
#     prn=list(set(pn))
#     prn= pd.DataFrame({'b_words':prn,'bucket_name':'proper noun'})
#     return prn

# #remove proper noun
# df=proper_nouns(text)
# print(df)



