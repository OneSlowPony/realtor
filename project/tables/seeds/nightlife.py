"""
File:
1. generates a single nightlife score per neighborhood. for now that's combining yelp and liquor license scores
2. seeds nightlife table in models
"""
from math import log
from tables.models import Neighborhood, Score

# function takes comprehensives nb dictionaries of the form: {'neighborhood': score}
def generate_score(*args):
	average_score = {}
	for arg in args:
		for nb in arg:
			if nb in average_score:
				average_score[nb] += arg[nb]
			else:
				average_score[nb] = arg[nb]
	
	for nb in average_score:
		average_score[nb] = round(average_score[nb]/float(len(args)))
	
	return average_score

def get_scores(my_dict):
	results = {}
	for key in my_dict:
		# log scales down liquor license counts
		score = round(log(my_dict[key]),2)
		results[key] = score
	return results


# n.generate_score(n.yelp_average, logged_liquor)
avg_yelp_plus_liquor = {
	'East New York': 16, 'Middle Village': 16, 'Highbridge': 14, 'Morningside Heights': 14, 
	'Bath Beach': 16, 'East Concourse-Concourse Village': 14, 'Belmont': 14, 
	'Hudson Yards-Chelsea-Flat Iron-Union Square': 21, 'Bedford Park-Fordham North': 16, 
	'Glendale': 16, 'Rossville-Woodrow': 10, 'Marble Hill-Inwood': 14, 'Old Astoria': 11, 
	'Midtown-Midtown South': 22, 'Rosedale': 16, 'Port Richmond': 12, 'Ocean Hill': 17, 
	'Kew Gardens Hills': 14, 'Woodlawn-Wakefield': 12, 'Bedford': 19, 'Borough Park': 19, 
	'Dyker Heights': 16, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 12, 'Kew Gardens': 14, 
	'Breezy Point-Belle Harbor-Rockaway Park-Broad': 15, 'Mount Hope': 21, 'Flushing': 19, 
	'Murray Hill-Kips Bay': 20, 'Washington Heights North': 19, 'Laurelton': 12, 
	'Fort Greene': 16, 'Far Rockaway-Bayswater': 12, 'Spuyten Duyvil-Kingsbridge': 14, 
	'Ft. Totten-Bay Terrace-Clearview': 9, 'West Concourse': 13, 'New Dorp-Midland Beach': 11, 
	'Flatlands': 15, 'Longwood': 12, 'Allerton-Pelham Gardens': 11, 'Richmond Hill': 15, 
	'New Springville-Bloomfield-Travis': 11, 'Arden Heights': 6, 'North Side-South Side': 7, 
	'Ocean Parkway South': 19, 'South Jamaica': 15, 'Soundview-Bruckner': 12, 'Clinton Hill': 17, 
	'Canarsie': 13, 'Whitestone': 16, 'North Riverdale-Fieldston-Riverdale': 12, 
	'Stapleton-Rosebank': 12, 'Eastchester-Edenwald-Baychester': 10, 'Murray Hill': 20, 
	'Jamaica Estates-Holliswood': 14, 'Charleston-Richmond Valley-Tottenville': 10, 'Forest Hills': 19, 
	'Cypress Hills-City Line': 16, 'East Tremont': 16, 'Prospect Lefferts Gardens-Wingate': 18, 
	'Starrett City': 9, 'Maspeth': 17, 'Gravesend': 17, 'Bronxdale': 16, 'Crotona Park East': 16, 
	'Ridgewood': 18, 'Oakwood-Oakwood Beach': 13, 'East Harlem North': 15, 'Great Kills': 13, 
	'Stuyvesant Heights': 15, 'Norwood': 15, 'Greenpoint': 21, 'East Williamsburg': 20, 
	'Glen Oaks-Floral Park-New Hyde Park': 13, 'Schuylerville-Throgs Neck-Edgewater Park': 12, 
	'Astoria': 19, 'Auburndale': 16, 'Gramercy': 16, 'West Farms-Bronx River': 13, 'Woodhaven': 13, 
	'Parkchester': 13, 'Fordham South': 17, 'Melrose South-Mott Haven North': 16, 'Williamsburg': 18, 
	'East Flatbush-Farragut': 13, 'Madison': 16, 'East Flushing': 16, 'Elmhurst': 18, 
	'Grymes Hill-Clifton-Fox Hills': 13, 'Central Harlem North-Polo Grounds': 14, 'Sunset Park East': 17, 
	'Bellerose': 15, 'Co-Op City': 13, 'Upper East Side-Carnegie Hill': 19, 
	'Queensbridge-Ravenswood-Long Island City': 20, 'Morrisania-Melrose': 13, 
	'West New Brighton-New Brighton-St. George': 14, "Mariner's Harbor-Arlington-Port Ivory-Granite": 16, 
	'Corona': 15, 'Queens Village': 14, 'Westerleigh': 14, 'Van Nest-Morris Park-Westchester Square': 11, 
	'West Brighton': 14, 'Carroll Gardens-Columbia Street-Red Hook': 17, 'St. Albans': 14, 
	'Hammels-Arverne-Edgemere': 10, 'Pelham Parkway': 10, 'Rego Park': 16, 'Hamilton Heights': 20, 
	'New Brighton-Silver Lake': 11, "Annadale-Huguenot-Prince's Bay-Eltingville": 10, 'Steinway': 18, 
	'East Harlem South': 21, 'Turtle Bay-East Midtown': 21, 
	'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 14, 'Brownsville': 16, 'Flatbush': 18, 
	'Todt Hill-Emerson Hill-Heartland Village-Ligh': 14, 'Lower East Side': 20, 'Fresh Meadows-Utopia': 15, 
	'Crown Heights North': 18, 'Van Cortlandt Village': 13, 'Upper West Side': 20, 
	'Pelham Bay-Country Club-City Island': 10, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 18, 
	'Yorkville': 21, 'Lincoln Square': 20, 'College Point': 15, 'Bensonhurst East': 17, 
	'Seagate-Coney Island': 15, 'Westchester-Unionport': 14, 'Brooklyn Heights-Cobble Hill': 17, 
	'Elmhurst-Maspeth': 18, 'Rikers Island': 17, 'Bayside-Bayside Hills': 14, 'North Corona': 16, 
	'Queensboro Hill': 20, 'Chinatown': 19, 'Central Harlem South': 20, 
	'Washington Heights South': 18, 'Mott Haven-Port Morris': 18, 'Bensonhurst West': 17, 
	'Bushwick North': 19, 'Bushwick South': 19, 'Brighton Beach': 16, 'Baisley Park': 14, 
	'East New York (Pennsylvania Ave)': 14, 'Old Town-Dongan Hills-South Beach': 12, 
	'Battery Park City-Lower Manhattan': 21, 'Jackson Heights': 18, 
	'Douglas Manor-Douglaston-Little Neck': 12, 'Sunset Park West': 17, 'Kingsbridge Heights': 14, 
	'Pomonok-Flushing Heights-Hillcrest': 16, 'Grasmere-Arrochar-Ft. Wadsworth': 12, 'Hollis': 11, 
	'Briarwood-Jamaica Hills': 18, 'Soundview-Castle Hill-Clason Point-Harding Pa': 15, 
	'Prospect Heights': 19, 'East Elmhurst': 17, 'South Ozone Park': 14, 'Hunts Point': 10, 
	'Stuyvesant Town-Cooper Village': 21, 'Springfield Gardens North': 10, 
	'University Heights-Morris Heights': 16, 'East Village': 20, 'Cambria Heights': 12, 
	'Springfield Gardens South-Brookville': 10, 'Midwood': 16, 'Lindenwood-Howard Beach': 13, 
	'Rugby-Remsen Village': 17, 'Kensington-Ocean Parkway': 15, 'Lenox Hill-Roosevelt Island': 19, 
	'Hunters Point-Sunnyside-West Maspeth': 16, 'Crown Heights South': 18, 'Claremont-Bathgate': 13, 
	'Manhattanville': 18, 'Clinton': 4, 'Williamsbridge-Olinville': 16, 'Oakland Gardens': 14, 
	"Clinton": 21, 'Erasmus': 16, 'Jamaica': 15, 'West Village': 20, 'Ozone Park': 15, 
	'SoHo-TriBeCa-Civic Center-Little Italy': 20, 'Homecrest': 15, 'Windsor Terrace': 16, 
	'Bay Ridge': 17, 'Woodside': 22, 'Park Slope-Gowanus': 20,
}

