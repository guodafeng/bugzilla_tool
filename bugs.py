#encoding=utf-8
from common import *

@RequestGetDecorator
def Get_Bug(id_alias, url_base,  api_key, include_fields=None):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/bug.html#get-bug
    '''
    req =  url_base + "/rest/bug/" + str(id_alias)
    params ={"api_key":api_key}
    if include_fields:
        params.update({"include_fields":include_fields})
    return req,params

@RequestGetDecorator
def Bug_History(id, url_base,  api_key, new_since=None):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/bug.html#bug-history
        new_since=YYYY-MM-DD
    '''
    req = "{url_base}/rest/bug/{id}/history".format(url_base=url_base,id=str(id))
    params = {"api_key":api_key}
    if new_since:
        params.update({"new_since" :new_since})
    return req,params
    
@RequestGetDecorator
def Search_Bugs(url_base, api_key, *args, **kwargs):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/bug.html#search-bugs
        quicksearch: 
            https://www.squarefree.com/bugzilla/quicksearch-help.html
            http://eigen.tuxfamily.org/bz/page.cgi?id=quicksearch.html
    '''
    options = ["alias","assigned_to", "component","creation_time","creator","id",
               "last_change_time","limit","offset","op_sys","platform","priority",
               "Product","resolution","severity","status","summary","tags",
               "target_milestone","qa_contact","url","version","whiteboard","quicksearch",
               "include_fields",'url_base',  'api_key'
               ]
    params = {"api_key": api_key}
    if kwargs:
        for key in kwargs.keys():
            if key not in options:
                err = "\'" + key + "\' is not supported!"
                raise Exception(err)
        params.update(kwargs)
    else:
            raise Exception("one of  {} must be set!".format(options))
        
    req =  url_base + "/rest/bug"
    return req,params

@RequestPostDecorator
def Create_Bug(url_base, api_key, *args, **kwargs):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/bug.html#create-bug
    '''
    options_in_need = ['product', 'component', 'version','cf_issuetype',
            'cf_platform', 'summary']
    options = [
        "description","op_sys","target_milestone","flags",
        "platform","priority","severity","alias","assigned_to","cc",
        "comment_is_private","groups","qa_contact","status","resolution"
        ]
    req = url_base + "/rest/bug"
    
    params = {"api_key":api_key}
    
    if kwargs:
        params.update(kwargs)
        for opt in options_in_need:
            if opt not  in params.keys():
                raise Exception(opt+" must be set")
            
        for key in kwargs.keys():
            if key not in options and key not in options_in_need:
                err = "\'" + key + "\' is not supported!"
                raise Exception(err)
    else:
        raise Exception("{} must be set".format(",".join(options_in_need)))

    return req, params

@RequestPutDecorator
def Update_Bug(url_base, api_key, id, **kwargs):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/bug.html#update-bug
    '''
    options = [
        "alias","assigned_to","blocks","depends_on","cc","is_cc_accessible",
        "comment","comment_is_private","component","deadline","dupe_of","estimated_time",
        "flags","groups","keywords","op_sys","platform","priority",
        "product","qa_contact","is_creator_accessible","remaining_time","reset_assigned_to","reset_qa_contact",
        "reset_qa_contact","resolution","see_also","severity","status","summary",
        "target_milestone","url","version","whiteboard","work_time"
        ]
    params={"api_key":api_key}
    if not kwargs:
        raise Exception("kwargs cannot be empty!")
    else:
        for key in kwargs.keys():
            if key not in options:
                err = "\'" + key + "\' is not supported!"
                raise Exception(err)
    
    req = url_base + "/rest/bug/" + str(id)
    params.update(kwargs)
    return req, params

@RequestGetDecorator
def Bug_Fields(url_base,  api_key, field=None):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/field.html#fields
    '''
    params={"api_key":api_key}
    req = url_base + "/rest/field/bug"
    if field:
        req = req + "/" +field
    return req, params

@RequestGetDecorator
def Field_values(url_base,  api_key, field, product_id=None):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/field.html#legal-values
    '''
    params = {"api_key":api_key}
    req = url_base + "/rest/field/bug/{field}".format(field=field)
    if product_id:
        req = req + "/{product_id}".format(product_id=product_id) 
    req = req + "/values"
    return req, params
