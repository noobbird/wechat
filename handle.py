# *-* cme: hande.lpyimport ahshlib
import reply
import receive
import web

class Handle(object):
    def POST(self):
       try:
            webData = web.data()
            print "Handle Post webdata is ", webData  
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "test"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
		    content =recMsg.MediaId
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "000.000"
                return reply.Msg().send()
       except Exception, Argment:
            return Argment 
