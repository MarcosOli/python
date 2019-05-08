import requests
import json
from datetime import datetime
now = datetime.now()

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

# Create a local file called 'pagespeed.txt' and populate it with URLs to test
with open('pagespeed.txt') as pagespeedurls:
    download_dir = 'pagespeed-results.csv'
    file = open(download_dir, 'w')
    content = pagespeedurls.readlines()
    content = [line.rstrip('\n') for line in content]

    columnTitleRow = "URL\ Score\ TTFB\ First Contentful Paint\ Time to Interactive\ Speed Index\ First Meaningful Paint\ First CPU Idle\ Estimated Input Latency\ Total Byte Weight\Data hora\n"
    file.write(columnTitleRow)

    # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
    for line in content:
        # If no "strategy" parameter is included, the query by default returns desktop data.
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=mobile'
        r = requests.get(x)
        final = r.json()
        
        try:
            urlid = final['id']
            split = urlid.split('?') # This splits the absolute url from the api key parameter
            urlid = split[0] # This reassigns urlid to the absolute url
            ID = f'URL: {urlid}'
            ID2 = str(urlid)
            urlscore = final['lighthouseResult']['categories']['performance']['score']
            score = f'Score: {urlscore}'
            score2 = str(urlscore)
            urlttfb = final['lighthouseResult']['audits']['time-to-first-byte']['displayValue']
            TTFB = f'TTFB: {urlttfb} '
            TTFB2 = str(urlttfb)
            urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            FCP = f'First Contentful Paint: {str(urlfcp)}'
            FCP2 = str(urlfcp)
            urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
            FI = f'Time to Interactive: {str(urlfi)}'
            FI2 = str(urlfi)
            urlspeedindex = final['lighthouseResult']['audits']['speed-index']['displayValue']
            speedindex = f'Speed Index: {str(urlspeedindex)}'
            speedindex2 = str(urlspeedindex)
            urlfmp = final['lighthouseResult']['audits']['first-meaningful-paint']['displayValue']
            FMP = f'First Meaningful Paint: {str(urlfmp)}'
            FMP2 = str(urlfmp)
            urlfci = final['lighthouseResult']['audits']['first-cpu-idle']['displayValue']
            FCI = f'First CPU Idle: {str(urlfci)}'
            FCI2 = str(urlfci)
            urleil = final['lighthouseResult']['audits']['estimated-input-latency']['displayValue']
            EIL = f'Estimated Input Latency: {str(urleil)}'
            EIL2 = str(urleil)
            urltbw = final['lighthouseResult']['audits']['total-byte-weight']['displayValue']
            TBW = f'Total Byte Weight: {str(urltbw)}'
            TBW2 = str(urltbw)
                        
        except KeyError:
            print(f'<KeyError> One or more keys not found {line}.')
        
        try:
            row = f'{ID2}\{score2}\{TTFB2}\{FCP2}\{FI2}\{speedindex2}\{FMP2}\{FCI2}\{EIL2}\{TBW2}\{now}\n'
            file.write(row)
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')
            file.write(f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {line}.' + '\n')
        
        try:
            print(ID)
            print(score)
            print(TTFB) 
            print(FCP)
            print(FI)
            print(speedindex)
            print(FMP)
            print(FCI)
            print(EIL)
            print(TBW)
            print(now)
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')

    file.close()
