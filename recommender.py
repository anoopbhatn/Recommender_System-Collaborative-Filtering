from math import sqrt
from dataset2 import ratings,people

# Returns the Pearson correlation coefficient for p1 and p2
def pearson_correlation(dataset,p1,p2):
	sim={}
	# If p2 has watched a movie that p1 has watched, mark it.
	for item in dataset[p1]:
		if item in dataset[p2]:
			sim[item]=1
	n=len(sim)
	# Return 0, if there are no common ratings
	if n==0: 
		return 0
	
	s1=0
	s2=0
	# Sum of person1
	for item in sim:
		s1+=dataset[p1][item]

	# Sum of person2
	for item in sim:
		s2+=dataset[p2][item]
	
	sqs1=0
	sqs2=0
	# Sum of squares for person1
	for item in sim:
		sqs1+=(dataset[p1][item]*dataset[p1][item])
	# Sum of squares for person2
	for item in sim:
		sqs2+=(dataset[p2][item]*dataset[p2][item])
	
	sum_of_prod=0
	# Sum of products
	for item in sim:
		sum_of_prod+=(dataset[p1][item]*dataset[p2][item])

	num=sum_of_prod-(s1*s2/n)
	den=sqrt((sqs1-pow(s1,2)/n)*(sqs2-pow(s2,2)/n))

	if den==0:
		return 0
	r=num/den

	return r
	
# Method to find the probable rankings that a person can give 
def getRecommendations(dataset,person):
	totals={}
	simSums={}
	# Loop for every person
	for other in dataset:
		# Skip if it is the same person 
		if other==person: 
			continue
		# Find the distance between person and other
		sim=pearson_correlation(dataset,person,other)

		# If distance (similarity) is less than 0, skip the other
		if sim<=0: 
			continue
		# For the movies in the other's ,
		for item in dataset[other]:
			# The movies which are not seen by 'person'
			if item not in dataset[person] or dataset[person][item]==0:
				# Initialize the movie in totals dictionary
				if item not in totals:
					totals[item]=0
				# Add up the product of similarity and ranking of other for every other
				totals[item]+=dataset[other][item]*sim
				if item not in simSums:
					simSums[item]=0
				simSums[item]+=sim
	
	# Predict the rankings of the person
	rankings=[(total/simSums[item],item) for item,total in totals.items( )]
	
	# Sort the rankings in descending order to get the highest rankings that person may give
	rankings.sort( )
	rankings.reverse( )
	return rankings

print '\nEnter a person:'

person_=str(input())

print 'The list of (expected rating,movie_id) of the person',person_,'is :\n'
print getRecommendations(ratings,person_)