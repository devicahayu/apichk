from random import randint
class infobill:
    __name = (
        'Scott',
        'Gallagher',
        'Susan',
        'Van',
        'Carla',
        'Seese',
        'Dawn',
        'Britt',
        'Mark',
        'Ellis',
        'Rosemary',
        'Morris',
        'SueAnn',
        'Dowell',
        'Shawna',
        'Burns',
        'Donald',
        'Linder',
        'Rita',
        'DeOliveira',
        'James',
        'Koop',
        'Nicholas',
        'Taylor',
        'Veronica',
        'Smith',
        'Paul',
        'Lidberg',
        'Ricky',
        'McGhee',
        'Gwendolyn',
        'Alleman',
        'Phillip',
        'OReilly',
        'Annette',
        'Cavalier',
        'Ida',
        'Harrison',
        'Tiffany',
        'Megli',
        'Karen',
        'Hurst',
        'Kate',
        'Weathersby',
        'Caroline',
        'Kim',
        'Owens',
        'Kyle',
        'Dupre',
        'Stephanie',
        'Stalter',
        'Pam',
        'Headlee',
        'Michael',
        'Howard',
        'Jenny',
        'Borders',
        'Jerry',
        'Stanley',
        'Judy',
        'Lauren',
        'Teague',
        'Berry',
        'Lynn',
        'Kenneth',
        'Schmidt',
        'Madison',
        'Rachel',
        'Nault',
        'Casey',
        'Hart',
        'Deborah',
        'Theriot',
        'Anju',
        'Ahuja',
        'Adam',
        'Harrington',
        'Megan',
        'Schumacher',
        'Heather',
        'Larsen',
        'Anthony',
        'Lama',
        'Karri',
        'Tugwell',
        'Amber',
        'Bernot',
        'Greg',
        'Davidson',
        'Clarissa',
        'Lowery',
        'Tina',
        'Mathieu',
        'Rodger',
        'Dougherty',
        'Kathryn',
        'Slack',
        'Lucy',
        'Johnson',
        'David',
        'Sheffield',
        'Kathy',
        'Crist',
        'Dennis',
        'Strickland',
        'Summer',
        'Golden',
        'Paige',
        'Harden',
        'Tanya',
        'Canup',
        'Patricia',
        'Moroney',
        'Angela',
        'Slayton',
        'Robert',
        'Autenreith',
        'Landry',
        'Joan',
        'Pustka',
        'Juanita',
        'Drobish',
        'Fran',
        'Reed',
        'Shannon',
        'Zantello',
        'Hoag',
        'Margaret',
        'Vollenweider',
        'Ronald',
        'Haag',
        'JON',
        'SCHUMACHER',
        'Terrilyn',
        'Hannan',
        'Cleta',
        'White',
        'Erin',
        'Morgan',
        'Kelly',
        'Rouse',
        'Kerri',
        'Coleman',
        'Arthur',
        'Welch',
        'Amy',
        'Brown',
        'Yoohwan',
        'Hwang',
        'Hayes',
        'Carolyn',
        'Allen',
        'McKay',
        'Rehwinkel',
        'Jennifer',
        'Hoyle',
        'Laura',
        'Doty',
        'Francis',
        'Rodwig',
        'Nikki',
        'Deblieux',
        'Leigh',
        'McCann',
        'Carol',
        'Tannehill',
        'Candi',
        'Starner',
        'Dustin',
        'Rathcke',
        'Patty',
        'Singley',
        'Julie',
        'Stoelting',
        'Ben',
        'Harding',
        'Shanon',
        'Naquin',
        'Crader',
        'Michelle',
        'Yenni',
        'Whitney',
        'Temonia',
        'Helen',
        'Walsh',
        'William',
        'Scullin',
        'Sherry',
        'Anita',
        'Humphreys',
        'Ruth',
        'Barone',
        'Christopher',
        'Guidry',
        'Emily',
        'Eason',
        'Overman'
    )
    __adress = (
        (
            '2046 Kinsmon Drive',
            'Marietta',
            'Georgia',
            '30062',
            'GA',
            '19','3631','18','9'),
        (
            '711 Grand Lakes Drive',
            'Baton Rouge',
            'Louisiana',
            '70810',
            'LA',
            '28','3640','27','18'),
        (
            '9021 Alder Drive',
            'Baton Rouge',
            'Louisiana',
            '70817',
            'LA',
            '28','3640','27','18'),
        (
            '904 Blair Crossing',
            'Shreveport',
            'Louisiana',
            '71111',
            'LA',
            '28','3640','27','18'),
        (
            '13037 Triple B',
            'Greenwell Springs',
            'Louisiana',
            '70739',
            'LA',
            '28','3640','27','18'),
        (
            '2907 Kassarine Pass',
            'Austin',
            'Texas',
            '78704',
            'TX',
            '57','3669','65','43'),
        (
            '10157 Widdington Close',
            'Powell',
            'Ohio',
            '43065',
            'OH',
            '47',
            '3659',
            '51',
            '35'
        ),
        (
            '11580 Forest Lake DR',
            'Rolla',
            'Missouri',
            '65401',
            'MO',
            '36','3648','24','24'),
        (
            '2900 hunters rdige road',
            'marion',
            'Iowa',
            '52302',
            'IA',
            '25','3637','21','12'),
        (
            '6851 s central ave',
            'phoenix',
            'Arizona',
            '85042',
            'AZ',
            '4','3616','9','4'),
        (
            '2305 Acadienne',
            'Sulphur',
            'Louisiana',
            '70663',
            'LA',
            '28','3640','27','18'),
        (
            '102 Arline Ct',
            'Montz',
            'Louisiana',
            '70068',
            'LA',
            '28','3640','27','18'),
        (
            '100 Adclare Rd.',
            'Rockville',
            'Maryland',
            '20850',
            'MD',
            '31','3643','30','20'),
        (
            '58047 Churchill RD',
            'Slidell',
            'Louisiana',
            '70460',
            'LA',
            '28','3640','27','18'),
        (
            '5012 Willow Tree Rd.',
            'Marrero',
            'Louisiana',
            '70072',
            'LA',
            '28','3640','27','18'),
        (
            '1003 Scottland Dr',
            'Murfreesboro',
            'Tennessee',
            '37130',
            'TN',
            '56','3668','64','42'),
        (
            '601 Short Street',
            'Greensburg',
            'Pennsylvania',
            '15601',
            'PA',
            '51','3663','55','38'),
        (
            '303 E 8th Ave.',
            'Covington',
            'Louisiana',
            '70433',
            'LA',
            '28','3640','27','18'),
        (
            '250 w Greenway st',
            'Derby',
            'Kansas',
            '67037',
            'KS',
            '26','3638','25','15'),
        (
            '7023 East Caprice Ave',
            'Baton Rouge',
            'Louisiana',
            '70811',
            'LA',
            '28','3640','27','18'),
        (
            '2682 goodfellows rd',
            'Tucker',
            'Georgia',
            '30084',
            'GA',
            '19','3631','18','10'),
        (
            '11959 Nicholson Drive',
            'Baton Rouge',
            'Louisiana',
            '70180',
            'LA',
            '28','3640','27','18'),
        (
            '109 Defiance Drive',
            'Slidell',
            'Louisiana',
            '70458',
            'LA',
            '28','3640','27','18'),
        (
            '1302 W Crocker St',
            'Sulphur',
            'Louisiana',
            '70663',
            'LA',
            '28','3640','27','18'),
        (
            '9018 Jefferson Hwy',
            'Baton Rouge',
            'Louisiana',
            '70809',
            'LA',
            '28','3640','27','18'),
        (
            '19119 Poujeaux Avenue',
            'Baton Rouge',
            'Louisiana',
            '70817',
            'LA',
            '28','3640','27','18'),
        (
            '5372 Grey Stag Court',
            'Suwanee',
            'Georgia',
            '30024',
            'GA',
            '19','3631','18','10'),
        (
            '8355 Barnett Drive',
            'Baton Rouge',
            'Louisiana',
            '70809',
            'LA',
            '28','3640','27','18'),
        (
            '1725 Swan Drive',
            'Lake Charles',
            'Louisiana',
            '70605',
            'LA',
            '28','3640','27','18'),
        (
            '1220 Vista Jardin',
            'San Clemente',
            'California',
            '92673',
            'CA',
            '12','3624','11','5'),
        (
            '9302 Hilltrace Avenue',
            'Baton Rouge',
            'Louisiana',
            '70809',
            'LA',
            '28','3640','27','18'),
        (
            '212 B Yvonne Street',
            'Broussard',
            'Louisiana',
            '70518',
            'LA',
            '28','3640','27','18'),
        (
            '1195 A T and T Tower Road',
            'Saint Landry',
            'Louisiana',
            '71367',
            'LA',
            '28','3640','27','18'),
        (
            '6234 Durande Dr',
            'Baton Rouge',
            'Louisiana',
            '70820',
            'LA',
            '28','3640','27','18'),

        (
            '10001 Six Pines Dr',
            'The Woodlands',
            'Texas',
            '77380',
            'TX',
            '57','3669','65','43'),
        (
            '214 Glenn St.',
            'Broussard',
            'Louisiana',
            '70518',
            'LA',
            '28','3640','27','18'),
        (
            '4301 Lake Michigan Drive',
            'Corpus Christi',
            'Texas',
            '78413',
            'TX',
            '57','3669','65','43'),
        (
            '373 Lexington St',
            'Auburndale',
            'Massachusetts',
            '02466',
            'MA',
            '32','3644','28','19'),
        (
            '45 Georgian Way',
            'Weston',
            'Massachusetts',
            '02493',
            'MA',
            '32','3644','28','19'),
        (
            '1416 Circle Ln',
            'Bedford',
            'Texas',
            '76022',
            'TX',
            '57','3669','65','43'),
        (
            '760 Robert E Lee',
            'New Orleans',
            'Louisiana',
            '70124',
            'LA',
            '28','3640','27','18'),
        (
            '9118 rue de vieux carre',
            'denham springs',
            'Louisiana',
            '70706',
            'LA',
            '28','3640','27','18'),
        (
            '3911 Hartzdale Drive',
            'Camp Hill',
            'Pennsylvania',
            '17011',
            'PA',
            '51','3663','55','38'),
        (
            '75 Fairmount Road West',
            'Califon',
            'New Jersey',
            '07830',
            'NJ',
            '41','3653','45','30'),
        (
            '2018 Tennessee Rd',
            'Durham',
            'North Carolina',
            '27704',
            'NC',
            '44','3656','40','27'),
        (
            '2108 Oakmont St',
            'Monroe',
            'Louisiana',
            '71201',
            'LA',
            '28','3640','27','18'),
        (
            '1726 The Woods Drive',
            'El Cajon',
            'California',
            '92019',
            'CA',
            '12','3624','11','5'),
        (
            '6515 Bandera Ave 1A',
            'Dallals',
            'Texas',
            '75225',
            'TX',
            '57','3669','65','43'),
        (
            '141 Normandy circle',
            'Madison',
            'Mississippi',
            '39110',
            'MS',
            '35','3647','37','25'),
        (
            '4509 Palatine Ave N',
            'Seattle',
            'Washington',
            '98103',
            'WA',
            '62','3674','70','47'),
        (
            '4806 Sundance Hollow lane',
            'katy',
            'Texas',
            '77494',
            'TX',
            '57','3669','65','43'),
        (
            '38211 Bullion Switch Rd',
            'Prairieville',
            'Louisiana',
            '70769',
            'LA',
            '28','3640','27','18'),
        (
            '6222 S. Saddlecreek Lane',
            'Fulshear',
            'Texas',
            '77441',
            'TX',
            '57','3669','65','43'),
        (
            '312 Field Crest Pkwy',
            'Youngsville',
            'Louisiana',
            '70592',
            'LA',
            '28','3640','27','18'),
        (
            '1230 W. Peachtree St.',
            'Atlanta',
            'Georgia',
            '30309',
            'GA',
            '19','3631','18','10'),
        (
            '518 Castle Kirk Drive',
            'Baton Rouge',
            'Louisiana',
            '70808',
            'LA',
            '28','3640','27','18'),
        (
            '6146 Shakespeare Dr',
            'Baton Rouge',
            'Louisiana',
            '70817',
            'LA',
            '28','3640','27','18'),
        (
            '826 Focis Street',
            'Metairie',
            'Louisiana',
            '70005',
            'LA',
            '28','3640','27','18'),
        (
            '302 Cedar Tree Drive',
            'Thibodaux',
            'Louisiana',
            '70301',
            'LA',
            '28','3640','27','18'),
        (
            '209 Country Estates Drive',
            'Houma',
            'Louisiana',
            '70364',
            'LA',
            '28','3640','27','18'),
        (
            '708 Aberdeen Dr.',
            'lafayette',
            'Louisiana',
            '70508',
            'LA',
            '28','3640','27','18'),
        (
            '4713 Timberhill Court',
            'Nashville',
            'Tennessee',
            '37211',
            'TN',
            '56','3668','64','42'),
        (
            '7575 Sherwood Hwy',
            'Bellevue',
            'Michigan',
            '49021',
            'MI',
            '33','3645','33','22'),
        (
            '2525 Stubbs Vinson Road',
            'Monroe',
            'Louisiana',
            '71203',
            'LA',
            '28','3640','27','18'),
        (
            '1223 Sanders St',
            'Auburn',
            'Alabama',
            '36830',
            'AL',
            '1','3613','5','2'),
        (
            '4600 Beau Lac Lane',
            'Metairie',
            'Louisiana',
            '70002',
            'LA',
            '28','3640','27','18'),
        (
            '10961 Pleasant Hill Cir',
            'Sandy',
            'Utah',
            '84092',
            'UT',
            '58','3670','66','44'),
        (
            '17523 Beachwood Ave',
            'Baton Rouge',
            'Louisiana',
            '70817',
            'LA',
            '28','3640','27','18'),
        (
            '278 Elliot Road',
            'West Monroe',
            'Louisiana',
            '71292',
            'LA',
            '28','3640','27','18'),
        (
            '2942 e 94th street',
            'Tulsa',
            'Oklahoma',
            '74137',
            'OK',
            '48','3660','52','36'),
        (
            '230 South Grand Avenue',
            'Pasadena',
            'California',
            '91105',
            'CA',
            '12','3624','11','5'),
        (
            '12448 heversham avenue',
            'baton rouge',
            'Louisiana',
            '70810',
            'LA',
            '28','3640','27','18'),
        (
            '60 sunrise mesa dr',
            'canon city',
            'Colorado',
            '81212',
            'CO',
            '13','3625','12','6'),
        (
            '3316 Vine Ridge',
            'Bedford',
            'Texas',
            '76021',
            'TX',
            '57','3669','65','43'),
        (
            '29211 Red Willow Dr',
            'Denham Springs',
            'Louisiana',
            '70726',
            'LA',
            '28','3640','27','18'),
        (
            '158 Mary Ellen Drive',
            'Charleston',
            'South Carolina',
            '29403',
            'SC',
            '54','3666','61','40'),
        (
            '919 W. King Street',
            'Quincy',
            'Florida',
            '32351',
            'FL',
            '18','3630','16','9'),
        (
            '1899 Baytowne Loop',
            'Miramar Beach',
            'Florida',
            '32550',
            'FL',
            '18','3630','16','9'),
        (
            '36033 Eaton Drive',
            'Clinton Twp',
            'Michigan',
            '48035',
            'MI',
            '33','3645','33','22'),
        (
            '3632 Inwood ave',
            'new Orlean',
            'Louisiana',
            '70131',
            'LA',
            '28','3640','27','18'),
        (
            '15021 Dendinger Drive',
            'Covington',
            'Louisiana',
            '70433',
            'LA',
            '28','3640','27','18'),
        (
            '1000 Rue Royal',
            'New Orleans',
            'Louisiana',
            '70116',
            'LA',
            '28','3640','27','18'),
        (
            '20526 E. Maplewood Pl.',
            'Centennial',
            'Colorado',
            '80016',
            'CO',
            '13','3625','12','6'),
        (
            '2305 Bocage Place',
            'ruston',
            'Louisiana',
            '71270',
            'LA',
            '28','3640','27','18'),
        (
            '185 s curtis ave',
            'pea ridge',
            'Arkansas',
            '72751',
            'AR',
            '5','3617','7',"3"),
        (
            '17332 Roble Avenue',
            'Greenwell Springs',
            'Louisiana',
            '70739',
            'LA',
            '28','3640','27','18'),
        (
            '1201 Cook Road',
            'Delhi',
            'Louisiana',
            '71232',
            'LA',
            '28','3640','27','18'),
        (
            '4040 Vincennes Circle',
            'Indianapolis',
            'Indiana',
            '46268',
            'IN',
            '24',
            '3636','24','15'),
        (
            '500 Taylor',
            'Columbia',
            'South Carolina',
            '29201',
            'SC',
            '54','3666','61','40'),
        (
            '2801 south miltary hwy',
            'chesapeake',
            'Virginia',
            '23323',
            'VA',
            '61',
            '3673','67','45'),
        (
            '14402 Laumar Ct.',
            'Cypress',
            'Texas',
            '77429',
            'TX',
            '57','3669','65','43'),
        (
            '3600 Chateau Blvd.',
            'Kenner',
            'Louisiana',
            '70065',
            'LA',
            '28','3640','27','18'),
        (
            '9142 S. Weatherstone Ct.',
            'Highlands Ranch',
            'Colorado',
            '80126',
            'CO',
            '13','3625','12','6'),
        (
            '13513 Kimble Avenue',
            'Baton Rouge',
            'Louisiana',
            '70810',
            'LA',
            '28','3640','27','18'),
        (
            '7535 Torrey santa fe road',
            'San Diego',
            'California',
            '92129',
            'CA',
            '12','3624','11','5'),
        (
            '23 W Oakley Dr N Apt 202',
            'Westmont',
            'Illinois',
            '60559',
            'IL',
            '23',
            '3635','23','14'),
        (
            '230 Greenway Avenue',
            'Satellite Beach',
            'Florida',
            '32937',
            'FL',
            '18','3630','16','9'),
        (
            '2609 E. Aster Dr.',
            'Phoenix',
            'Arizona',
            '85032',
            'AZ',
            '4','3616','9','4'),
        (
            '9934 lee circle',
            'leawood',
            'Kansas',
            '66206',
            'KS',
            '26','3638','25','15'),
        (
            '21052 Berry Glen',
            'Lake Forest',
            'California',
            '92630',
            'CA',
            '12','3624','11','5'),
        (
            '404 Oxford St. 1301',
            'Houston',
            'Texas',
            '77007',
            'TX',
            '57','3669','65','43'),
        (
            '6740 Tylersville Road',
            'West chester',
            'Ohio',
            '45069',
            'OH',
            '47',
            '3659',
            '51',
            '35'
        )
    )
    __adressInfo = None
    nameFirs = None
    nameLast = None
    nameLast2 = None
    phone1 = None 
    phone2 = None
    address = None
    city = None
    estado = None
    estado2 = None
    estado3 = None
    estado4 = None
    estado5 = None
    estado6 = None
    zipcode = None
    emailx = None
    
    def __init__(self):
        self.__adressInfo = self.__adress[randint(0,len(self.__adress) - 1)]
        self.nameFirs = self.__name[randint(0,(len(self.__name) -1)/2 )]
        self.nameLast = self.__name[randint((len(self.__name) -1)/2 + 1, len(self.__name) -2)]
        self.nameLast2 = self.__name[randint((len(self.__name) -1)/2 + 1, len(self.__name) -2)]
        self.phone1 =  f'{randint(100,999)}{randint(100,999)}{randint(1000,9999)}'
        self.phone2 =  f'{randint(100,999)}-{randint(100,999)}-{randint(1000,9999)}'
        self.address = self.__adressInfo[0]
        self.city = self.__adressInfo[1]
        self.zipcode = self.__adressInfo[3]
        self.estado = self.__adressInfo[2]
        self.estado2 = self.__adressInfo[4]
        self.estado3 = self.__adressInfo[5]
        self.estado4 = self.__adressInfo[6]
        self.estado5 = self.__adressInfo[7]
        self.estado6 = self.__adressInfo[8]
        self.emailx = self.nameFirs+str(randint(1,10000))+self.nameLast+str(randint(1,20000))