# n.get_scores(n.nb_count_dict)
logged_liquor = {
'East New York': 5.21,'Bath Beach': 5.02,
'Highbridge': 4.95,
'Morningside Heights': 4.76,
'Middle Village': 3.87,
'East Concourse-Concourse Village': 4.61,
'Belmont bronx': 5.12,
'Hudson Yards-Chelsea-Flat Iron-Union Square': 6.59,
'Bedford Park-Fordham North': 5.12,
'Glendale': 5.63,
'Jamaica Estates-Holliswood': 3.4,
'South Ozone Park': 3.14,'Great Kills': 3.95,'Midtown-Midtown South': 6.17,
'Rosedale': 3.3,
'Port Richmond': 4.14,
'Hunts Point': 3.56,
'Kew Gardens Hills': 3.43,'Woodlawn-Wakefield': 4.2,
'Bedford brooklyn': 4.84,
'Borough Park': 4.61,'Dyker Heights': 4.2,
'Georgetown-Marine Park-Bergen Beach-Mill Basi': 4.82,
'Bayside-Bayside Hills': 4.62,
'Breezy Point-Belle Harbor-Rockaway Park-Broad': 2.4,
'Mount Hope': 6.29,
'Flushing': 5.44,
'Murray Hill-Kips Bay': 5.86,
'Washington Heights North': 5.69,
'Laurelton': 3.5,
'Rossville-Woodrow': 4.13,
'West New Brighton-New Brighton-St. George': 3.97,
'Far Rockaway-Bayswater': 3.87,
'East Elmhurst': 3.81,
'Spuyten Duyvil-Kingsbridge': 4.62,
'Ft. Totten-Bay Terrace-Clearview': 2.77,
'West Concourse': 4.61,
'New Dorp-Midland Beach': 4.41,
'Flatlands': 4.82,
'Longwood': 4.5,
'Starrett City': 2.56,
'Richmond Hill': 4.52,
'New Springville-Bloomfield-Travis': 4.84,
'Cypress Hills-City Line': 5.12,
'Ocean Parkway South': 4.38,
'South Jamaica': 3.71,
'Soundview-Bruckner': 4.8,
'Queens Village': 3.37,
'Canarsie': 4.47,
'Whitestone': 4.09,
'Schuylerville-Throgs Neck-Edgewater Park': 4.26,
'Stapleton-Rosebank': 4.52,
'Eastchester-Edenwald-Baychester': 3.58,
'North Riverdale-Fieldston-Riverdale': 3.47,'St. Albans': 3.76,
'Queensboro Hill queens': 4.82,
'Charleston-Richmond Valley-Tottenville': 3.37,
'Forest Hills': 5.02,'East Tremont': 4.88,'Prospect Lefferts Gardens-Wingate': 4.56,'Allerton-Pelham Gardens': 4.19,
'Maspeth': 4.43,'Gravesend': 5.1,
'Bronxdale': 4.78,'Crotona Park East': 4.48,
'Ridgewood': 5.63,'Oakwood-Oakwood Beach': 4.41,'East Harlem North': 3.09,
'Old Astoria': 4.43,'Stuyvesant Heights nyc': 4.53,
'Norwood': 4.91,
'Greenpoint': 5.44,
'East Williamsburg': 6.17,
'Glen Oaks-Floral Park-New Hyde Park': 4.61,'West Village': 6.57,
'Astoria': 5.17,'Auburndale': 4.86,'Gramercy': 6.29,
'West Farms-Bronx River': 4.48,
'Woodhaven': 4.25,
'Parkchester': 4.78,
'Fordham South': 5.12,
'Melrose South-Mott Haven North': 4.61,
'Williamsburg': 6.17,
'East Flatbush-Farragut': 4.74,
'Madison brookl': 4.74,
'Midwood': 4.38,
'Elmhurst': 5.05,
'Grymes Hill-Clifton-Fox Hills': 4.51,
'Central Harlem North-Polo Grounds': 3.18,
'Sunset Park East': 5.41,
'Bellerose': 3.09,
'Co-Op City': 3.58,
'Upper East Side-Carnegie Hill': 6.43,
'Queensbridge-Ravenswood-Long Island City': 5.98,
'Morrisania-Melrose': 4.78,
'Fort Greene': 4.88,
 "Mariner's Harbor-Arlington-Port Ivory-Granite": 3.66,
'Corona': 5.66,
'Clinton Hill': 4.88,
'Westerleigh': 4.84,'Van Nest-Morris Park-Westchester Square': 4.78,'West Brighton': 3.97,'Carroll Gardens-Columbia Street-Red Hook': 5.18,
'Hammels-Arverne-Edgemere': 2.08,
'Rego Park': 4.39,'Hamilton Heights': 4.61,
'New Brighton-Silver Lake': 4.51,
 "Annadale-Huguenot-Prince's Bay-Eltingville": 4.19,
'East Harlem South': 5.04,'Turtle Bay-East Midtown': 5.8,
'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 5.19,'Sunset Park West': 5.41,
'Flatbush': 5.03,'Todt Hill-Emerson Hill-Heartland Village-Ligh': 4.17,
'Lower East Side': 5.9,
'Fresh Meadows-Utopia': 3.53,
'Crown Heights North': 4.56,
'Van Cortlandt Village': 4.61,
'Upper West Side': 5.94,
'Pelham Bay-Country Club-City Island': 3.56,
'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 6.11,
'Yorkville nyc': 5.06,
'Lincoln Square': 5.03,
'College Point': 3.95,
'Bensonhurst East': 4.65,
'Seagate-Coney Island': 4.39,
'Westchester-Unionport': 4.88,
'Brooklyn Heights-Cobble Hill': 5.55,
'Elmhurst-Maspeth': 5.05,
'Kew Gardens': 3.43,
'North Corona': 5.66,
'Pomonok-Flushing Heights-Hillcrest': 6.01,
'Central Harlem South': 4.16,
'Washington Heights South': 4.7,
'Mott Haven-Port Morris': 4.5,
'Bensonhurst West': 5.02,
'Bushwick North': 5.35,
'Brighton Beach': 5.19,
'Baisley Park': 4.23,
'Chinatown': 5.81,
'Old Town-Dongan Hills-South Beach': 4.52,
'Battery Park City-Lower Manhattan': 5.53,
'Jackson Heights': 5.53,
'Douglas Manor-Douglaston-Little Neck': 3.47,
'Brownsville': 4.78,
'Kingsbridge Heights': 4.62,
'Soundview-Castle Hill-Clason Point-Harding Pa': 4.8,
'Grasmere-Arrochar-Ft. Wadsworth': 4.17,
'Hollis': 3.4,
'Briarwood-Jamaica Hills': 4.78,
'Prospect Heights': 5.41,
'Steinway': 4.84,
'Marble Hill-Inwood': 4.64,
'Ocean Hill': 4.53,
'Murray Hill': 5.86,
'Stuyvesant Town-Cooper Village': 6.21,
'Springfield Gardens North': 3.5,
'University Heights-Morris Heights': 4.84,
'East Village': 5.71,
'Cambria Heights': 2.89,
'Springfield Gardens South-Brookville': 3.5,
'East Flushing': 5.44,
'Lindenwood-Howard Beach': 3.69,
'Rugby-Remsen Village': 4.74,
'Kensington-Ocean Parkway': 4.83,
'Lenox Hill-Roosevelt Island': 4.38,
'Hunters Point-Sunnyside-West Maspeth': 4.53,
'Crown Heights South': 4.56,
'East New York (Pennsylvania Ave)': 5.21,
'Claremont-Bathgate': 4.88,
'Manhattanville': 4.76,
'Windsor Terrace': 5.73,
'Williamsbridge-Olinville': 5.27,
'Oakland Gardens': 3.56,
 "hell's kitchen": 6.17,
'Erasmus': 5.03,
'Jamaica': 4.57,
'Bushwick South': 5.35,
'Ozone Park': 4.06,
'SoHo-TriBeCa-Civic Center-Little Italy': 6.03,
'Homecrest': 5.1,
'Clinton': 7.03,
'Bay Ridge': 5.35,
'Woodside': 5.3
}


