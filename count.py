from collections import Counter

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
paragraph = "Believe it or not, there are still people who are not online! In the US as of 2015, 15% of all adults aged 18+ were not online [Perrin and Duggan, 2015]. A much higher percentage of older adults than younger adults are not online (19–42% vs. 4–7%) [Perrin and Duggan, 2015]. Of all off-liners, 32% cited usability issues: “finding it too difficult or frustrating to go online, or saying that they don’t know how or are physically unable” [Zickuhr, 2013]. Other reasons included high cost, no perceived benefit, and lack of access or availability.But many other people aged 50+ have used digital technology, in some form and to some extent, for decades. They may own computers, tablets, smartphones, e-readers, and fitness trackers. Some of these older adults are casual users (email, shopping, videos), while others have very high levels of technical expertise. Why do some older adults have a hard time with technology?" #Enter your String here

for char in paragraph:
       if char not in punctuations:
            no_punct = no_punct + char

l1 = (no_punct.split())
final = sorted((Counter(l1).most_common(len(Counter(l1)))))

print(final)