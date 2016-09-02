#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Here's some info on Jeff"
print "Salary:",enron_data["SKILLING JEFFREY K"]["salary"]
print "Bonus:",enron_data["SKILLING JEFFREY K"]["bonus"]

print len(enron_data),"people in dataset"
print len(enron_data[enron_data.keys()[0]]),"features per person"


num_pois = 0

for p in enron_data.values():
	if p["poi"] == 1:
		num_pois += 1

print num_pois,"persons of interest"


# for (k,v) in enron_data["PRENTICE JAMES"].items():
# 	print k,", ",v
# print "James Prentice's total stock value is",enron_data["PRENTICE JAMES"]["total_stock_value"]

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"],"emails from Wesley Colwell to persons of interest"


max_payments = 0
richest = "no one"

for (k, p) in enron_data.items():
	if (k != "TOTAL" and 
		p["total_payments"] != "NaN" and 
		p["total_payments"] > max_payments):

		max_payments = p["total_payments"]
		richest = k


print richest,"took home the most money, $",max_payments

# for (k, p) in enron_data.items():
# 	print k," took home $",p["total_payments"]


num_salaries = 0
num_emailAddresses = 0
num_totalPayments = 0

for p in enron_data.values():
	if p["salary"] != "NaN":
		num_salaries += 1
	if p["email_address"] != "NaN":
		num_emailAddresses += 1
	if p["total_payments"] != "NaN":
		num_totalPayments += 1

print num_salaries,"people have quantified salaries"
print num_emailAddresses,"people have email addresses"

print len(enron_data) - num_totalPayments,"people do not have total payment information,"
print "which is",(len(enron_data) - num_totalPayments) / float(len(enron_data)) * 100,"percent of people"


num_poiTotalPayments = 0

for p in enron_data.values():
	if p["poi"] == 1 and p["total_payments"] != "NaN":
		num_poiTotalPayments += 1

print num_pois - num_poiTotalPayments,"POIs do not have total payment information,"
print "which is",((num_pois - num_poiTotalPayments) / float(num_pois)) * 100,"percent of POIs"