# from yelp_responses.py,
# results were generated with single zip code per nb,
# before we had lists
bar_scores = {'Borough Park': 28.56,'Fresh Meadows-Utopia': 20.84,'Soundview-Bruckner': 11.9, 'Co-Op City': 17.75, 'Gramercy': 21.2, 'Hollis': 11.4, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 12.53, 'Yorkville nyc': 33.03, 'Battery Park City-Lower Manhattan': 32.23, 'Greenpoint': 34.79, 'East Village': 32.67, 'North Riverdale-Fieldston-Riverdale': 12.91, 'St. Albans': 15.05, 'Whitestone': 22.23, 'Laurelton': 15.77, 'Hunters Point-Sunnyside-West Maspeth': 21.62, 'East Flatbush-Farragut': 14.99, 'West Brighton': 18.42, 'Brownsville': 24.92, 'Fordham South': 21.92, "Mariner's Harbor-Arlington-Port Ivory-Granite": 23.15, 'Woodhaven': 16.41, 'Hamilton Heights': 33.04, 'Brighton Beach': 19.0, 'East Tremont': 21.75, 'Bensonhurst West': 22.87, 'Allerton-Pelham Gardens': 9.42, 'Queensboro Hill queens': 32.46, 'Auburndale': 22.17, 'Corona': 17.96, 'Murray Hill': 31.35, 'Astoria': 29.06, 'Forest Hills': 28.29, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 20.29, 'Ocean Hill': 25.9, 'Mount Hope': 32.6, 'Murray Hill-Kips Bay': 33.13, 'South Jamaica': 17.06, 'Bensonhurst East': 23.76, 'New Springville-Bloomfield-Travis': 11.99, 'Maspeth': 27.9, 'Springfield Gardens North': 11.32, 'Central Harlem South': 30.84, 'Pelham Bay-Country Club-City Island': 11.39, 'Washington Heights South': 26.23, 'Ft. Totten-Bay Terrace-Clearview': 9.24, 'Turtle Bay-East Midtown': 34.77, 'Belmont bronx': 14.32, 'Morrisania-Melrose': 14.92, 'Port Richmond': 12.52, 'Cypress Hills-City Line': 21.66, 'Windsor Terrace': 22.3, 'Kew Gardens': 18.31, 'Rosedale': 21.43, 'Douglas Manor-Douglaston-Little Neck': 12.58, 'East Elmhurst': 24.77, 'Grasmere-Arrochar-Ft. Wadsworth': 11.08, 'Kingsbridge Heights': 19.29, 'Claremont-Bathgate': 12.72, 'Upper West Side': 31.29, 'Bedford brooklyn': 30.34, 'Bellerose': 19.4, 'North Side-South Side': 9.79, 'Bushwick South': 29.59, 'Queens Village': 17.04, 'Fort Greene': 23.18, 'Middle Village': 24.28, 'Pomonok-Flushing Heights-Hillcrest': 20.6, 'Gravesend': 21.38, 'Van Nest-Morris Park-Westchester Square': 11.16, 'Kew Gardens Hills': 18.31, 'Richmond Hill': 21.11, 'Upper East Side-Carnegie Hill': 27.28, 'Rossville-Woodrow': 9.76, 'Morningside Heights': 20.67, 'Woodside': 33.34, 'Great Kills': 14.86, 'Canarsie': 15.33, 'Madison brookl': 21.37, 'East Harlem South': 32.18, 'Dyker Heights': 22.62, 'Cambria Heights': 14.85, 'Flatlands': 19.96, 'College Point': 21.58, 'Hammels-Arverne-Edgemere': 10.68, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 14.82, 'East New York (Pennsylvania Ave)': 17.32, 'Prospect Heights': 28.68, 'Parkchester': 12.94, 'Midwood': 20.68, 'Washington Heights North': 26.23, 'Lower East Side': 31.89, 'West Village': 31.66, 'Elmhurst': 22.53, 'Stuyvesant Town-Cooper Village': 32.39, 'Rego Park': 23.57, 'Norwood': 21.79, 'Queensbridge-Ravenswood-Long Island City': 30.55, 'Highbridge': 17.22, "Annadale-Huguenot-Prince's Bay-Eltingville": 8.3, 'Clinton Hill': 24.87, 'SoHo-TriBeCa-Civic Center-Little Italy': 30.55, 'Soundview-Castle Hill-Clason Point-Harding Pa': 18.11, 'Crotona Park East': 19.35, 'Grymes Hill-Clifton-Fox Hills': 14.85, 'Schuylerville-Throgs Neck-Edgewater Park': 11.4, 'Manhattanville': 26.02, "hell's kitchen": 33.71, 'Glen Oaks-Floral Park-New Hyde Park': 14.29, 'Erasmus': 19.58, 'Prospect Lefferts Gardens-Wingate': 27.97, 'Baisley Park': 17.99, 'Kensington-Ocean Parkway': 18.6, 'Longwood': 11.01, 'Bedford Park-Fordham North': 21.67, 'Central Harlem North-Polo Grounds': 19.15, 'Old Astoria': 16.23, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 32.23, 'Lenox Hill-Roosevelt Island': 28.52, 'North Corona': 18.22, 'East Williamsburg': 32.07, 'Flushing': 27.54, 'East Concourse-Concourse Village': 17.69, 'Bayside-Bayside Hills': 15.4, 'Starrett City': 7.92, 'Steinway': 28.21, 'East Harlem North': 20.52, 'Sunset Park East': 23.04, 'Flatbush': 26.74, 'University Heights-Morris Heights': 22.19, 'Spuyten Duyvil-Kingsbridge': 18.91, 'Lindenwood-Howard Beach': 19.94, 'Bath Beach': 21.46, 'Glendale': 23.98, 'Williamsburg': 27.22, 'Stuyvesant Heights nyc': 20.76, 'West New Brighton-New Brighton-St. George': 19.29, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 16.85, 'Stapleton-Rosebank': 12.13, 'New Brighton-Silver Lake': 17.45, 'Chinatown': 28.15, 'Rugby-Remsen Village': 24.73, 'Arden Heights': 7.97, 'Charleston-Richmond Valley-Tottenville': 10.63, 'Seagate-Coney Island': 19.0, 'South Ozone Park': 19.14, 'Woodlawn-Wakefield': 11.63, 'Briarwood-Jamaica Hills': 27.14, 'Carroll Gardens-Columbia Street-Red Hook': 24.51, 'East Flushing': 20.26, 'Mott Haven-Port Morris': 26.62, 'Ozone Park': 20.4, 'Sunset Park West': 23.04, 'Pelham Parkway': 16.2, 'Jackson Heights': 25.31, 'Crown Heights South': 27.97, 'Old Town-Dongan Hills-South Beach': 12.13, 'Eastchester-Edenwald-Baychester': 9.01, 'Homecrest': 16.44, 'Oakwood-Oakwood Beach': 13.0, 'Melrose South-Mott Haven North': 22.46, 'Ocean Parkway South': 29.9, 'Lincoln Square': 30.22, 'Jamaica': 17.76, 'Williamsbridge-Olinville': 20.78, 'New Dorp-Midland Beach': 10.58, 'Bushwick North': 29.59, 'Bay Ridge': 20.82, 'Far Rockaway-Bayswater': 15.03, 'Westchester-Unionport': 15.95, 'Midtown-Midtown South': 33.86, 'Marble Hill-Inwood': 17.23, 'West Farms-Bronx River': 12.99, 'Hunts Point': 6.84, 'Crown Heights North': 27.97, 'West Concourse': 16.58, 'Brooklyn Heights-Cobble Hill': 24.19, 'East New York': 22.74, 'Oakland Gardens': 19.58, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 25.23, 'Bronxdale': 20.04, 'Jamaica Estates-Holliswood': 15.75, 'Westerleigh': 16.57, 'Springfield Gardens South-Brookville': 10.85, 'Ridgewood': 25.42, 'Elmhurst-Maspeth': 23.99, 'Van Cortlandt Village': 16.57}
restaurant_scores = {'Borough Park': 35.89, 'Fresh Meadows-Utopia': 29.05, 'Soundview-Bruckner': 21.62, 'Co-Op City': 26.48, 'Gramercy': 25.63, 'Hollis': 18.09, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 21.09, 'Yorkville nyc': 38.41, 'Battery Park City-Lower Manhattan': 37.45, 'Greenpoint': 38.81, 'East Village': 36.33, 'North Riverdale-Fieldston-Riverdale': 19.64, 'St. Albans': 26.71, 'Whitestone': 26.64, 'Laurelton': 23.17, 'Hunters Point-Sunnyside-West Maspeth': 28.9, 'East Flatbush-Farragut': 24.08, 'West Brighton': 26.01, 'Brownsville': 30.39, 'Fordham South': 31.01, "Mariner's Harbor-Arlington-Port Ivory-Granite": 30.27, 'Woodhaven': 22.56, 'Hamilton Heights': 40.05, 'Brighton Beach': 28.2, 'East Tremont': 31.6, 'Bensonhurst West': 31.13, 'Allerton-Pelham Gardens': 15.4, 'Queensboro Hill queens': 38.67, 'Auburndale': 29.75, 'Corona': 26.67, 'Murray Hill': 35.61, 'Astoria': 35.38, 'Forest Hills': 37.03, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 29.56, 'Ocean Hill': 33.99, 'Mount Hope': 36.54, 'Murray Hill-Kips Bay': 36.31, 'South Jamaica': 28.4, 'Bensonhurst East': 31.08, 'New Springville-Bloomfield-Travis': 16.82, 'Maspeth': 31.01, 'Springfield Gardens North': 18.14, 'Central Harlem South': 37.35, 'Pelham Bay-Country Club-City Island': 12.99, 'Washington Heights South': 35.96, 'Ft. Totten-Bay Terrace-Clearview': 13.35, 'Turtle Bay-East Midtown': 39.98, 'Belmont bronx': 27.0, 'Morrisania-Melrose': 24.43, 'Port Richmond': 21.95, 'Cypress Hills-City Line': 28.47, 'Windsor Terrace': 25.99, 'Kew Gardens': 25.05, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 23.79, 'Rosedale': 30.47, 'Rikers Island': 47.78, 'Douglas Manor-Douglaston-Little Neck': 20.27, 'East Elmhurst': 31.99, 'Grasmere-Arrochar-Ft. Wadsworth': 17.56, 'Kingsbridge Heights': 23.91, 'Claremont-Bathgate': 24.82, 'Upper West Side': 35.86, 'Bedford brooklyn': 35.77, 'Bellerose': 26.56, 'North Side-South Side': 17.66, 'Bushwick South': 35.46, 'Queens Village': 25.71, 'Fort Greene': 29.81, 'Middle Village': 32.11, 'Pomonok-Flushing Heights-Hillcrest': 27.08, 'Gravesend': 30.82, 'Van Nest-Morris Park-Westchester Square': 18.69, 'Kew Gardens Hills': 25.05, 'Richmond Hill': 27.61, 'Upper East Side-Carnegie Hill': 32.44, 'Rossville-Woodrow': 14.93, 'Morningside Heights': 26.91, 'Woodside': 41.93, 'Great Kills': 21.5, 'Madison brookl': 29.55, 'East Harlem South': 39.14, 'Dyker Heights': 31.13, 'Cambria Heights': 21.44, 'Flatlands': 27.8, 'College Point': 28.5, 'Hammels-Arverne-Edgemere': 10.62, 'Canarsie': 25.0, 'East New York (Pennsylvania Ave)': 24.5, 'Prospect Heights': 34.27, 'Parkchester': 23.45, 'Midwood': 31.0, 'Washington Heights North': 35.96, 'Lower East Side': 35.79, 'West Village': 34.75, 'Westchester-Unionport': 23.94, 'Stuyvesant Town-Cooper Village': 36.69, 'Rego Park': 31.41, 'Norwood': 27.54, 'Queensbridge-Ravenswood-Long Island City': 37.03, 'Highbridge': 28.47, "Annadale-Huguenot-Prince's Bay-Eltingville": 13.18, 'Clinton Hill': 30.52, 'SoHo-TriBeCa-Civic Center-Little Italy': 34.77, 'Soundview-Castle Hill-Clason Point-Harding Pa': 28.29, 'Crotona Park East': 31.14, 'Grymes Hill-Clifton-Fox Hills': 21.76, 'Schuylerville-Throgs Neck-Edgewater Park': 18.46, 'Manhattanville': 33.29, "hell's kitchen": 38.18, 'Glen Oaks-Floral Park-New Hyde Park': 19.92, 'Erasmus': 27.57, 'Prospect Lefferts Gardens-Wingate': 34.5, 'Baisley Park': 25.98, 'Kensington-Ocean Parkway': 26.1, 'Longwood': 22.95, 'Bedford Park-Fordham North': 29.31, 'Central Harlem North-Polo Grounds': 27.83, 'Old Astoria': 19.39, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 36.14, 'Lenox Hill-Roosevelt Island': 34.47, 'North Corona': 28.04, 'East Williamsburg': 37.07, 'Flushing': 35.85, 'East Concourse-Concourse Village': 26.02, 'Bayside-Bayside Hills': 22.01, 'Starrett City': 14.84, 'Steinway': 33.62, 'East Harlem North': 27.7, 'Sunset Park East': 31.46, 'Flatbush': 33.33, 'University Heights-Morris Heights': 30.94, 'Spuyten Duyvil-Kingsbridge': 23.91, 'Lindenwood-Howard Beach': 25.53, 'Bath Beach': 28.46, 'Glendale': 28.36, 'Williamsburg': 31.77, 'Stuyvesant Heights nyc': 28.12, 'West New Brighton-New Brighton-St. George': 26.13, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 24.82, 'Stapleton-Rosebank': 19.27, 'New Brighton-Silver Lake': 11.12, 'Chinatown': 33.58, 'Rugby-Remsen Village': 31.81, 'Arden Heights': 16.46, 'Charleston-Richmond Valley-Tottenville': 16.04, 'Seagate-Coney Island': 28.2, 'South Ozone Park': 27.61, 'Woodlawn-Wakefield': 22.21, 'Briarwood-Jamaica Hills': 36.35, 'Carroll Gardens-Columbia Street-Red Hook': 29.1, 'East Flushing': 27.08, 'Mott Haven-Port Morris': 33.4, 'Ozone Park': 26.96, 'Sunset Park West': 31.46, 'Pelham Parkway': 24.0, 'Jackson Heights': 33.34, 'Crown Heights South': 34.5, 'Old Town-Dongan Hills-South Beach': 19.27, 'Eastchester-Edenwald-Baychester': 18.0, 'Homecrest': 25.99, 'Oakwood-Oakwood Beach': 20.78, 'Melrose South-Mott Haven North': 32.22, 'Ocean Parkway South': 36.54, 'Lincoln Square': 35.18, 'Jamaica': 28.29, 'Williamsbridge-Olinville': 29.3, 'New Dorp-Midland Beach': 18.44, 'Bushwick North': 35.46, 'Bay Ridge': 29.89, 'Far Rockaway-Bayswater': 21.42, 'Elmhurst': 33.53, 'Midtown-Midtown South': 39.78, 'Marble Hill-Inwood': 25.3, 'West Farms-Bronx River': 25.57, 'Hunts Point': 19.86, 'Crown Heights North': 34.5, 'West Concourse': 23.72, 'Brooklyn Heights-Cobble Hill': 29.99, 'East New York': 27.03, 'Oakland Gardens': 24.39, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 30.79, 'Bronxdale': 29.66, 'Jamaica Estates-Holliswood': 27.18, 'Westerleigh': 24.9, 'Springfield Gardens South-Brookville': 15.72, 'Ridgewood': 32.89, 'Elmhurst-Maspeth': 33.72, 'Van Cortlandt Village': 23.81}
atmosphere_restaurant_scores = {'Queensbridge-Ravenswood-Long Island City': 40.88, 'Bedford brooklyn': 40.98, 'East Harlem South': 42.62, 'Soundview-Castle Hill-Clason Point-Harding Pa': 37.75, 'Corona': 38.36, 'Jamaica Estates-Holliswood': 39.19, 'Upper East Side-Carnegie Hill': 41.12, 'Central Harlem South': 41.4, 'Marble Hill-Inwood': 35.09, 'Midtown-Midtown South': 41.84, 'Schuylerville-Throgs Neck-Edgewater Park': 36.53, 'Grasmere-Arrochar-Ft. Wadsworth': 35.67, 'Middle Village': 36.65, 'Westchester-Unionport': 38.96, 'Baisley Park': 36.93, 'Washington Heights South': 40.21, 'Chinatown': 37.68, 'Port Richmond': 36.51, 'Hunts Point': 36.05, 'West Farms-Bronx River': 38.01, 'Stuyvesant Heights nyc': 39.04, 'Eastchester-Edenwald-Baychester': 32.88, 'Van Nest-Morris Park-Westchester Square': 35.81, 'Manhattanville': 39.7, 'Bayside-Bayside Hills': 39.2, 'Woodlawn-Wakefield': 36.5, 'Ft. Totten-Bay Terrace-Clearview': 36.46, 'Old Town-Dongan Hills-South Beach': 35.36, 'Stapleton-Rosebank': 35.36, 'New Brighton-Silver Lake': 37.28, 'Erasmus': 41.68, 'West Village': 40.63, 'Parkchester': 37.25, 'Borough Park': 37.55, 'Oakland Gardens': 35.45, 'Westerleigh': 35.76, 'Bushwick North': 40.54, 'Sunset Park West': 38.05, 'Homecrest': 36.74, 'Washington Heights North': 40.21, 'Elmhurst': 38.87, 'Glendale': 35.64, 'Steinway': 41.14, 'Sunset Park East': 38.05, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 37.34, 'Rossville-Woodrow': 34.28, 'Mount Hope': 41.59, 'Turtle Bay-East Midtown': 41.35, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 37.5, 'South Jamaica': 39.94, 'Glen Oaks-Floral Park-New Hyde Park': 37.44, 'Richmond Hill': 36.58, 'Astoria': 42.11, 'Norwood': 39.22, 'St. Albans': 37.93, 'Morrisania-Melrose': 36.08, 'East Harlem North': 39.47, 'Ridgewood': 40.3, 'Midwood': 37.74, 'Pelham Bay-Country Club-City Island': 35.22, 'College Point': 38.66, 'Crotona Park East': 38.99, 'Flushing': 41.2, 'Spuyten Duyvil-Kingsbridge': 36.8, 'Whitestone': 37.92, 'Williamsbridge-Olinville': 39.7, 'North Corona': 38.63, 'Central Harlem North-Polo Grounds': 39.47, 'Allerton-Pelham Gardens': 34.85, 'Hunters Point-Sunnyside-West Maspeth': 40.13, 'Dyker Heights': 38.35, 'East Village': 42.55, 'Van Cortlandt Village': 37.52, 'Canarsie': 33.42, 'Clinton Hill': 38.82, 'New Dorp-Midland Beach': 32.62, 'West New Brighton-New Brighton-St. George': 36.87, 'Claremont-Bathgate': 38.27, 'Rikers Island': 40.85, 'East Flushing': 37.67, 'Bedford Park-Fordham North': 39.96, 'Far Rockaway-Bayswater': 34.9, 'Highbridge': 37.78, 'Fort Greene': 38.1, 'Old Astoria': 16.88, 'Woodside': 39.14, 'Fresh Meadows-Utopia': 38.7, 'Murray Hill': 39.16, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 39.57, 'Woodhaven': 38.03, 'Ocean Hill': 41.46, 'Bensonhurst West': 36.79, 'Crown Heights North': 40.72, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 38.15, 'East Flatbush-Farragut': 38.04, 'East Williamsburg': 40.56, 'Cambria Heights': 36.69, 'South Ozone Park': 36.69, 'Gramercy': 39.65, 'Crown Heights South': 40.72, 'Jamaica': 39.94, 'Maspeth': 34.51, 'Lincoln Square': 39.43, 'Upper West Side': 39.19, 'Great Kills': 36.82, 'Springfield Gardens North': 33.93, 'Lenox Hill-Roosevelt Island': 40.63, 'Brooklyn Heights-Cobble Hill': 38.62, 'Kensington-Ocean Parkway': 38.52, 'Springfield Gardens South-Brookville': 31.93, 'Murray Hill-Kips Bay': 40.37, 'Starrett City': 31.95, 'East Elmhurst': 38.42, 'Pomonok-Flushing Heights-Hillcrest': 37.67, 'East New York': 39.24, 'Co-Op City': 34.58, "Annadale-Huguenot-Prince's Bay-Eltingville": 36.21, 'Queens Village': 39.95, 'West Concourse': 36.08, 'Prospect Heights': 39.28, 'Belmont bronx': 38.99, 'Lindenwood-Howard Beach': 21.43, 'Williamsburg': 40.09, 'North Side-South Side': 13.83, 'Auburndale': 39.7, 'Gravesend': 38.2, 'Kew Gardens': 36.6, 'Queensboro Hill queens': 40.14, 'Bronxdale': 39.95, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 39.9, 'Rego Park': 36.64, 'Bellerose': 39.2, 'Bushwick South': 40.54, 'Battery Park City-Lower Manhattan': 40.13, 'Windsor Terrace': 37.09, 'West Brighton': 35.92, 'Arden Heights': 11.91, 'SoHo-TriBeCa-Civic Center-Little Italy': 41.1, 'Hamilton Heights': 40.68, 'Flatbush': 40.47, 'Morningside Heights': 33.11, 'Lower East Side': 41.56, 'Rosedale': 37.41, 'Soundview-Bruckner': 35.8, 'Pelham Parkway': 20.62, 'Laurelton': 33.93, 'Rugby-Remsen Village': 39.49, 'New Springville-Bloomfield-Travis': 32.35, 'Seagate-Coney Island': 37.18, 'Ozone Park': 36.78, 'Prospect Lefferts Gardens-Wingate': 40.72, 'Stuyvesant Town-Cooper Village': 42.55, "Mariner's Harbor-Arlington-Port Ivory-Granite": 36.23, 'Madison brookl': 38.44, 'Hammels-Arverne-Edgemere': 38.89, 'Flatlands': 36.31, 'Cypress Hills-City Line': 38.28, 'Fordham South': 39.48, 'Douglas Manor-Douglaston-Little Neck': 39.21, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 33.95, 'Hollis': 37.44, 'Kew Gardens Hills': 36.6, 'Charleston-Richmond Valley-Tottenville': 34.61, 'Briarwood-Jamaica Hills': 39.96, 'Bath Beach': 36.04, 'Grymes Hill-Clifton-Fox Hills': 37.31, 'Bay Ridge': 38.02, 'Carroll Gardens-Columbia Street-Red Hook': 40.53, 'Kingsbridge Heights': 36.8, 'Melrose South-Mott Haven North': 39.25, 'Brighton Beach': 37.18, 'Ocean Parkway South': 39.46, 'Yorkville nyc': 41.12, 'North Riverdale-Fieldston-Riverdale': 37.25, 'Greenpoint': 41.56, 'East New York (Pennsylvania Ave)': 32.46, 'Mott Haven-Port Morris': 41.91, 'Elmhurst-Maspeth': 40.57, 'East Tremont': 38.75, 'Bensonhurst East': 37.52, 'University Heights-Morris Heights': 38.76, 'East Concourse-Concourse Village': 36.8, 'Brownsville': 39.98, 'Forest Hills': 40.0, "hell's kitchen": 40.15, 'Oakwood-Oakwood Beach': 38.03, 'Longwood': 36.31, 'Jackson Heights': 39.39}
fine_dining_scores = {'Queensbridge-Ravenswood-Long Island City': 30.67, 'Bedford brooklyn': 29.17, 'East Harlem South': 31.86, 'Soundview-Castle Hill-Clason Point-Harding Pa': 18.06, 'Corona': 18.45, 'Jamaica Estates-Holliswood': 18.76, 'Upper East Side-Carnegie Hill': 28.78, 'Central Harlem South': 30.02, 'Marble Hill-Inwood': 16.62, 'Midtown-Midtown South': 35.26, 'Schuylerville-Throgs Neck-Edgewater Park': 11.91, 'Grasmere-Arrochar-Ft. Wadsworth': 12.83, 'Middle Village': 24.22, 'Westchester-Unionport': 15.33, 'Baisley Park': 15.82, 'Washington Heights South': 26.76, 'Chinatown': 29.26, 'Port Richmond': 13.0, 'Hunts Point': 5.47, 'West Farms-Bronx River': 14.29, 'Stuyvesant Heights nyc': 19.35, 'Eastchester-Edenwald-Baychester': 8.68, 'Van Nest-Morris Park-Westchester Square': 8.9, 'Manhattanville': 25.31, 'Bayside-Bayside Hills': 17.91, 'Woodlawn-Wakefield': 9.24, 'Ft. Totten-Bay Terrace-Clearview': 8.58, 'Old Town-Dongan Hills-South Beach': 13.11, 'Stapleton-Rosebank': 13.11, 'New Brighton-Silver Lake': 7.67, 'Erasmus': 18.56, 'West Village': 32.51, 'Parkchester': 14.45, 'Borough Park': 30.47, 'Oakland Gardens': 21.14, 'Westerleigh': 16.81, 'Bushwick North': 27.26, 'Sunset Park West': 24.29, 'Homecrest': 17.56, 'Washington Heights North': 26.76, 'Elmhurst': 25.15, 'Glendale': 21.95, 'Steinway': 28.31, 'Sunset Park East': 24.29, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 20.95, 'Rossville-Woodrow': 9.12, 'Mount Hope': 33.35, 'Turtle Bay-East Midtown': 35.91, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 11.04, 'South Jamaica': 18.45, 'Glen Oaks-Floral Park-New Hyde Park': 14.96, 'Richmond Hill': 21.51, 'Astoria': 28.45, 'Norwood': 18.73, 'St. Albans': 16.09, 'Morrisania-Melrose': 9.88, 'East Harlem North': 19.85, 'Ridgewood': 25.33, 'Midwood': 21.99, 'Pelham Bay-Country Club-City Island': 10.0, 'College Point': 22.07, 'Crotona Park East': 19.92, 'Flushing': 27.11, 'Spuyten Duyvil-Kingsbridge': 17.04, 'Whitestone': 21.64, 'Williamsbridge-Olinville': 19.9, 'North Corona': 19.93, 'Central Harlem North-Polo Grounds': 17.89, 'Allerton-Pelham Gardens': 9.33, 'Hunters Point-Sunnyside-West Maspeth': 22.08, 'Dyker Heights': 21.87, 'East Village': 32.21, 'Van Cortlandt Village': 14.16, 'Canarsie': 14.79, 'Clinton Hill': 24.8, 'New Dorp-Midland Beach': 12.28, 'West New Brighton-New Brighton-St. George': 18.08, 'Claremont-Bathgate': 13.66, 'Rikers Island': 40.73, 'East Flushing': 19.62, 'Bedford Park-Fordham North': 20.08, 'Far Rockaway-Bayswater': 12.03, 'Highbridge': 15.66, 'Fort Greene': 25.01, 'Old Astoria': 14.08, 'Woodside': 37.57, 'Fresh Meadows-Utopia': 22.7, 'Murray Hill': 32.46, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 26.33, 'Woodhaven': 14.1, 'Ocean Hill': 23.6, 'Bensonhurst West': 22.87, 'Crown Heights North': 28.01, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 17.18, 'East Flatbush-Farragut': 12.98, 'East Williamsburg': 30.04, 'Cambria Heights': 16.04, 'South Ozone Park': 16.1, 'Gramercy': 22.12, 'Crown Heights South': 28.01, 'Jamaica': 20.23, 'Maspeth': 24.89, 'Lincoln Square': 32.71, 'Upper West Side': 32.8, 'Great Kills': 15.23, 'Springfield Gardens North': 7.2, 'Lenox Hill-Roosevelt Island': 30.46, 'Brooklyn Heights-Cobble Hill': 26.76, 'Kensington-Ocean Parkway': 18.23, 'Springfield Gardens South-Brookville': 6.98, 'Murray Hill-Kips Bay': 33.61, 'Starrett City': 6.98, 'East Elmhurst': 25.89, 'Pomonok-Flushing Heights-Hillcrest': 19.62, 'East New York': 19.87, 'Co-Op City': 16.6, "Annadale-Huguenot-Prince's Bay-Eltingville": 8.17, 'Queens Village': 19.29, 'West Concourse': 14.4, 'Prospect Heights': 27.11, 'Belmont bronx': 14.95, 'Lindenwood-Howard Beach': 18.86, 'Williamsburg': 25.19, 'North Side-South Side': 11.32, 'Auburndale': 22.4, 'Gravesend': 21.88, 'Kew Gardens': 18.38, 'Queensboro Hill queens': 33.97, 'Bronxdale': 19.97, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 33.01, 'Rego Park': 24.74, 'Bellerose': 20.81, 'Bushwick South': 27.26, 'Battery Park City-Lower Manhattan': 34.89, 'Windsor Terrace': 20.83, 'West Brighton': 17.37, 'Arden Heights': 9.14, 'SoHo-TriBeCa-Civic Center-Little Italy': 32.28, 'Hamilton Heights': 32.6, 'Flatbush': 26.34, 'Morningside Heights': 20.18, 'Lower East Side': 30.22, 'Rosedale': 22.46, 'Soundview-Bruckner': 10.91, 'Pelham Parkway': 19.41, 'Laurelton': 14.2, 'Rugby-Remsen Village': 24.96, 'New Springville-Bloomfield-Travis': 10.2, 'Seagate-Coney Island': 20.68, 'Ozone Park': 18.07, 'Prospect Lefferts Gardens-Wingate': 28.01, 'Stuyvesant Town-Cooper Village': 32.56, "Mariner's Harbor-Arlington-Port Ivory-Granite": 22.11, 'Madison brookl': 20.82, 'Hammels-Arverne-Edgemere': 17.89, 'Flatlands': 20.16, 'Cypress Hills-City Line': 20.98, 'Fordham South': 21.5, 'Douglas Manor-Douglaston-Little Neck': 15.36, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 18.65, 'Hollis': 9.75, 'Kew Gardens Hills': 18.38, 'Charleston-Richmond Valley-Tottenville': 8.84, 'Briarwood-Jamaica Hills': 26.26, 'Bath Beach': 21.8, 'Grymes Hill-Clifton-Fox Hills': 14.95, 'Bay Ridge': 21.78, 'Carroll Gardens-Columbia Street-Red Hook': 24.77, 'Kingsbridge Heights': 17.04, 'Melrose South-Mott Haven North': 21.97, 'Brighton Beach': 20.68, 'Ocean Parkway South': 30.6, 'Yorkville nyc': 32.56, 'North Riverdale-Fieldston-Riverdale': 13.26, 'Greenpoint': 33.85, 'East New York (Pennsylvania Ave)': 14.7, 'Mott Haven-Port Morris': 27.32, 'Elmhurst-Maspeth': 26.26, 'East Tremont': 20.76, 'Bensonhurst East': 23.37, 'University Heights-Morris Heights': 20.2, 'East Concourse-Concourse Village': 15.28, 'Brownsville': 21.86, 'Forest Hills': 28.77, "hell's kitchen": 34.03, 'Oakwood-Oakwood Beach': 14.3, 'Longwood': 9.08, 'Jackson Heights': 27.41}
family_restaurant_scores = {'Queensbridge-Ravenswood-Long Island City': 32.78, 'Bedford brooklyn': 31.31, 'East Harlem South': 34.55, 'Soundview-Castle Hill-Clason Point-Harding Pa': 23.34, 'Corona': 23.29, 'Jamaica Estates-Holliswood': 23.01, 'Upper East Side-Carnegie Hill': 29.89, 'Central Harlem South': 33.0, 'Marble Hill-Inwood': 19.25, 'Midtown-Midtown South': 34.13, 'Schuylerville-Throgs Neck-Edgewater Park': 15.43, 'Grasmere-Arrochar-Ft. Wadsworth': 15.7, 'Middle Village': 26.43, 'Westchester-Unionport': 21.48, 'Baisley Park': 19.44, 'Washington Heights South': 30.45, 'Chinatown': 29.54, 'Port Richmond': 17.27, 'Hunts Point': 13.29, 'West Farms-Bronx River': 21.2, 'Stuyvesant Heights nyc': 21.68, 'Eastchester-Edenwald-Baychester': 13.81, 'Van Nest-Morris Park-Westchester Square': 17.21, 'Manhattanville': 28.9, 'Bayside-Bayside Hills': 20.85, 'Woodlawn-Wakefield': 16.89, 'Ft. Totten-Bay Terrace-Clearview': 12.55, 'Old Town-Dongan Hills-South Beach': 16.89, 'Stapleton-Rosebank': 16.89, 'New Brighton-Silver Lake': 9.96, 'Erasmus': 22.33, 'West Village': 32.15, 'Parkchester': 19.84, 'Borough Park': 31.13, 'Oakland Gardens': 22.73, 'Westerleigh': 21.51, 'Bushwick North': 30.63, 'Sunset Park West': 28.7, 'Homecrest': 22.04, 'Washington Heights North': 30.45, 'Elmhurst': 29.23, 'Glendale': 24.75, 'Steinway': 30.6, 'Sunset Park East': 28.7, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 25.79, 'Rossville-Woodrow': 13.7, 'Mount Hope': 32.73, 'Turtle Bay-East Midtown': 34.35, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 17.14, 'South Jamaica': 24.5, 'Glen Oaks-Floral Park-New Hyde Park': 18.62, 'Richmond Hill': 23.48, 'Astoria': 31.92, 'Norwood': 24.93, 'St. Albans': 22.39, 'Morrisania-Melrose': 18.08, 'East Harlem North': 23.32, 'Ridgewood': 28.22, 'Midwood': 27.16, 'Pelham Bay-Country Club-City Island': 12.87, 'College Point': 25.19, 'Crotona Park East': 25.04, 'Flushing': 31.68, 'Spuyten Duyvil-Kingsbridge': 20.95, 'Whitestone': 24.93, 'Williamsbridge-Olinville': 25.47, 'North Corona': 23.61, 'Central Harlem North-Polo Grounds': 21.44, 'Allerton-Pelham Gardens': 13.51, 'Hunters Point-Sunnyside-West Maspeth': 25.65, 'Dyker Heights': 28.31, 'East Village': 32.82, 'Van Cortlandt Village': 19.21, 'Canarsie': 17.94, 'Clinton Hill': 25.45, 'New Dorp-Midland Beach': 16.6, 'West New Brighton-New Brighton-St. George': 22.32, 'Claremont-Bathgate': 18.67, 'Rikers Island': 39.94, 'East Flushing': 23.8, 'Bedford Park-Fordham North': 25.95, 'Far Rockaway-Bayswater': 18.29, 'Highbridge': 20.68, 'Fort Greene': 25.87, 'Old Astoria': 17.49, 'Woodside': 36.44, 'Fresh Meadows-Utopia': 26.09, 'Murray Hill': 31.09, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 27.22, 'Woodhaven': 19.56, 'Ocean Hill': 27.52, 'Bensonhurst West': 27.21, 'Crown Heights North': 30.33, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 20.6, 'East Flatbush-Farragut': 19.54, 'East Williamsburg': 32.14, 'Cambria Heights': 20.28, 'South Ozone Park': 22.1, 'Gramercy': 21.98, 'Crown Heights South': 30.33, 'Jamaica': 24.23, 'Maspeth': 27.29, 'Lincoln Square': 31.74, 'Upper West Side': 31.52, 'Great Kills': 19.25, 'Springfield Gardens North': 15.17, 'Lenox Hill-Roosevelt Island': 30.25, 'Brooklyn Heights-Cobble Hill': 27.36, 'Kensington-Ocean Parkway': 22.64, 'Springfield Gardens South-Brookville': 13.43, 'Murray Hill-Kips Bay': 32.02, 'Starrett City': 11.54, 'East Elmhurst': 27.33, 'Pomonok-Flushing Heights-Hillcrest': 23.8, 'East New York': 21.52, 'Co-Op City': 19.81, "Annadale-Huguenot-Prince's Bay-Eltingville": 12.37, 'Queens Village': 22.96, 'West Concourse': 18.12, 'Prospect Heights': 29.53, 'Belmont bronx': 20.31, 'Lindenwood-Howard Beach': 21.74, 'Williamsburg': 27.14, 'North Side-South Side': 15.89, 'Auburndale': 26.75, 'Gravesend': 26.94, 'Kew Gardens': 21.96, 'Queensboro Hill queens': 35.3, 'Bronxdale': 25.68, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 31.91, 'Rego Park': 25.61, 'Bellerose': 23.25, 'Bushwick South': 30.63, 'Battery Park City-Lower Manhattan': 34.14, 'Windsor Terrace': 23.65, 'West Brighton': 22.85, 'Arden Heights': 11.85, 'SoHo-TriBeCa-Civic Center-Little Italy': 30.81, 'Hamilton Heights': 35.33, 'Flatbush': 28.72, 'Morningside Heights': 21.28, 'Lower East Side': 32.06, 'Rosedale': 26.37, 'Soundview-Bruckner': 18.68, 'Pelham Parkway': 21.47, 'Laurelton': 20.32, 'Rugby-Remsen Village': 27.38, 'New Springville-Bloomfield-Travis': 16.39, 'Seagate-Coney Island': 25.28, 'Ozone Park': 23.32, 'Prospect Lefferts Gardens-Wingate': 30.33, 'Stuyvesant Town-Cooper Village': 33.0, "Mariner's Harbor-Arlington-Port Ivory-Granite": 26.32, 'Madison brookl': 26.43, 'Hammels-Arverne-Edgemere': 14.19, 'Flatlands': 24.12, 'Cypress Hills-City Line': 23.97, 'Fordham South': 26.21, 'Douglas Manor-Douglaston-Little Neck': 18.55, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 22.56, 'Hollis': 16.85, 'Kew Gardens Hills': 21.96, 'Charleston-Richmond Valley-Tottenville': 14.84, 'Briarwood-Jamaica Hills': 30.9, 'Bath Beach': 24.65, 'Grymes Hill-Clifton-Fox Hills': 18.23, 'Bay Ridge': 27.22, 'Carroll Gardens-Columbia Street-Red Hook': 26.45, 'Kingsbridge Heights': 20.95, 'Melrose South-Mott Haven North': 26.06, 'Brighton Beach': 25.28, 'Ocean Parkway South': 33.1, 'Yorkville nyc': 34.67, 'North Riverdale-Fieldston-Riverdale': 17.63, 'Greenpoint': 34.76, 'East New York (Pennsylvania Ave)': 19.06, 'Mott Haven-Port Morris': 29.54, 'Elmhurst-Maspeth': 30.41, 'East Tremont': 25.81, 'Bensonhurst East': 27.17, 'University Heights-Morris Heights': 24.88, 'East Concourse-Concourse Village': 19.67, 'Brownsville': 25.3, 'Forest Hills': 31.65, "hell's kitchen": 34.58, 'Oakwood-Oakwood Beach': 18.78, 'Longwood': 16.65, 'Jackson Heights': 29.8}

