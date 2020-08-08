#===============================================================
# Creator: Ghostinterminal.
# Date: Aug 12 2018
# Time:9:35 AM
# For: POST EXPLOTIATION.
# For Website: FACEBOOK.COM
# PURPOSE: MISC TOOLS.
# ==============================================================

#***************************************************************
#======================= MAIN TARGET ===========================
#============ NAME: https://m.facebook.com/ ====================
#======================= TARGET END ============================
#***************************************************************

import requests
import base64


class fbTools():
    ''' Class name: FBTOOLS. '''
    ''' Provides: Tools related FB pentesting... '''

    # ==================== Starting of refsrcs ==============================
    # List of refsrc for facebook.
    # Can be used for making server to beleive that request is made from their website.
    # =======================================================================

    def decodeCookie(self,cookieDict):

        def __init__(self):

            self.Agent = {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
            self.nextkeyword = '?next='
            self.nextUrls = ['https://m.facebook.com/settings', 'https://m.facebook.com/messages', 'https://www.facebook.com/messages/t', ]
  		
  		# Take cookie dictionary as argument.
  		# And return each key as decode string
  	cookies = cookieDict

  	for key in cookies.keys():
  		try:
  			print '\n',key,' : ', base64.b64decode(str(cookies[key]))
  		except:
  			pass

  	return '\n',0
    
    def giveRefsrc(self, key):
        refsrcs = ['https://m.facebook.com/login/device-based/password',
                   'https://m.facebook.com/login', 'https://www.facebook.com/']
        virtual_list = []

        if key == '1':
            for ref in refsrcs:
                virtual_list.append('?_refsrc=' + ref)
        if key == '2':
            for ref in refsrcs:
                virtual_list.append('&refsrc=' + ref)
        return virtual_list

    def giveNext(self, key):

        # =======================================================================
        # Global List of ?next for facebook.
        # List can be used to supply facebook about what do when device is logged in.
        # ======================== STARTING LIST ================================

        nexts = ['https://m.facebook.com/settings', 'https://m.facebook.com/privacy',
                 'https://m.facebook.com/logout/', 'https://m.facebook.com/settings/email/add']
        virtual_list = []
        if key == '1':
            for next_ in nexts:
                virtual_list.append('&next=' + next_)

        if key == '2':
            for next_ in nexts:
                virtual_list.append('?next=' + next_)

        return virtual_list

    def makeCookie(self, raw_string):
        ''' getCookie will return a dict of cookies. '''
        ''' Returned dict can be used in python request module for supplying cookies '''
        ''' Usage of cookies: cookies = getCookies('afdadsfasdadsfa') '''
        ''' data = requests.get(url, cookies=cookies)'''

        raw_string = ''.join(raw_string.split(';'))
        raw_string = ''.join(raw_string.replace('=', '\':\''))
        raw_string = ''.join(raw_string.replace(' ', '\',\''))
        cookies = '{\'' + raw_string + '\'}'
        return cookies

    def makeConnection(self, url, cookies):
        # ===============================================================
        # makeConnection method will make a connection with https://m.facebook.com.
        # This will make request with refsrc to https://m.facebook.com.
        # ===============================================================

        data = requests.get(url, cookies=cookies, headers=self.Agent)
        print data.text






if __name__ == '__main__':
    fbtools = fbTools()
    fbtools.makeConnection('https://m.facebook.com/typeahead/search/facebar/bootstrap/', cookies=cookies)