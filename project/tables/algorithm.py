from tables.models import Ages, Demographic, Economic, UnitDescription,


def make_queries(querystring):
	


def sort_by_largest_to_smallest(table, field):
	# '-' orders by descending
	return table.objects.order_by('-' + field)[:10]

def sort_by_smallest_to_largest(table, field):
	return table.objects.order_by(field)[:10]

def age_match(age):
	if age == '0_19':
		return sort_by_largest_to_smallest(table=Ages, field='age_0_19')
	elif age == '20_24':
		return sort_by_largest_to_smallest(table=Ages, field='age_20_24')
	elif age == '25_34':
		return sort_by_largest_to_smallest(table=Ages, field='age_25_34')
	elif age == '35_64':
		return sort_by_largest_to_smallest(table=Ages, field='age_35_64')
	elif age == '65_plus':
		return sort_by_largest_to_smallest(table=Ages, field='age_65_over')

# not necessarily a good thing to match on
def gender_match(gender):
	if gender == "male":
		return sort_by_largest_to_smallest(table=Demographic, field='gender_m')
	elif gender == "female":
		return sort_by_largest_to_smallest(table=Demographic, field='gender_f')

def income_match(income):
	if income < 50000:
		return sort_by_largest_to_smallest(table=Economic, field='income_0_50')
	elif 50000 <= income < 100000:
		return sort_by_largest_to_smallest(table=Economic, field='income_50_100')
	elif 100000 <= income < 200000:
		return sort_by_largest_to_smallest(table=Economic, field='income_100_200')
	elif income >= 200000:
		return sort_by_largest_to_smallest(table=Economic, field='income_200_plus')

def children_match(number_of_children):
	if number_of_children == '0':
		pass
	elif number_of_children == '1_plus' or '3_plus':
		# assuming families want bigger units
		rooms_per_unit_over_4 = sort_by_largest_to_smallest(table=UnitDescription, field='rooms_per_unit_over_4')
		# assuming families want neighborhoods with more stability
		length_residence_2000_2009 = sort_by_largest_to_smallest(table=UnitDescription, field='length_residence_2000_2009')
		length_residence_before_2000 = sort_by_largest_to_smallest(table=UnitDescription, field='length_residence_before_2000')

		

def married_match(married):
	if married == "On":
		return sort_by_largest_to_smallest(table=Demographic, field='married')
	elif married == "Off":
		return sort_by_smallest_to_largest(table=Demographic, field='married')


# if querystring and model fields were synched....
def age_match(age):
	return sort_by_largest_to_smallest(table=Ages, field=age)

def gender_match(gender):
	return sort_by_largest_to_smallest(table=Demographic, field=gender)

# ***********************


