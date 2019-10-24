from PreProcessing.PolicyPreProcessing import read_policy, create_data_structure, preprocess_pipeline
from PreProcessing.HTML.Utils import get_cleaned_content_from_url, get_written_file_name_from_url

URL = [
    'https://global.canon/en/privacy/',
    'https://www.amazon.com/gp/help/customer/display.html?nodeId=468496',
    'https://www.mopub.com/legal/privacy/',
    'https://www.appache.games/privacy',
    'http://www.metajoy.io/privacy.html',
    'http://www.94-percent.com/policy',
    'https://www.abigames.com.vn/policy',
    'https://www.adobe.com/privacy/policy.html',
    'https://en.akinator.com/content/4/terms-of-service',
    'https://www.any.do/legal/privacy-policy',
    'https://www.apple.com/legal/privacy/en-ww/',
    'https://about.ask.fm/legal/en/privacy.html',
    'https://www.avira.com/en/general-privacy',
    'https://about.babbel.com/en/privacy/',
    'https://en.babybus.com/index.php?s=/index/privacyPolicy.shtml',
    'https://www.bible.com/privacy',
    'https://www.bigbluebubble.com/privacy-policy/',
    'https://www.bitmango.com/privacy-policy/',
    'https://www.blinkist.com/en/privacy',
    'https://www.blizzard.com/en-us/legal/a4380ee5-5c8d-4e3b-83b7-ea26d01a9918/blizzard-entertainment-online-privacy'
    '-policy ',
    'https://www.bodyfast.de/privacy',
    'https://www.boomerangtv.co.uk/#',
    'https://www.bundesliga.com/en/bundesliga/info/privacy-statement',
    'https://www.busuu.com/en/privacy',
    'https://about.canva.com/privacy-policy/',
    'https://www.car2go.com/DE/en/privacy-policy/',
    'https://www.amazon.com/gp/help/customer/display.html?ie=UTF8&nodeId=508088&ref_=footer_cou'
]

sample_policy_format = """# Privacy Policy

## Topic 1 

content of topic 1.1
content of topic 1.2
content of topic 1.3
content of topic 1.4
content of topic 1.5

## Topic 2 

content of topic 2.1
content of topic 2.2
content of topic 2.3
content of topic 2.4
content of topic 2.5

## Topic 3 

content of topic 3.1
content of topic 3.2
content of topic 3.3
content of topic 3.4
content of topic 3.5

### Topic 3.1 

content of topic 3.1.1
content of topic 3.1.2
content of topic 3.1.3
content of topic 3.1.4
content of topic 3.1.5

### Topic 3.2 

content of topic 3.2.1
content of topic 3.2.2
content of topic 3.2.3
content of topic 3.2.4
content of topic 3.2.5


## Topic 4 

content of topic 4.1
content of topic 4.2
content of topic 4.3
content of topic 4.4
content of topic 4.5
"""

data_strut = create_data_structure(sample_policy_format)

# complete_test = preprocess_pipeline(URL[4])

# print(complete_test)

# policy = read_policy(URL[15])
# print(policy)
#
# policy = get_policy_from_url(URL[4])
# get_file_of_policy_from_url(URL[15])