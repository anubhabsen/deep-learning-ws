from random import randint

feature0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
feature1 = [8, 6, 9, 2, 0, 1, 2, 5, 4, 7]
feature2 = [9, 8, 5, 6, 3, 7, 3, 4, 6, 2]
feature3 = [9, 8, 8, 8, 0, 3, 6, 3, 8, 7]
labels = [5, 8, 2, 5, 6, 8, 1, 0, 9, 1]

theta0 = randint(0, 5)
theta1 = randint(0, 5)
theta2 = randint(0, 5)
theta3 = randint(0, 5)

length_features = len(feature3)

cost = 0

for i in xrange(length_features):
	added_term = theta0 * feature0[i] + theta1 * feature1[i] + theta2 * feature2[i] + theta3 * feature3[i] - labels[i]
	cost += added_term * added_term
	print i, cost

cost = cost / (2 * length_features)

print cost

while 1:
	prevcost = cost
	gradient0 = 0
	gradient1 = 0
	gradient2 = 0
	gradient3 = 0
	for i in xrange(length_features):
		added_term = (theta0 * feature0[i] + theta1 * feature1[i] + theta2 * feature2[i] + theta3 * feature3[i] - labels[i]) * feature0[i]
		gradient0 += added_term
		added_term = (theta0 * feature0[i] + theta1 * feature1[i] + theta2 * feature2[i] + theta3 * feature3[i] - labels[i]) * feature1[i]
		gradient1 += added_term
		added_term = (theta0 * feature0[i] + theta1 * feature1[i] + theta2 * feature2[i] + theta3 * feature3[i] - labels[i]) * feature2[i]
		gradient2 += added_term
		added_term = (theta0 * feature0[i] + theta1 * feature1[i] + theta2 * feature2[i] + theta3 * feature3[i] - labels[i]) * feature3[i]
		gradient3 = added_term

	theta0 = theta0 - 0.01 * gradient0 / length_features
	theta1 = theta1 - 0.01 * gradient1 / length_features
	theta2 = theta2 - 0.01 * gradient2 / length_features
	theta3 = theta3 - 0.01 * gradient3 / length_features

	cost = 0

	for i in xrange(length_features):
		added_term = theta0 * feature0[i] + theta1 * feature1[i] + theta2 * feature2[i] + theta3 * feature3[i] - labels[i]
		cost += added_term * added_term
		# print i, cost

	cost = cost / (2 * length_features)

	# print cost
	if abs(cost - prevcost) <= 0.00000001:
		print
		print
		print
		print
		print '=========================='
		print 'The best thetas are'
		print theta0, theta1, theta2, theta3
		print 'cost is ', cost
		break
