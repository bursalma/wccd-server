USE `white_collar`;

DELETE FROM `scheme`;
DELETE FROM `crime`;
DELETE FROM `sector`;
DELETE FROM `occupation`;
DELETE FROM `race`;
DELETE FROM `source_type`;
DELETE FROM `user`;

ALTER TABLE `scheme`      AUTO_INCREMENT = 1;
ALTER TABLE `crime`       AUTO_INCREMENT = 1;
ALTER TABLE `sector`      AUTO_INCREMENT = 1;
ALTER TABLE `occupation`  AUTO_INCREMENT = 1;
ALTER TABLE `race`        AUTO_INCREMENT = 1;
ALTER TABLE `source_type` AUTO_INCREMENT = 1;
ALTER TABLE `user` 		  AUTO_INCREMENT = 1;

INSERT INTO `user` (`username`, `password`, `full_name`, `email`, 			   `privilege`)
VALUES			   ('admin', 	'password', 'admin', 	 'bursalma@gmail.com', 'admin');

INSERT INTO `source_type` (`source_type`)
VALUES  ('Book'), 		  ('Broadcast Transcripts'), ('Commercial/Non-Governmental Source'), ('Court Document'), 
	    ('Dataset'),      ('Governmental Report'),   ('Journal'), 						     ('Magazine'), 
	    ('Mailing List'), ('Newspaper'),             ('NGO Report'), 						 ('Website'), 
	    ('Wire Report');

INSERT INTO `race` (`race`)
VALUES ('Asian'), ('Black'), ('Hispanic'), ('White'), ('Other'), ('NOT REPORTED');

INSERT INTO `occupation` (`occupation`)
VALUES 	('Accountant'), 			('Artist / Celebrity'),  ('Author / Writer'), 		   ('Business Manager / Agent'), 
		('Businessman'), 			('Computer Programmer'), ('Con Artist'), 			   ('Contractor'), 
        ('Controller + Treasurer'), ('Corporate Figure'), 	 ('Educational Figure'), 	   ('Engineer / Specialist / Developer'), 
        ('Financial Advisor'), 		('Judicial Figure'), 	 ('Law Enforcement Figure'),   ('Media Figure / Journalist'), 
        ('Medical Figure'), 		('Military Figure'), 	 ('Mortgage Broker / Trader'), ('OC Figure'), 
        ('Political Figure'), 		('Public Employee'), 	 ('Religious Figure'), 		   ('Sports Figure'), 
        ('Store Owner'), 			('OTHER'), 				 ('NOT REPORTED');
        
INSERT INTO `sector` (`sector`, `sector_desc`)
VALUES 	('Accommodation and Food Services', 					'Beverage/Leisure/Hotels-Motels/Restaurant'), 
		('Agriculture & Forestry & Fishing and Hunting', 		NULL), 
        ('Amusement, Gambling, and Recreation Industries', 		NULL), 
        ('Apparel Manufacturing', 								'Clothing and Accessories Stores'), 
        ('Architecture and Engineering', 						NULL), 
		('Arts, Entertainment, and Recreation', 				NULL), 
        ('Business and Financial', 								'Banking/Funds/Insurance/Investment'), 
        ('Construction and Real Estate Development', 			NULL), 
        ('Educational Services', 								'Schools/Training/Library'), 
        ('Energy (Utilities) & Oil Industry', 					NULL), 
        ('Government & Public Office', 							'Administrative and Support Services'), 
        ('Healthcare', 											'Hospitals/Clinics/Personal Care'), 
        ('Information Technology', 								'Data Processing, Hosting, and Related Services'), 
		('Legal & Judiciary', 									NULL),
		('Media & Communications', 								'Internet Publishing and Broadcasting'), 
        ('Military & Security', 								'Defense Contractors'), 
        ('Motion Picture and Sound Recording Industries', 		NULL), 
        ('Museums, Historical Sites, and Similar Institutions', NULL), 
        ('Natural Resources and Mining (except Oil and Gas)', 	NULL), 
        ('Postal Service', 										'Couriers and Messengers'), 
        ('Religious & Charity Organizations', 					NULL), 
        ('Retail Industry', 									'General Merchandise Stores'), 
        ('Transportation & Logistics', 							'Air/Ground/Water'), 
        ('Waste Management & Disposal Services', 				NULL), 
        ('OTHER', 												NULL), 
        ('NOT REPORTED', 										NULL);
        
