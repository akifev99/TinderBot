import robobrowser
import re

##MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
##FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

FACEBOOK_ID = ''


##FACEBOOK_AUTH_TOKEN = 'EAAGm0PX4ZCpsBAAagcncSZCmH6ezIXGcwu9ZCZCi4kAWopXe8kQxMCvx3YFMS75ZC7uhDnBDZAXnKPLWJd7OWlPlcGOUZBqQ2l9jF40k35lOoEvFSgAIwdgYeKXc8PGYZBH8I3ZAW2SofePAkZCAgmPIPcRpQZAfaZB9QBZCiOpwdH3Ta9l05TZBs3AIevDR29QrUoGUF5TCcHhhSrkFoRrsNTmep8tvxy8RMEPE1pthMZAgMfYSnhjWOXehuSyR843y4SRZAmu61f4AcOnyRwZDZD'

def get_access_token(url):
    s = robobrowser.RoboBrowser(user_agent=ua, parser="lxml")
    s.open(url)
    ## submit login form
    f = s.get_form()
    print(f.parsed)

    ##s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    ## get access token from the http response
    ##access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    ##return access_token
FACEBOOK_AUTH_TOKEN = get_access_token("http://www.google.ru")
