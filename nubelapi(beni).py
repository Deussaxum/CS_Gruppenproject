import requests
import json 

api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/benjamin-david-auer/',
}
#comment next three lines when testing
response = requests.get(api_endpoint,
                       params=params,
                       headers=headers)

def extract_info(jsondata):

    # Set default values to Not available
    extracted_info = {
        'full_name': 'Not available',
        'city':'Not available',
        'experiences': [],
        'birth_date': [],
        'personal_emails': [],
        'education': []
    }

    # Replace values if found in response
    if "full_name" in jsondata:
        extracted_info["full_name"] = jsondata["full_name"]
    
    if "city" in jsondata:
        extracted_info["city"]  = jsondata["city"]

    if "birth_date" in jsondata:
        extracted_info["birth_date"]  = jsondata["birth_date"]

    if "personal_emails" in jsondata:
        extracted_info["personal_emails"] = jsondata["personal_emails"]

    if "experiences" in jsondata:
        for experience in jsondata["experiences"]:
            extracted_info['experiences'].append({
                'title': experience["title"],
                'company': experience["company"],
                'description': experience["description"]
            })

    if "education" in jsondata:
        for educations in jsondata ["education"]:
            extracted_info['education'].append({
                'school': educations ["school"],
                'degree_name': educations ["degree_name"],
                'field_of_study': educations["field_of_study"]
             })
    return extracted_info 
# Check if the response was successful
if response.status_code == 200:
    jsondata = response.json()
    # Call the extract_info function with the JSON data
    extracted_info = extract_info(jsondata)
    # Print the extracted information - Correct place to put the print function
    print(extracted_info)
else:
    print("Error: Unable to fetch data. Status code:", response.status_code)
# Print or process the extracted information
##extracted_info = extract_info(jsondata)
##print(extracted_info)   

#below is just for testing to save API Credits
# Parse the JSON data if api_response is a JSON string
# api_response = json.loads(api_response)

# Extract information

#extracted_info = extract_info(response.json())