INSERT INTO `crime` (`crime`, `crime_desc`)
VALUES  ('Bank Fraud', 					'To engage in an act or pattern of activity where the purpose is to defraud a bank of funds.'), 
		('Blackmail', 					'A demand for money or other consideration under threat to do bodily harm, to injure property, to accuse of a crime, or to expose secrets.'), 
		('Bribery', 					'When money, goods, services, information or anything else of value is offered with intent to influence the actions, opinions, or decisions of the taker. You may be charged with bribery whether you offer the bribe or accept it.'), 
		('Cellular Phone Fraud', 		'The unauthorized use, tampering, or manipulation of a cellular phone or service. This can be accomplished by either use of a stolen phone, or where an actor signs up for service under false identification or where the actor clones a valid electronic serial number (ESN) by using an ESN reader and reprograms another cellular phone with a valid ESN number.'), 
		('Computer fraud', 				'Where computer hackers steal information sources contained on computers such as: bank information, credit cards, and proprietary information.'), 
		('Counterfeiting', 				'Occurs when someone copies or imitates an item without having been authorized to do so and passes the copy off for the genuine or original item. Counterfeiting is most often associated with money however can also be associated with designer clothing, handbags and watches.'), 
		('Credit Card Fraud', 			'The unauthorized use of a credit card to obtain goods of value.'), 
		('Currency Schemes', 			'The practice of speculating on the future value of currencies.'), 
		('Embezzlement', 				'When a person who has been entrusted with money or property appropriates it for his or her own use and benefit.'), 
		('Environmental Schemes', 		'The overbilling and fraudulent practices exercised by corporations which purport to clean up the environment.'), 
		('Extortion', 					'Occurs when one person illegally obtains property from another by actual or threatened force, fear, or violence, or under cover of official right.'), 
		('Forgery', 					'When a person passes a false or worthless instrument such as a check or counterfeit security with the intent to defraud or injure the recipient.'), 
		('Funeral and Cemetery Fraud', 	'Regulations for prepaid funeral services vary from state to state, providing a window of opportunity for unscrupulous operators to overcharge expenses and list themselves as beneficiaries.'), 
		('Health Care Fraud', 			'Where an unlicensed health care provider provides services under the guise of being licensed and obtains monetary benefit for the service.'), 
		('Insider Trading', 			'When a person uses inside, confidential, or advance information to trade in shares of publicly held corporations.'), 
		('Insurance Fraud', 			'To engage in an act or pattern of activity wherein one obtains proceeds from an insurance company through deception.'), 
		('Investment Schemes', 			'Where an unsuspecting victim is contacted by the actor who promises to provide a large return on a small investment.'), 
		('Kickback', 					'Occurs when a person who sells an item pays back a portion of the purchase price to the buyer.'), 
		('Larceny/Theft', 				"When a person wrongfully takes another person's money or property with the intent to appropriate, convert or steal it."), 
		('Money Laundering', 	   		'The investment or transfer of money from racketeering, drug transactions or other embezzlement schemes so that it appears that its original source either cannot be traced or is legitimate.'), 
		('Racketeering', 		  		'The operation of an illegal business for personal profit.'), 
		('Reverse Mortgage Scams',		'Reverse mortgage scams are engineered by unscrupulous professionals in a multitude of real estate, financial services, and related companies to steal the equity from the property of unsuspecting senior citizens or to use these seniors to unwittingly aid the fraudsters in stealing equity from a flipped property.'), 
		('Securities Fraud', 			'The act of artificially inflating the price of stocks by brokers so that buyers can purchase a stock on the rise.'), 
		('Tax Evasion', 				'When a person commits fraud in filing or paying taxes.'), 
		('Telemarketing Fraud', 		'Actors operate out of boiler rooms and place telephone calls to residences and corporations where the actor requests a donation to an alleged charitable organization or where the actor requests money up front or a credit card number up front, and does not use the donation for the stated purpose.'), 
		('Weights and Measures', 		'The act of placing an item for sale at one price yet charging a higher price at the time of sale or short weighing an item when the label reflects a higher weight.'), 
		('Welfare Fraud', 				'To engage in an act or acts where the purpose is to obtain benefits (i.e. Public Assistance, Food Stamps, or Medicaid) from the State or Federal Government.'),
		('OTHER', 						NULL), 
		('NOT REPORTED', 				NULL);

