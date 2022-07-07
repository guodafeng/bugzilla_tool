#encoding=utf-8
import requests
import json
from common import *
from comments import Get_Comments

@RequestGetDecorator
def Get_Attachments(url_base, api_key, bug_id=None, attachment_id=None):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/attachment.html#get-attachment
    '''
    params={"api_key":api_key}
    if bug_id:
        req = url_base +"/rest/bug/{bug_id}/attachment".format(bug_id=bug_id)
    elif attachment_id:
        req = url_base +"/rest/bug/attachment/{attachment_id}".format(attachment_id=attachment_id)
    else:
        raise Exception("parameter error!")
    return req, params

def Get_CQ_Attachment_Path(url_base, api_key, id):
    bSuccess, comments = Get_Comments(url_base, api_key, id)
    if not bSuccess:
        return None        
    comment0 = comments['bugs'][str(id)]['comments'][0]
    text = comment0['text']
    key = "Attachments Shared Path and FTP Path:"
    start = text[text.find(key) + len(key):].split("\n")
    attachment_path = start[1]
    return attachment_path

@RequestPostDecorator
def Create_Attachment(url_base, api_key, bug_id, *args, **kwargs):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/attachment.html#create-attachment
    '''
    req = url_base + "/rest/bug/{bug_id}/attachment".format(bug_id=bug_id)
    options = [
        "ids","data","file_name","summary","content_type",
        "comment","is_patch","is_private","flags"
        ]
    params={"api_key":api_key}
    if kwargs:
        for param in params_in_need:
            if param not in kwargs.keys():
                err = "param \'{}\'  muset be set!".format(param)
                raise Exception(err)
        for key in kwargs.keys():
            if key not in options:
                err = "\'" + key + "\' is not supported!"
                raise Exception(err)
        params.update(kwargs)
    else:
        raise Exception("param error!")
    
    return req, params
