#encoding=utf-8
from common import *

@RequestGetDecorator
def Get_Comments(url_base,  api_key, id=None, comment_id=None, new_since=None, include_fields=None):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/comment.html#get-comments
        parameters:
            id: A single integer bug ID 
            comment_id: A single integer comment ID
            new_since:  datetime, YYYY-MM-DD
            include_fields: filt fields you want
        useages:
            case  1:  Get_Comments(id), get all comments of BUG[d]
            case 2:  Get_Comments(id, new_since)  get all comments of BUG[id] since [new_since]
            case 3:  Get_Comments(comment_id)  get specified comment by [comment_id]
    '''
    params = {"api_key":api_key}
    if comment_id:
        req = url_base + "/rest/bug/comment/{comment_id}".format(comment_id=comment_id)
    elif id:
        req = url_base + "/rest/bug/{id}/comment".format(id=id)
        if new_since:
            params.update({"new_since":new_since})
    else:
        raise Exception("parameter error! param 'id' or comment_id must 'be' set!")
    if include_fields:
        params.update({"include_fields":include_fields})
    return req, params

@RequestPostDecorator
def Create_Comments(url_base,  api_key, id, comment, is_private=False, work_time=None):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/comment.html#create-comments
        This allows you to add a comment to a bug in Bugzilla.
        parameters:
        id, int,  bug id. 
        comment, string, bug comment to be added. 
        is_private, boolean,  comment is private or not. 
        work_time, double, Adds this many hours to the “Hours Worked” on the bug. If you are not in the time tracking group, this value will be ignored. 
    '''
    params = {
        "api_key":api_key,
        "comment":comment,
        "is_private":is_private
    }
    if work_time:
        params.update({"work_time":work_time})
        
    req = url_base + "/rest/bug/{id}/comment".format(id=id)
    return req, params

@RequestGetDecorator
def Search_Comments_Tags(url_base,  api_key, query):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/comment.html#search-comment-tags
        Searches for tags which contain the provided substring.
    '''
    params={"api_key":api_key}
    req = url_base + "/rest/bug/comment/tags/{query}".format(query=query)
    
    return req, params

@RequestPutDecorator
def Update_Comments_Tags(url_base,  api_key, comment_id, add, tags):
    '''
        https://bugzilla.readthedocs.io/en/5.0/api/core/v1/comment.html#update-comment-tags
        Adds or removes tags from a comment.
        parameters:
            comment_id,
            add,  True for add  and False for remove
            tags, tags to be added in list format
    '''
    params = {
        "comment_id":comment_id,
        "api_key":api_key      
        }
    req = url_base + "/rest/bug/comment/{comment_id}/tags".format(comment_id=comment_id)
    if type(tags) != list:
        raise Exception("type error, type of \'tags\' must be a list")
    if add:
        params.update({"add":tags})
    else:
        params.update({"remove":tags})
    return req, params
