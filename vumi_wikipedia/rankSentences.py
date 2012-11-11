from cosine import CosineSimilarity

class SentenceRanker(object):
	def __init__(self):
		a="compare"
	def splitParagraphIntoSentences(self,paragraph):
		import re
    	# to split by multile characters
	
    	#   regular expressions are easiest (and fastest)
		sentenceEnders = re.compile('[.!?]')
		sentenceList = sentenceEnders.split(paragraph)
		return sentenceList


	def rankWikiArticleSentences(self,query,articletext):
		cosineobj1 = CosineSimilarity()
		querydoc = query
		sentences = self.splitParagraphIntoSentences(articletext)
		scoredsentences = dict()
		for s in sentences:
			if s != "":
				scoredsentences[cosineobj1.compare(query,s.strip())] = s.strip()
		it = iter(sorted(scoredsentences.iterkeys(),reverse=True))
		key = it.next()
		finalsentence = scoredsentences[key]
		while finalsentence == "":
			key = it.next()
			finalsentence = scoredsentences[key]

		key = it.next()
		finalsentence += " . "
		finalsentence += scoredsentences[key]
		finalsentence += " . "
		key = it.next()
		finalsentence += scoredsentences[key]
		return finalsentence





if __name__ == '__main__':
	senrank = SentenceRanker()
	print "Ranked sentences"
	print senrank.rankWikiArticleSentences("sachine tennis","Tendulkar was born on 24 April 1973 into a Rajapur Saraswat Brahmin family in Bombay (now Mumbai).[26][27][28] His father Ramesh Tendulkar was a reputed Marathi novelist and his mother Rajni worked in the insurance industry.[29] Ramesh named Tendulkar after his favourite music director, Sachin Dev Burman. Tendulkar has three elder siblings: two half-brothers Nitin and Ajit, and a half-sister Savita. They were Ramesh's children from his first marriage[30]. He spent his formative years in the Sahitya Sahawas Cooperative Housing Society, Bandra (East), Bombay. As a young boy, Tendulkar was considered a bully, and often picked up fights with new children in his school[31]. He also showed an interest in tennis, idolising John McEnroe[32]. To help curb his mischievious and bullying tendencies, Ajit introduced him to cricket in 1984. He introduced the young Sachin to Ramakant Achrekar, a famous cricket coach of Bombay and a club cricketer of repute, at Shivaji Park, Dadar, Bombay.")


	
	