# from liquor.py, this is the active liquor licenses count
nb_count_dict = {'Lindenwood-Howard Beach': 40, 'Longwood': 90, 'North Riverdale-Fieldston-Riverdale': 32, 'Norwood': 136, 'Schuylerville-Throgs Neck-Edgewater Park': 71, 'Stuyvesant Town-Cooper Village': 497, 'Fordham South': 168, 'Bushwick North': 210, 'Rego Park': 81, 'North Corona': 288, 'Flatlands': 124, 'Lincoln Square': 153, 'Rosedale': 27, 'St. Albans': 43, 'Soundview-Castle Hill-Clason Point-Harding Pa': 121, 'Yorkville nyc': 157, 'Sunset Park East': 223, 'Brooklyn Heights-Cobble Hill': 257, 'West Concourse': 100, 'Springfield Gardens North': 33, 'Oakland Gardens': 35, 'Queens Village': 29, 'Gravesend': 164, 'Corona': 288, 'Dyker Heights': 67, 'Bedford Park-Fordham North': 168, 'West New Brighton-New Brighton-St. George': 53, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 179, 'Spuyten Duyvil-Kingsbridge': 102, 'Soundview-Bruckner': 121, 'Williamsbridge-Olinville': 194, 'Greenpoint': 231, 'Clinton Hill': 131, 'Cambria Heights': 18, 'Woodside': 213, 'Chinatown': 332, 'Allerton-Pelham Gardens': 66, 'West Brighton': 53, 'Starrett City': 13, 'Van Nest-Morris Park-Westchester Square': 119, 'Belmont bronx': 168, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 65, 'Kew Gardens': 31, 'East Village': 303, 'University Heights-Morris Heights': 126, 'Central Harlem North-Polo Grounds': 24, 'Elmhurst': 156, 'East New York (Pennsylvania Ave)': 183, 'Bushwick South': 210, 'Bronxdale': 119, 'Jamaica Estates-Holliswood': 30, 'Gramercy': 541, 'Morningside Heights': 117, 'Crown Heights South': 96, 'Jackson Heights': 252, 'Washington Heights North': 296, 'Washington Heights South': 110, 'Westerleigh': 126, 'East Flatbush-Farragut': 115, 'Highbridge': 141, 'Homecrest': 164, 'Hollis': 30, 'Great Kills': 52, 'Bellerose': 22, 'Cypress Hills-City Line': 167, 'Briarwood-Jamaica Hills': 119, 'Grymes Hill-Clifton-Fox Hills': 91, 'Lenox Hill-Roosevelt Island': 80, 'Claremont-Bathgate': 132, 'Sunset Park West': 223, 'Prospect Lefferts Gardens-Wingate': 96, 'Bath Beach': 151, 'East Concourse-Concourse Village': 100, 'Forest Hills': 151, 'Springfield Gardens South-Brookville': 33, 'Grasmere-Arrochar-Ft. Wadsworth': 65, 'Auburndale': 129, 'South Jamaica': 41, 'Stuyvesant Heights nyc': 93, 'Midwood': 80, 'Westchester-Unionport': 132, 'Van Cortlandt Village': 100, 'Brighton Beach': 179, 'Old Astoria': 84, 'Borough Park': 100, 'Manhattanville': 117, 'Battery Park City-Lower Manhattan': 252, 'Parkchester': 119, 'East Flushing': 230, 'Ocean Parkway South': 80, 'Stapleton-Rosebank': 92, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 726, 'Midtown-Midtown South': 480, 'Marble Hill-Inwood': 104, 'Charleston-Richmond Valley-Tottenville': 29, 'College Point': 52, 'Kew Gardens Hills': 31, 'Central Harlem South': 64, 'Ozone Park': 58, 'Richmond Hill': 92, 'Fresh Meadows-Utopia': 34, 'Bayside-Bayside Hills': 102, "Annadale-Huguenot-Prince's Bay-Eltingville": 66, 'Whitestone': 60, 'Elmhurst-Maspeth': 156, 'Seagate-Coney Island': 81, 'Upper West Side': 379, 'East Harlem South': 155, 'Flushing': 230, 'Rossville-Woodrow': 62, 'Hamilton Heights': 100, 'Fort Greene': 131, 'Turtle Bay-East Midtown': 329, 'Co-Op City': 36, 'New Brighton-Silver Lake': 91, 'Rugby-Remsen Village': 115, 'Hunts Point': 35, 'Baisley Park': 69, 'Madison brookl': 114, 'Ocean Hill': 93, 'Pelham Bay-Country Club-City Island': 35, 'Far Rockaway-Bayswater': 48, 'Maspeth': 84, 'Kensington-Ocean Parkway': 125, 'New Dorp-Midland Beach': 82, 'Prospect Heights': 224, 'Laurelton': 33, 'Ridgewood': 279, 'Melrose South-Mott Haven North': 100, 'Canarsie': 87, 'Middle Village': 48, 'Carroll Gardens-Columbia Street-Red Hook': 178, 'Bensonhurst East': 105, 'Hammels-Arverne-Edgemere': 8, 'Douglas Manor-Douglaston-Little Neck': 32, 'Mount Hope': 541, 'Glendale': 279, 'Murray Hill-Kips Bay': 350, "hell's kitchen": 480, 'Queensboro Hill queens': 124, 'Jamaica': 97, 'East Harlem North': 22, 'Clinton': 1134, 'Woodlawn-Wakefield': 67, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 451, 'East Tremont': 132, 'New Springville-Bloomfield-Travis': 126, 'Queensbridge-Ravenswood-Long Island City': 394, 'Oakwood-Oakwood Beach': 82, 'Kingsbridge Heights': 102, 'Glen Oaks-Floral Park-New Hyde Park': 100, 'Steinway': 127, 'Lower East Side': 364, 'Bensonhurst West': 151, 'Eastchester-Edenwald-Baychester': 36, 'East Elmhurst': 45, 'Pomonok-Flushing Heights-Hillcrest': 408, 'SoHo-TriBeCa-Civic Center-Little Italy': 417, 'Windsor Terrace': 309, 'Morrisania-Melrose': 119, 'West Farms-Bronx River': 88, 'Hunters Point-Sunnyside-West Maspeth': 93, 'Erasmus': 153, 'Murray Hill': 350, 'East New York': 183, 'Brownsville': 119, 'West Village': 711, 'Williamsburg': 479, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 124, 'Port Richmond': 63, 'Crown Heights North': 96, 'East Williamsburg': 479, 'Astoria': 176, "Mariner's Harbor-Arlington-Port Ivory-Granite": 39, 'Bedford brooklyn': 127, 'Mott Haven-Port Morris': 90, 'Flatbush': 153, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 11, 'Woodhaven': 70, 'Crotona Park East': 88, 'Old Town-Dongan Hills-South Beach': 92, 'Upper East Side-Carnegie Hill': 618, 'South Ozone Park': 23, 'Ft. Totten-Bay Terrace-Clearview': 16, 'Bay Ridge': 210}

