import bugs
import comments
import attachments

class BugzillaBase():
    def __init__(self, url_base, api_key):
        self.url_base = url_base
        self.api_key = api_key
    
    def set_url_base(self, url_base):
        self.url_base = url_base
    
class BugzillaWebService(BugzillaBase):
    '''
        The REST API for creating, changing, and getting the details of bugs.
        This part of the Bugzilla REST API allows you to file new bugs in Bugzilla and to get information about existing bugs.
        View details please visit:
            https://bugzilla.readthedocs.io/en/5.0/api/core/v1/bug.html
    '''
    def __init__(self, url_base, api_key):
        super(BugzillaWebService, self).__init__(url_base, api_key)
        
    def Get_Bug(self, api_key, id_alias, include_fields=None):
        return bugs.Get_Bug(id_alias, self.url_base, api_key, include_fields)
    
    # verifyed
    def Get_Bug(self, id_alias, include_fields=None):
        return bugs.Get_Bug(id_alias, self.url_base, self.api_key, include_fields)

    # verifyed
    def Create_Bug(self, dict_info):
        return bugs.Create_Bug(self.url_base, self.api_key, **dict_info) 
    
    def Get_Fields(self):
        return bugs.Bug_Fields(self.url_base, self.api_key)

    def Bug_History(self, bug_id,  api_key, new_since=None):
        return bugs.Bug_History(bug_id, self.url_base, api_key, new_since)
    
    def Search_Bugs(self, *args, **kwargs):
        return bugs.Search_Bugs(self.url_base, self.api_key, *args, **kwargs)
    
    def Search_Bugs(self, *args, **kwargs):
        return bugs.Search_Bugs(self.url_base, self.api_key, *args, **kwargs)

    def Get_Comments(self, id=None, comment_id=None, new_since=None, include_fields=None):
        return comments.Get_Comments(self.url_base,  self.api_key, id, comment_id, new_since, include_fields)

    def Get_Attachments(self, bug_id=None, attachment_id=None):
        return comments.Get_Attachment(self.url_base, self.api_key, bug_id, attachment_id)



def test_create(ws):
    bug_info = {'product':'Dragon',
            'component': 'BSP',
            'version': 'DVT', 
            'cf_issuetype': 'Bug',
            'cf_platform': 'Unisoc',
            'summary': 'create by scripts',
            'assigned_to': 'yunfeng.guo@fih-foxconn.com',
            'description': 'test'
            }
    print(ws.Create_Bug(bug_info))

def test_get(ws):
    print(ws.Get_Bug(6))



if __name__ == '__main__':
    ws = BugzillaWebService("https://10.75.10.95/bugzilla",
            "mfvXTgdyzBoYiTtBu2WwdrNRbuIk841cTmSYCyfE")

    print(ws.Get_Fields())