# Remove the next two lines (or comment out) when running API queries
#testdata = {'public_identifier': 'gabrielsherrera', 'profile_pic_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/person/gabrielsherrera/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20231205%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20231205T221643Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=a760d1aaf3ca4bf04230d73cfa0d163c8ada7b6c6b49479c62683ee4b5397b0d', 'background_cover_image_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/person/gabrielsherrera/cover?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20231205%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20231205T221643Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=579eb13181c19b644f1e67d0371d588e78ef8002bf4892b0388d582dc1043128', 'first_name': 'Gabriel', 'last_name': 'Herrera', 'full_name': 'Gabriel Herrera', 'follower_count': 2059, 'occupation': 'Global Director of Technical Solutions at Frontify', 'headline': 'Connecting commercial and product teams @ Frontify | Director of Technical Solutions', 'summary': 'Holding a combination of international experience and technical knowledge, I find myself at my best in the interface of technology and people. A problem solver by nature and always hungry for new challenges. Constantly seeking to improve through new hobbies, experiences and training.', 'country': 'CZ', 'country_full_name': 'Czech Republic', 'city': 'Prague', 'state': None, 'experiences': [{'starts_at': {'day': 1, 'month': 1, 'year': 2021}, 'ends_at': None, 'company': 'Catapult International', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/catapult-international/', 'title': 'Advisor', 'description': 'Catapult equips corporates across Europe and North-America with data-driven research about the tech market, best tech innovations, competitor insights, fastest growing verticals, CVC etc. Combining data on 1M+ tech companies with AI/ML, NLP and manual validation in either a full service research offering or a SaaS research platform.', 'location': 'Prague, Czechia', 'logo_url': 'https://media.licdn.com/dms/image/C560BAQHkZh3jDJ9KWw/company-logo_400_400/0/1560842190606/startup_catapult_logo?e=1706140800&v=beta&t=3ETKTfnrwyg2pj0S4ogQDUI1P_HByMLT9u4vUCcuR8Y'}, {'starts_at': {'day': 1, 'month': 4, 'year': 2021}, 'ends_at': {'day': 31, 'month': 12, 'year': 2021}, 'company': 'Catapult International', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/catapult-international/', 'title': 'Product Lead - Innopipe', 'description': "Innopipe is a single platform leveraging AI and Machine learning to Discover, Manage and Take Action on tech companies and innovations - no matter if the goal is investment, acquisition, market research, competitor analysis or other.\n\nAs the Product Lead I marry our founders' vision for the platform and customer needs and translate those into a prioritised product backlog. This includes working closely with customers, sales enablement work and building functional prototypes to test assumptions. I also continue as a practical advisor in marketing and business strategy, as well as team building and recruiting.", 'location': 'Prague, Czechia', 'logo_url': 'https://media.licdn.com/dms/image/C560BAQHkZh3jDJ9KWw/company-logo_400_400/0/1560842190606/startup_catapult_logo?e=1706140800&v=beta&t=3ETKTfnrwyg2pj0S4ogQDUI1P_HByMLT9u4vUCcuR8Y'}, {'starts_at': {'day': 1, 'month': 10, 'year': 2021}, 'ends_at': None, 'company': 'Clarisights', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/clarisights/', 'title': 'Advisor', 'description': 'Clarisights streamlines reporting for sophisticated performance marketing teams. It automatically integrates, processes and visualises all data from marketing, analytical and attribution sources.', 'location': 'Berlin, Germany', 'logo_url': 'https://media.licdn.com/dms/image/C4E0BAQGtrvMXhoGAFw/company-logo_400_400/0/1566479385828/clarisights_logo?e=1706140800&v=beta&t=DUJkA781VW8qVS1KkLH3Ec8hViwvQaUeX1legq-boVY'}, {'starts_at': {'day': 1, 'month': 1, 'year': 2022}, 'ends_at': None, 'company': 'Frontify', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/frontify/', 'title': 'Global Director of Technical Solutions', 'description': 'My task has been to create commercial support functions and processes to enable faster and larger deals, as well as providing faster onboarding for new customers. This has led to the development of three teams:\n1. Technical Solutions Consultanting, akin to Sales Engineers, but with a high focus on enablement and also existing customers\n2. Solutions Engineering, whom manage highly technical requirements and various integration development \n3. Professional Services, responsible for providing internal and external services to facilitate sales, training and customer onboarding.', 'location': 'Prague, Czechia', 'logo_url': 'https://media.licdn.com/dms/image/C560BAQGXnWxj3ILj-w/company-logo_400_400/0/1670601880617/frontify_logo?e=1706140800&v=beta&t=ZUy8ibWfMYkboBSqqN-8971CMCextw2ojQS6U0E5cok'}, {'starts_at': {'day': 1, 'month': 4, 'year': 2020}, 'ends_at': {'day': 31, 'month': 3, 'year': 2021}, 'company': 'Smartly.io', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/smartly-io/', 'title': 'Global Director of Technical Solutions', 'description': 'Running teams across the globe of both technically and commercially talented individuals focused on solving current and future customers’ problems and build trust in our product our team, through providing technical solutions and guidance. Efforts focus on\n- Product and needs discovery\n- Scoping and solution design\n- Process and product management\n- Supporting new platform development and roll-out\n- Custom solution development\n- Bridging commercial and technical organizations', 'location': 'New York, United States & Prague, Czech Republic', 'logo_url': 'https://media.licdn.com/dms/image/C4D0BAQH1cZk12xQwbw/company-logo_400_400/0/1678452092522/smartly_io_logo?e=1706140800&v=beta&t=knrHHQwwI516QxX4L_1Sg360rAVGHTGkaYfRP0o-wNg'}, {'starts_at': {'day': 1, 'month': 3, 'year': 2018}, 'ends_at': {'day': 30, 'month': 4, 'year': 2020}, 'company': 'Smartly.io', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/smartly-io/', 'title': 'General Manager Americas', 'description': "As the General Manager, I worked on a variety of responsibilities, including:\n- Business development\n- Recruiting\n- Key customer acquisition\n- Partnership management\n- Customer and stakeholder relationships\n- Marketing co-ordination\n- Co-ordinating product feedback\n- Internal training and knowledge management\n\nDirect responsibilities spanned 5 offices and over 60 people across 3 countries. A key focus area in this role was about building a pioneering sales team and strengthening the sales culture at Smartly.io, with the goal of scaling our business, team and operations in the Americas, while maintaining the essence of Smartly.io's values and culture.", 'location': 'New York, United States', 'logo_url': 'https://media.licdn.com/dms/image/C4D0BAQH1cZk12xQwbw/company-logo_400_400/0/1678452092522/smartly_io_logo?e=1706140800&v=beta&t=knrHHQwwI516QxX4L_1Sg360rAVGHTGkaYfRP0o-wNg'}, {'starts_at': {'day': 1, 'month': 10, 'year': 2015}, 'ends_at': {'day': 31, 'month': 3, 'year': 2018}, 'company': 'Smartly.io', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/smartly-io/', 'title': 'Head of LatAm', 'description': "Social media platforms like Facebook are disrupting advertising at record pace. Keeping up with the change and developing solutions to bring more value in it is a challenge we at Smartly gladly accept. We're motivated by facing problems we don't have solutions to, invigorated by the road to find those and thrilled by the success of innovative solutions.\n\nThis has made Smartly.io the worlds leading Facebook Marketing Partner with offices on 4 continents, a 400+ person headcount and over 30 nationalities. More than a platform, our service offers large scale performance marketers and media agencies tools for managing, optimizing and automating large-scale social advertising accounts, all with the world's best support, because it's all about the clients at the end of the day.\n\nAs the head of a market I facilitate for a team of the most talented people I know in market development and new customer acquisition, maintaining and developing existing customer relationships, training, recruiting, scaling results and contributing to product and business development on daily basis.", 'location': 'San Francisco, United States & New York, United States', 'logo_url': 'https://media.licdn.com/dms/image/C4D0BAQH1cZk12xQwbw/company-logo_400_400/0/1678452092522/smartly_io_logo?e=1706140800&v=beta&t=knrHHQwwI516QxX4L_1Sg360rAVGHTGkaYfRP0o-wNg'}, {'starts_at': {'day': 1, 'month': 2, 'year': 2013}, 'ends_at': {'day': 31, 'month': 10, 'year': 2015}, 'company': 'Monikulttuurisuuden edistämisyhdistys Walter ry', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/monikulttuurisuuden-edist-misyhdistys-walter-ry/', 'title': 'Project Co-ordinator (KYTKE-project)', 'description': 'Walter assoc. is a Finnish non-profit organization that does anti-discrimination work by furthering intercultural communication and interaction, especially with children and youths. \n\nKey tasks under my responsibility included to create and develop educational and promotional materials and strategies, run Research and Analysis, Heading Mediation, Community management, Building up and maintaining information systems, Technical administration and establishing fundraising for future years.\n\nOther: holding workshops, peer support, teaching, representing Walter assoc. at events.', 'location': 'Helsinki, Finland', 'logo_url': 'https://media.licdn.com/dms/image/C4E0BAQHaGSuviVcCRA/company-logo_400_400/0/1519895445827?e=1706140800&v=beta&t=f7Ui0L0by8TY0wVbTfcmoYEg1VG403RO6KjSXSQAAjo'}, {'starts_at': {'day': 1, 'month': 3, 'year': 2013}, 'ends_at': {'day': 31, 'month': 1, 'year': 2015}, 'company': 'StartHQ', 'company_linkedin_profile_url': None, 'title': 'Co-Founder / COO', 'description': 'A starting point for YOUR web with search across all web services, instant access to functions and operations and strong customizability with every new tab. Including a directory of business SaaS services. In stealth mode, after a good, nearly 2 year run full of great experience. E.g. was a Startup Sauna winner and Arctic startup top 30 company.', 'location': 'Helsinki, Finland', 'logo_url': None}, {'starts_at': {'day': 1, 'month': 7, 'year': 2007}, 'ends_at': {'day': 29, 'month': 2, 'year': 2012}, 'company': 'Taksi Kari Järvinen Oy', 'company_linkedin_profile_url': None, 'title': 'Logistics Manager, Driver and Liquidator', 'description': 'Part time during university studies. Taxi company where I worked first as a driver, later a logistics manager when my employer became seriously ill and finally a liquidator after his passing away.\n\nImplemented all aspects of a controlled liquidation of the company making sure all the employees and stock holders were satisfied with the result.', 'location': 'Tampere Area, Finland', 'logo_url': None}, {'starts_at': {'day': 1, 'month': 1, 'year': 2009}, 'ends_at': {'day': 31, 'month': 12, 'year': 2009}, 'company': 'Student Union of University of Tampere', 'company_linkedin_profile_url': None, 'title': 'Director of International Affairs, Development Co-operation and Information Technology', 'description': 'Full time position. Major themes: the implementation of the new university law in Finland and addressing the housing situation of new students.\n\nSome accomplishments: Together with the secretary for international affairs, increased development co-operation funds by 150% while actually lowering costs through a project restructure. Restructuring data management and network upgrading resulted in savings and increased connectivity.', 'location': 'Tampere, Finland', 'logo_url': 'https://media.licdn.com/dms/image/C560BAQEKvZNwQE9veg/company-logo_400_400/0/1519884313006?e=1706140800&v=beta&t=UjnNjWf9kcxczh4Y-JIT48XH7vP2_j9vuh8GMb15OhE'}, {'starts_at': {'day': 1, 'month': 5, 'year': 2007}, 'ends_at': {'day': 31, 'month': 8, 'year': 2009}, 'company': 'Finnish Summer High School Association', 'company_linkedin_profile_url': None, 'title': 'Course designer and instructor', 'description': 'Planning, preparing and implementing, by request, two-day intensive courses on conflict resolution (2007) and Latin American culture (2008 & 2009). The conflict resolution course was done as a joint effort with an International Relations researcher from the University of Tampere and the Latin American culture courses were fully my own.\n\nThe courses included interactive teaching, immersive exercises, creative thinking tasks and simulations. They were aimed at high-school level students and to be challenging for them. All material was prepared specifically for the courses. Teaching languages were Finnish and English and the material was made available in both.', 'location': 'Helsinki, Finland', 'logo_url': None}, {'starts_at': {'day': 1, 'month': 5, 'year': 2012}, 'ends_at': {'day': 28, 'month': 2, 'year': 2013}, 'company': 'Mobile Backstage', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/mobile-backstage/', 'title': 'Community & Product Manager', 'description': "Provided insights and statistics from fan communities of 150 000 users + monitoring and moderation. Product Manager for the development and implementation of a web dashboard and Fan Club service and developed testing procedures focusing on usability and user experience, while overseeing Quality Assurance.\n\nMobile Backstage connects fans to artists, artists to fans and fans to each other in new and exciting ways. The company is listed as one of WIRED magazines: Europe's 100 Hottest Startups 2012.", 'location': 'Helsinki, Finland', 'logo_url': 'https://media.licdn.com/dms/image/C4D0BAQElX1K9uOx2CQ/company-logo_400_400/0/1519914348845?e=1706140800&v=beta&t=fu98cbGKz6TTNIqcEy29vhnGPXb6l1jqwjG6fLtzdPQ'}], 'education': [{'starts_at': {'day': 1, 'month': 1, 'year': 2003}, 'ends_at': {'day': 31, 'month': 1, 'year': 2012}, 'field_of_study': 'International Relations', 'degree_name': 'Master of Social Sciences', 'school': 'University of Tampere 1925-2018', 'school_linkedin_profile_url': None, 'description': None, 'logo_url': 'https://media.licdn.com/dms/image/C560BAQEKvZNwQE9veg/company-logo_400_400/0/1519884313006?e=1706140800&v=beta&t=UjnNjWf9kcxczh4Y-JIT48XH7vP2_j9vuh8GMb15OhE', 'grade': None, 'activities_and_societies': None}, {'starts_at': {'day': 1, 'month': 1, 'year': 2014}, 'ends_at': None, 'field_of_study': 'Computer Science', 'degree_name': 'Dropped with missing final year: Bachelor of Business Administration (B.B.A.)', 'school': 'Haaga-Helia University of Applied Sciences', 'school_linkedin_profile_url': None, 'description': None, 'logo_url': 'https://media.licdn.com/dms/image/D4D0BAQEmUoNq8aXGUw/company-logo_400_400/0/1688724573438/haaga_helia_university_of_applied_sciences_logo?e=1706140800&v=beta&t=lQnqqD7jQf5PDyTyxabSoVtemDf2g5xAmMuhXDEDHFo', 'grade': None, 'activities_and_societies': None}, {'starts_at': {'day': 1, 'month': 1, 'year': 2002}, 'ends_at': {'day': 31, 'month': 1, 'year': 2003}, 'field_of_study': 'Mortar & Antitank missile', 'degree_name': 'Reserve Officer - Rapid Deployment Force', 'school': 'Finnish Defence Forces', 'school_linkedin_profile_url': None, 'description': None, 'logo_url': None, 'grade': None, 'activities_and_societies': None}, {'starts_at': {'day': 1, 'month': 1, 'year': 1998}, 'ends_at': {'day': 31, 'month': 1, 'year': 2001}, 'field_of_study': 'International Baccalaureate', 'degree_name': 'High school graduate', 'school': 'Tampere Lyceum High School', 'school_linkedin_profile_url': None, 'description': None, 'logo_url': None, 'grade': None, 'activities_and_societies': None}], 'languages': ['English', 'Finnish', 'French', 'Portuguese', 'Spanish', 'Swedish'], 'accomplishment_organisations': [], 'accomplishment_publications': [], 'accomplishment_honors_awards': [], 'accomplishment_patents': [], 'accomplishment_courses': [{'name': 'Entrepreneurship course - Tampere College, 2011', 'number': None}, {'name': 'Startup accelerator - Startup Sauna, 2013', 'number': None}], 'accomplishment_projects': [{'starts_at': {'day': 1, 'month': 1, 'year': 2013}, 'ends_at': {'day': 31, 'month': 3, 'year': 2013}, 'title': 'StartHQ', 'description': "The project included collecting information on the problems various types of organizations face when using webapps and design a solution for them. Ongoing research is conducted to test each solution's effectiveness, following lean start-up methodology. Conclusion: the use of SaaS is constantly increasing, yet there are no good tools to discover, organize and manage them => StartHQ founded.", 'url': None}], 'accomplishment_test_scores': [], 'volunteer_work': [{'starts_at': {'day': 1, 'month': 1, 'year': 2009}, 'ends_at': {'day': 31, 'month': 12, 'year': 2010}, 'title': 'Chairman of the committee', 'cause': None, 'company': 'Tampere ylioppilastalo foundation', 'company_linkedin_profile_url': None, 'description': 'The committee uses the highest decisive power in the foundation, which takes care of the property at Kauppakatu 10, Tampere. E.g. it decides on the budget and elects the board.', 'logo_url': None}, {'starts_at': {'day': 1, 'month': 1, 'year': 2008}, 'ends_at': {'day': 31, 'month': 12, 'year': 2011}, 'title': 'Committee member, deputy board member', 'cause': None, 'company': 'Tampere Student Housing Foundation', 'company_linkedin_profile_url': None, 'description': "The committee uses the highest decisive power in the foundation, charged with supplying accommodation to students. E.g. it decides on the budget and elects the board, which in turn decides on the best implementation of the committee's wishes.", 'logo_url': None}, {'starts_at': {'day': 1, 'month': 1, 'year': 2008}, 'ends_at': {'day': 31, 'month': 12, 'year': 2010}, 'title': 'Co-founder, Chairperson, Vice-Chairperson', 'cause': None, 'company': 'Erasmus Student Network Finns and Internationals in Tampere ry. - ESN FINT Association', 'company_linkedin_profile_url': None, 'description': "Main tasks: co-ordinating activities, planning and establishment of independent association, maintaining and improving accounts and finances, business co-operation with local partners, negotiating contracts and agreements. Additionally I was in charge of creating the accounting procedures and handling accounting for the first year of the new registered association and implementing the first Drupal-based website for the association. I was also instrumentally involved in the planning, creating, marketing and development of the Club Xchange party (www.clubxchange.org) concept that accounts for the major part of the association's fundraising.\n\nThe association belongs to the European wide Erasmus Student Network and takes actively part in it's different levels. It grew to be the largest registered international student organization in Tampere.", 'logo_url': None}], 'certifications': [{'starts_at': {'day': 1, 'month': 5, 'year': 2023}, 'ends_at': {'day': 31, 'month': 5, 'year': 2027}, 'name': 'MEDDPICC Masterclass', 'license_number': 'maxinhywgm', 'display_source': 'meddicc.com', 'authority': 'MEDDICC', 'url': 'https://learn.meddicc.com/certificates/maxinhywgm'}, {'starts_at': {'day': 1, 'month': 3, 'year': 2016}, 'ends_at': {'day': 31, 'month': 3, 'year': 2018}, 'name': 'Facebook Blueprint ', 'license_number': '38500455', 'display_source': 'facebook.com', 'authority': 'Meta', 'url': 'https://www.facebook.com/blueprint'}, {'starts_at': {'day': 1, 'month': 10, 'year': 2020}, 'ends_at': {'day': 31, 'month': 10, 'year': 2022}, 'name': 'Snapchat Advertising Essentials', 'license_number': '146796407', 'display_source': 'snapchat.com', 'authority': 'Snap Inc.', 'url': 'https://forbusiness.snapchat.com/resources/snapfocus'}], 'connections': None, 'people_also_viewed': [{'link': 'https://www.linkedin.com/in/okkomakijarvi', 'name': 'Okko Mäkijärvi', 'summary': 'Lead Solution Consultant', 'location': None}, {'link': 'https://www.linkedin.com/in/terho-laakkonen-32315a85', 'name': 'Terho Laakkonen', 'summary': 'Solutions Engineering @ Clarisights', 'location': None}, {'link': 'https://www.linkedin.com/in/daniel-kaestli', 'name': 'Daniel Kästli', 'summary': 'Founder and Customer Success Leader', 'location': None}, {'link': 'https://www.linkedin.com/in/andreytalalaev', 'name': 'Andrey Talalaev', 'summary': 'Digital Marketing & Paid Social Expert 🤳 Customer Success with RevOps Mindset 👨\u200d💻', 'location': None}, {'link': 'https://www.linkedin.com/in/54n2', 'name': 'Santtu Koivumäki', 'summary': 'VP of Customer Success @ Clarisights | Marketing Insights/Analytics/Intelligence', 'location': None}, {'link': 'https://www.linkedin.com/in/rogerdudler', 'name': 'Roger Dudler', 'summary': 'Founder & CEO at Frontify', 'location': None}, {'link': 'https://www.linkedin.com/in/arun-srinivasan', 'name': 'Arun Srinivasan', 'summary': 'CEO at Clarisights | The marketing analytics platform for leading enterprises', 'location': None}, {'link': 'https://www.linkedin.com/in/shreyansh-chandak-421034123', 'name': 'Shreyansh Chandak', 'summary': 'Software Engineer at Clarisights', 'location': None}, {'link': 'https://www.linkedin.com/in/paavobeckman', 'name': 'Paavo Beckman', 'summary': 'Founder & Chief of Development at Catapult | Building the next gen company discovery (innopipe.ai) | Public speaker', 'location': None}, {'link': 'https://www.linkedin.com/in/ankur-gupta-3a24438', 'name': 'Ankur Gupta', 'summary': "Co-Founder at Clarisights (Techstars '18)", 'location': None}], 'recommendations': [], 'activities': [{'title': "Brands excite me. Driven by curiosity, I dive into particularly interesting ones once in a while.Storytelling is key in branding. I've always…", 'link': 'https://cz.linkedin.com/posts/gabrielsherrera_once-upon-a-time-how-storytelling-makes-activity-6988145172408586240-r7aB', 'activity_status': 'Sdílel(a): Gabriel Herrera'}, {'title': "3 days left! 😱This is going to be a conversation you don't want to miss!Sign up now. Link in the comments 👇#innovation #data #webinar", 'link': 'https://cz.linkedin.com/posts/catapult-international_innovation-data-webinar-activity-6974969232807612417-FYGI', 'activity_status': 'Dal(a) líbí se: Gabriel Herrera'}, {'title': '”We’ve been sponsoring Pride for over a decade. I don’t give a shit about who do people love. Loving whomever you like is a basic human right. And if…', 'link': 'https://cz.linkedin.com/posts/saritaruneberg_petterstordalen-nbforum2022-equality-activity-6978094053020041216-GAtC', 'activity_status': 'Dal(a) líbí se: Gabriel Herrera'}], 'similarly_named_profiles': [{'name': 'Gabriel Herrera', 'link': 'https://ph.linkedin.com/in/gabriel-herrera-42b43133', 'summary': 'Construction Manager at China Harbour Engineering Co. Ltd', 'location': 'Calabarzon, Filipíny'}, {'name': 'Gabriel Herrera', 'link': 'https://www.linkedin.com/in/baysystemsinc', 'summary': '--', 'location': 'Palo Alto, CA'}, {'name': 'Gabriel Herrera', 'link': 'https://mx.linkedin.com/in/gherrera83', 'summary': 'Retail Sales Manager (Consumer) en AMD', 'location': 'Mexico City, Mexiko'}, {'name': 'JUAN Gabriel HERRERA QUIROZ', 'link': 'https://co.linkedin.com/in/juan-gabriel-herrera-quiroz-a7bab18a', 'summary': 'Juan Gabriel Herrera Quiroz', 'location': 'Oddělení Antioquia, Kolumbie'}, {'name': 'GABRIEL HERRERA', 'link': 'https://ar.linkedin.com/in/gabriel-herrera-6281a71b', 'summary': 'GERENTE en INMOBILIARIA', 'location': 'Argentina'}], 'articles': [], 'groups': [], 'skills': [], 'inferred_salary': None, 'gender': None, 'birth_date': None, 'industry': None, 'extra': None, 'interests': [], 'personal_emails': [], 'personal_numbers': []}
#extracted_info = extract_info(testdata)

# Print or process the extracted information
#print(extracted_info)
