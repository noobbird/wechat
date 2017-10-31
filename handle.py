#_*_coding:utf-8_*_
# *-* cme: hande.lpyimport ahshlib
import reply
import receive
import web
import psycopg2

conn = psycopg2.connect(database="netease", user="ysr", password="123456", host="120.24.0.134", port="5432")
class Handle(object):
    def POST(self):
       try:
            webData = web.data()
            print "Handle Post webdata is ", webData  
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
		singer = recMsg.Content
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
		    cur = conn.cursor()
		    cur.execute('''SELECT
				singer.singer_name,
					song.song_name,
					song.song_id,
					album."name",
					album.release_date,
					to_char(round(ct.total*1.0/1000, 2), '99999.9') ||'k' as comment_count
					FROM
					singer,
					album,
					song,
					commentthread ct
					WHERE
					singer.singer_name = album.singer
					AND CAST (album.aid AS INTEGER) = song.album_id
					AND ct.comment_thread = song.comment_thread
					AND lower(singer.singer_name) like '%%%s%%' 
					ORDER BY  total DESC
					limit 20'''%singer.lower())
		    rows = cur.fetchall()
	            res ='' 
		    n = 1
	            for row in rows:
			singer = row[0]
			res += str(n) + '.'+ row[1] + '\t' +row[5] +'\n'
			n += 1
		    content = '歌手'+singer + ':\n'
		    content += res if res != '' else "很可惜，没有这个歌手"
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