# generate_score(bar_scores, restaurant_scores, atmosphere_restaurant_scores, fine_dining_scores, family_restaurant_scores)
yelp_average = {'Park Slope-Gowanus': 34, 'Van Cortlandt Village': 22, 'College Point': 27, 'Homecrest': 24, 'West Village': 34, 'New Dorp-Midland Beach': 18, 'Borough Park': 33, 'Cypress Hills-City Line': 27, 'Soundview-Castle Hill-Clason Point-Harding Pa': 25, 'Starrett City': 15, 'New Springville-Bloomfield-Travis': 18, 'Laurelton': 21, 'Arden Heights': 11, 'Gravesend': 28, 'Melrose South-Mott Haven North': 28, 'Bedford Park-Fordham North': 27, 'Lindenwood-Howard Beach': 22, 'Kew Gardens Hills': 24, 'Baisley Park': 23, 'Elmhurst-Maspeth': 31, 'West Concourse': 22, 'Crown Heights North': 32, 'Allerton-Pelham Gardens': 17, 'Springfield Gardens North': 17, 'West Brighton': 24, 'Stuyvesant Heights nyc': 26, 'Corona': 25, 'Port Richmond': 20, 'Oakland Gardens': 25, 'Stapleton-Rosebank': 19, 'Marble Hill-Inwood': 23, 'Upper West Side': 34, 'Charleston-Richmond Valley-Tottenville': 17, 'Upper East Side-Carnegie Hill': 32, 'Old Town-Dongan Hills-South Beach': 19, 'Rikers Island': 34, 'Kew Gardens': 24, 'Woodhaven': 22, 'East Tremont': 28, 'Schuylerville-Throgs Neck-Edgewater Park': 19, 'Mott Haven-Port Morris': 32, 'Van Nest-Morris Park-Westchester Square': 18, 'Gramercy': 26, 'Bedford brooklyn': 34, 'Ocean Parkway South': 34, 'Bay Ridge': 28, 'Eastchester-Edenwald-Baychester': 16, 'Bensonhurst West': 28, 'East Village': 35, 'East Flushing': 26, 'Ft. Totten-Bay Terrace-Clearview': 16, 'East Elmhurst': 30, 'Prospect Lefferts Gardens-Wingate': 32, 'Claremont-Bathgate': 22, "hell's kitchen": 36, 'Pelham Bay-Country Club-City Island': 16, "Mariner's Harbor-Arlington-Port Ivory-Granite": 28, 'Oakwood-Oakwood Beach': 21, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 23, 'North Riverdale-Fieldston-Riverdale': 20, 'Ozone Park': 25, 'Williamsbridge-Olinville': 27, 'Bushwick North': 33, 'Parkchester': 22, 'Williamsburg': 30, 'University Heights-Morris Heights': 27, 'Soundview-Bruckner': 20, 'East New York': 26, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 23, 'Bayside-Bayside Hills': 23, 'Astoria': 33, 'Bensonhurst East': 29, 'Richmond Hill': 26, 'Ocean Hill': 30, 'Rossville-Woodrow': 16, 'Brownsville': 28, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 35, 'Flatlands': 26, 'Carroll Gardens-Columbia Street-Red Hook': 29, 'Far Rockaway-Bayswater': 20, 'Morningside Heights': 24, 'Greenpoint': 37, 'Central Harlem North-Polo Grounds': 25, 'East Harlem North': 26, 'Erasmus': 26, 'Flatbush': 31, 'Woodside': 38, 'Co-Op City': 23, 'Old Astoria': 17, 'Lenox Hill-Roosevelt Island': 33, 'Murray Hill': 34, 'Midtown-Midtown South': 37, 'Yorkville nyc': 36, 'Queensbridge-Ravenswood-Long Island City': 34, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 27, 'Auburndale': 28, 'Lincoln Square': 34, 'Jamaica Estates-Holliswood': 25, 'Manhattanville': 31, 'North Side-South Side': 14, 'Great Kills': 22, 'Glen Oaks-Floral Park-New Hyde Park': 21, 'Woodlawn-Wakefield': 19, 'Belmont bronx': 23, 'Morrisania-Melrose': 21, 'Fort Greene': 28, "Annadale-Huguenot-Prince's Bay-Eltingville": 16, 'West New Brighton-New Brighton-St. George': 25, 'Rugby-Remsen Village': 30, 'Jamaica': 26, 'East New York (Pennsylvania Ave)': 22, 'Brighton Beach': 26, 'Highbridge': 24, 'Spuyten Duyvil-Kingsbridge': 24, 'Bath Beach': 26, 'Douglas Manor-Douglaston-Little Neck': 21, 'Jackson Heights': 31, 'Whitestone': 27, 'Springfield Gardens South-Brookville': 16, 'Queensboro Hill queens': 36, 'Mount Hope': 35, 'Ridgewood': 30, 'Fordham South': 28, 'Brooklyn Heights-Cobble Hill': 29, 'Washington Heights South': 32, 'Washington Heights North': 32, 'Clinton Hill': 29, 'Hamilton Heights': 36, 'East Concourse-Concourse Village': 23, 'Hunts Point': 16, 'Rego Park': 28, 'Longwood': 19, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 20, 'Windsor Terrace': 26, 'Elmhurst': 30, 'Westchester-Unionport': 23, 'St. Albans': 24, 'Dyker Heights': 28, 'Turtle Bay-East Midtown': 37, 'Battery Park City-Lower Manhattan': 36, 'Steinway': 32, 'South Ozone Park': 24, 'Maspeth': 29, 'Cambria Heights': 22, 'Glendale': 27, 'Flushing': 33, 'Chinatown': 32, 'Briarwood-Jamaica Hills': 32, 'Middle Village': 29, 'Hollis': 19, 'Stuyvesant Town-Cooper Village': 35, 'Rosedale': 28, 'Hammels-Arverne-Edgemere': 18, 'East Flatbush-Farragut': 22, 'Kingsbridge Heights': 24, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 30, 'East Williamsburg': 34, 'Pomonok-Flushing Heights-Hillcrest': 26, 'Fresh Meadows-Utopia': 27, 'Grasmere-Arrochar-Ft. Wadsworth': 19, 'Seagate-Coney Island': 26, 'West Farms-Bronx River': 22, 'Midwood': 28, 'Bellerose': 26, 'Bronxdale': 27, 'Madison brookl': 27, 'Murray Hill-Kips Bay': 35, 'Hunters Point-Sunnyside-West Maspeth': 28, 'Queens Village': 25, 'Canarsie': 21, 'Bushwick South': 33, 'Prospect Heights': 32, 'East Harlem South': 36, 'Norwood': 26, 'Westerleigh': 23, 'South Jamaica': 26, 'SoHo-TriBeCa-Civic Center-Little Italy': 34, 'Grymes Hill-Clifton-Fox Hills': 21, 'Kensington-Ocean Parkway': 25, 'Lower East Side': 34, 'Forest Hills': 33, 'New Brighton-Silver Lake': 17, 'Crown Heights South': 32, 'Central Harlem South': 35, 'Crotona Park East': 27, 'Sunset Park West': 29, 'Sunset Park East': 29, 'Pelham Parkway': 20, 'North Corona': 26}

def update_nb_nightlife_score(score_dict):
	# check if nb exists in score table
	for nb in score_dict:
		# may not be able to filter on foreign key attribute
		nb_obj = Neighborhood.objects.filter(name=nb)
		if nb_obj:
			nb_obj = nb_obj[0]
			score_row = Score.objects.filter(neighborhood=nb_obj)
			# if nb_score exists
			# probably should use get_or_create()
			if score_row:
				score_row[0].night_life_score = score_dict[nb]
				score_row[0].save()
			else:
				# create nb_score
				nb_obj = Neighborhood.objects.get(name=nb)
				score_row = Score.objects.create(
					neighborhood=nb_obj,
					night_life_score=score_dict[nb],
					commute_score=0,
					crime_score=0,
					noise_score=0,				
				)
		else:
			print("didn't find nb_obj: ", nb)

	return True

def run():
	update_nb_nightlife_score(avg_yelp_plus_liquor)