INSERT INTO `scheme` (`scheme`, `scheme_desc`)
VALUES  ('Advanced Fee Schemes', 			'Actor induces victim to give him some type of advanced fee in return for a future benefit. The future benefit never occurs and victim never receives the advanced fee back.'),
		('Airport Scam', 					'Actor approaches victim in an airport stating that the newspaper stand cannot change his one hundred dollar bill and asks the victim for change. Victim provides actor with the change, actor returns to the store to get the one hundred dollar bill back, however, never returns to victim.'),
		('Auto Repair', 					'Actor hangs out around an auto repair shop and approaches victims who leave after getting estimates. Actor claims to do work off duty at a very low cost. Once actor has the car, inferior work is completed and victim cannot get the return of the car until the very high bill is paid.'),
		('Check Kiting', 					'A bank account is opened with good funds and a rapport is developed with the bank. Actor then deposits a series of bad checks but prior to their discovery, withdraws funds from the bank.'),
		('Coupon Redemption', 				'Grocery stores amass large amounts of coupons and redeem them to manufacturers when in fact merchandise was never sold.'),
		('Directory Advertising', 			'Actor either impersonates sales person from a directory company like the yellow pages or fraudulently sells advertising which the victim never receives.'),
		('Fortune Telling', 				'Actor advises victim that victim is cursed. Actor advises victim that the curse must be removed. Actor advises that she must meditate to the spirits and will require payment. Over a period of time, victim pays fortune teller thousands of dollars to remove curse.'),
		('Gypsies', 						'Actor states that victims money is cursed. In order to remove the curse, the money must be placed into a bag or box that the actor provides. The bag or box is switched. Actor advises victim to perform certain rituals over the money and the curse will be removed. The bag or box cannot be opened for a period of time when it is opened, the money is gone.'),
		('Home Improvement', 				'Actor approaches a home owner with a very low estimate for a repair or improvement. Inferior or incomplete work is performed. Once the repairs are completed, actor intimidates the victim to pay a price much greater than the original estimate.'),
		('Inferior Equipment', 				'Actors travel around selling inferior equipment such as tools at high prices.'),
		('Jamaican Switch', 				'Actor #1 approaches a victim looking for the address of a prostitute. Actor #1 shows a large sum of money to the victim. Actor #2 arrives and tells Actor #1 where he can find the prostitute but cautions on taking all the money as the prostitute might rob him. Actor #1 asks the victim to hold the money for him. Actor #1 puts his money into a handkerchief with the victims money. Actor #1 shows the victim how to hide the money under his arm, inside his shirt while switching handkerchiefs. Victim takes the handkerchief and the parties split up, however, Actor #1 leaves with victims money.'),
		('Land Fraud', 						'Actor induces victim to purchase tracks of land in some type of retirement development which does not exist.'),
		('Odometer Fraud', 					'Unscrupulous used car salesman purchased used cars and turn back the odometers. The used car is sold at a higher price due to its low mileage.'),
		('Pigeon Drop', 					'Actor #1 befriends the victim. Actor #2 shows both Actor #1 and victim a "found" package containing a large amount of cash. Actor #1 insists that the found money be divided equally but only after each person puts up his own money to demonstrate good faith. All the money is put in one package and the package is later switched.'),
		('Police Impersonation', 			'Actor tells victim that his bank is being operated by fraudulent bank officers. Actor instructs victim to take money out of bank and place it into a good bank. After the money is withdrawn, the actor allegedly takes the money to the police station for safe keeping. The victim never sees the money again.'),
		('Ponzi', 							'An investment scheme where the actor solicits investors in a business venture, promising extremely high financial returns or dividends in a very short period of time. The actor never invests the money, however, does pay dividends. The dividends consist of the newest investors funds. The first investors, pleased to receive dividends, encourage new investors to invest. This scheme falls apart when the actor no longer has sufficient new investors to distribute dividends to the old investors or the actor simply takes all the funds and leaves the area.'),
		('Pyramid', 						'An investment fraud in which an individual is offered a distributorship or franchise to market a particular product. The promoter of the pyramid represents that although marketing of the product will result in profits, larger profits will be earned by the sale of franchises. For example, if a franchise price is $10,000.00, the seller receives $3,500.00 for every franchise sold. Each new franchise purchaser is presented with the same proposal so that each franchise owner is attempting to sell franchises. Once the supply of potential investors is exhausted, the pyramid collapses. Many times, there are no products involved in the franchise, simply just the exchange of money.'),
		('Quick Change', 					'Victim is confused by actors speedy series of money exchanges and in the end, is short changed.'),
		('Shell Game', 						'Actor #1 manipulates a pea beneath three walnut shells or bottle caps. Actor #1 moves the caps around and shows victim the cap with the pea under it. With the encouragement of another player, also Actor #2, victim places larger and larger bets as to which cap contains the pea. The game is ended by Actor #1 when the take is large enough.'),
		('Utilities Impersonators', 		'Actor impersonates utilities employees by wearing jumpsuits with name tags. Actor approaches victim with story about a gas leak or electrical surge to gain entry to the home. Valuables are taken by actor.'),
		('VCR Scam', 						"Actor purports to sell new VCR's or televisions at an extremely low cost due to his connections. Victim pays for the VCR or television only to discover that the box has been filled with rocks."),
		('West African Investment Scams', 	"Actors target businesses and obtain business' bank account information from which all funds are later withdrawn."),
		('Pump and Dump', 					"A highly illegal practice where a small group of informed people buy a stock before they recommend it to thousands of investors. The result is a quick spike in stock price followed by an equally fast downfall. The perpetrators who bought the stock early sell off when the price peaks at a huge profit. Most pump and dump schemes recommend companies that are over-the-counter bulletin board (OTCBB) and have a small float. Small companies are more volatile and it's easier to manipulate a stock when there's little or no information available about the company. There is also a variation of this scam called the \"short and distort.\" Instead of spreading positive news, fraudsters use a smear campaign and attempt to drive the stock price down. Profit is then made by short selling."), 
		('Prime Bank',						"This term usually describes the top 50 banks (or thereabouts) in the world. Prime banks trade high quality and low risk instruments such as world paper, International Monetary Fund bonds, and Federal Reserve notes. You should be very wary when you hear this term--it is often used by fraudsters looking to lend legitimacy to their cause. Prime bank programs often claim investors' funds will be used to purchase and trade \"prime bank\" financial instruments for huge gains. Unfortunately these \"prime bank\" instruments often never exist and people lose all of their money."),
		('Off Shore Investing', 			"These are becoming one of the more popular scams to trap U.S. and Canadian investors. Conflicting time zones, differing currencies, and the high costs of international telephone calls made it difficult for fraudsters to prey on North American residents. The Internet has eroded these barriers. Be all the more cautious when considering an investment opportunity originating in another country. It's extremely difficult for your local law enforcement agencies to investigate and prosecute foreign criminals."),
		('OTHER', 							NULL), 
		('NOT REPORTED', 					NULL);
