#2022.3.23 uvicorn wps:app --port 7002 --host 0.0.0.0 --reload
import json, time, traceback, en, fastapi, uvicorn, fire,sys, logging #CRITICAL > ERROR > WARNING > INFO > DEBUG
from dsk import mkf,gecv1

app				= fastapi.FastAPI()
is_sent_valid	= lambda snt:	( snt := snt.strip(), snt.isascii() if snt else False )[-1]
valid_snts		= lambda essay: [ (snt.text,snt[0].idx  ) for snt in spacy.sntbr(essay).sents if is_sent_valid(snt.text)]

logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh	= logging.FileHandler(f"wps-{time.strftime('%Y%m%d%H%M', time.localtime(time.time()))}.log", mode='w')
fh.setLevel(logging.INFO) 
fh.setFormatter(logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s"))
logger.addHandler(fh)

@app.post("/gecv1/dsk")
def gecv1_dsk(arr:dict={"key":"1002-3", "rid":"10", "essay":"English is a internationaly language which becomes importantly for modern world. In China, English is took to be a foreigh language which many student choosed to learn. They begin to studying English at a early age. They use at least one hour to learn English knowledges a day. Even kids in kindergarten have begun learning simple words. That's a good phenomenan, for English is essential nowadays. In addition to, some people think English is superior than Chinese. In me opinion, though English is for great significance, but English is after all a foreign language. it is hard for people to see eye to eye. English do help us read English original works, but Chinese helps us learn a true China. Only by characters Chinese literature can send off its brilliance. Learning a country's culture, especial its classic culture, the first thing is learn its language. Because of we are Chinese, why do we give up our mother tongue and learn our owne culture through a foreign language?"}, 
	diffmerge:bool=False, body:str='essay', topk_snts:int=0, gecon:bool=True, dskhost:str="172.17.0.1:7095", 
	check_valid_sents:bool=False, check_gec:bool=False):  
	''' when 'rid':"10", to return dsk dict, else return mkf list '''
	try:
		start = time.time()
		logger.info(f"input: {json.dumps(arr)}")
		essay	= arr.get(body, arr.get('doc',''))
		logger.info(f"essay: {essay}")
		if not essay.strip(): return 

		pairs	=  valid_snts(essay) # (snt, offset) 
		if check_valid_sents : return pairs
		if topk_snts > 0 : pairs = pairs[0:topk_snts]
		logger.info(f"valid sents: {json.dumps(pairs)}")

		snts	= [row[0] for row in pairs]
		sntdic	= gecv1.gecsnts(snts) if gecon else {snt:snt for snt in snts}
		if check_gec: return sntdic 
		logger.info(f"gec sents: {json.dumps(sntdic)}")

		dsk		= mkf.sntsmkf([ (row[0], sntdic.get(row[0], row[0])) for row in pairs], dskhost=dskhost, asdsk=True) #[{'feedback': {'_modern@confusion': {'cate': 
		logger.info(f"dsk: {json.dumps(dsk)}")

		if 'snt' in dsk: [ arsnt.get('meta',{}).update({'offset': pairs[i][1]})  for i, arsnt in enumerate(dsk['snt']) ]
		if not 'info' in dsk: dsk['info'] = {}
		dsk['info'].update(arr)
		dsk['info'].update({"timing": time.time() -start})
		return dsk 
	except Exception as ex:
		print(">>gecv1_dsk Ex:", ex, "\t|", arr)
		exc_type, exc_value, exc_traceback_obj = sys.exc_info()
		traceback.print_tb(exc_traceback_obj)
		return str(ex)

@app.get('/')
def home(): return fastapi.responses.HTMLResponse(content=f"<h2>wps api</h2><a href='/docs'> docs </a> | <a href='/redoc'> redoc </a><br>uvicorn wps:app --port 80 --host 0.0.0.0 --reload <br><br>2022.3.23")

def consume(queue, host='172.17.0.1', port=5672, user='pigai', pwd='NdyX3KuCq', durable=True, heartbeat=60, prefetch_count=1, debug=False,
		essay_field = 'essay', gecon=True, topk_snts= 0, # when> 0, mean only topk snts considered 
		dsk_exchange="wps-dsk", routing_key="pigai_callback_api_essay",  #wps-dsk-to-callback
		essay_exchange = 'wps-essay', expired_routing_key="wps-essay-long", timeout=3.6, failed_routing_key="wps-essay-failed"):
	''' mq consumer, set timeout = -1, upon long-essay '''
	import pika 
	from func_timeout import func_timeout, FunctionTimedOut
	credentials = pika.PlainCredentials(user, pwd)
	parameters	= pika.ConnectionParameters(host, port, '/', credentials, heartbeat=heartbeat)
	connection	= pika.BlockingConnection(parameters)
	channel		= connection.channel()
	channel.queue_declare(queue=queue, durable=durable)
	channel.basic_qos(prefetch_count=prefetch_count)

	def callback(ch, method, properties, body):
		try:
			start	= time.time()
			arr		= json.loads(body.decode(encoding='UTF-8',errors='ignore'), strict=False)
			key		= arr.get('key',"")
			dsk		= func_timeout( float(arr.get('timeout',timeout)) ,gecv1_dsk , args=(arr,)) if timeout > 0 else  gecv1_dsk(arr, gecon=gecon, topk_snts=topk_snts)  
			ch.basic_publish(exchange=arr.get('exchange', dsk_exchange), routing_key=arr.get("routing_key",routing_key), body=json.dumps(dsk))

			if debug: 
				tim = time.time()-start
				print (f"== {key} \t| timing: ", tim , flush=True)
				if timeout > 0 and tim > timeout: 
					print (">>slow ==\n", body.decode() )
					logger.warning(f"slow={tim}:{key}")

		except FunctionTimedOut:
			ch.basic_publish(exchange=essay_exchange, routing_key=expired_routing_key, body=body.decode())
			print ("expired:\n", body.decode()) 
			logger.warning(f"expired:{body.decode()}")

		except Exception as err:
			ch.basic_publish(exchange=essay_exchange, routing_key=failed_routing_key, body=body.decode())
			print("Failed:", err, "\n", body.decode())
			logger.error(f"failed:{body.decode()}")
			exc_type, exc_value, exc_traceback_obj = sys.exc_info()
			traceback.print_tb(exc_traceback_obj)

		ch.basic_ack(delivery_tag = method.delivery_tag)

	print("begin to consume queue: ", queue, host, port, flush=True)
	channel.basic_consume(queue, callback, auto_ack=False)
	channel.start_consuming()

def process(infile, outfile=None):
	''' line json -> dsk  '''
	print ("started to process:", infile, flush=True)
	with open(outfile if outfile else infile + ".dsk" , 'w') as fw: 
		for line in open(infile, 'r').readlines():
			try:
				arr = json.loads(line.strip(), strict=False)
				dsk = gecv1_dsk(arr)
				fw.write( json.dumps(dsk)  + "\n")
			except Exception as ex:
				print ("process ex:", ex, line[0:36]) 
	print ('finished:', infile) 

if __name__ == '__main__':
	fire.Fire({"consume":consume,"process":process,
	"hello": lambda : print(gecv1_dsk()), })

'''
python wps.py wps-essay-normal --host 192.168.201.79 --debug true
(cuda113) ubuntu@gpu120:/data/cikuu/pypi/util$ cuda=2 python wps.py wps-essay-normal --host 192.168.201.79 --debug true

python wps.py consume wps-essay-long --host 192.168.201.79 --timeout 0 --gecon false --debug true 

--routing_key wps-dsk-to-callback-long

nogpu: "timing": 0.20521903038024902

== 53.25092530250549
{"key":"PG115_11bae9_a6085c01798babf7262c83bc829bd09d","rid":"861591","ct":1647980829.9873,"tit":"new","doc":"\rIn the spring semester of 2022, I chose a course called career exploration. Students in this course are basically people who come to seek the help of teachers to make plans for their future. As a professor of this course, Michelle St. George helped many students during her tenure. She received a bachelor's degree in psychology from William Patterson university with a minor in women's & gender studies. These two majors have brought a lot of benefits for her to do this job well. She can not only better communicate with students through psychological analysis, but also won't have any prejudice against students because of gender. In this case, the consultation results obtained by students tend to be more fair. Michelle has her own views on job opportunities for different genders. \"I believe this is a good opportunity, no matter what gender you are, as long as you have skills,\" she said During the interview, she mentioned that driven by the strong recommendation of her friends and her own interests, she finally chose to continue to study the master's degree of women's & Gender Studies at Rutgers University. He has worked in Rutgers since 2011 and joined career exploration and success in 2013. This course contains many different aspects of knowledge, which greatly increases students' interest in this course. So far, students have experienced simulated recruitment in this course, wrote job applications, used various job application websites to check the jobs they are interested in, and tried to get in touch with alumni engaged in relevant jobs, so as to gain valuable experience. \"Through this course, students can learn many valuable lessons that can last their life. They will be able to develop the skills needed to effectively explore, test and reflect on career ideas. This course will enable them to be resilient in their career and use their art and science education and other unique advantages to build a purposeful life.\" Michelle St. George said. Michelle chose this career for a simple reason. \"I chose this to start with. I like working with students because I was in their position in college and needed career advice. Moreover, I like giving back to others,\" she said \"Helping students and seeing them get the next career opportunity\" is Michelle's greatest pleasure in the process of work. As a professor, she will encounter some difficult students during teaching, but she shows her great tolerance for them. \"Sometimes it's hard for me to get my students to submit their homework on time. I try my best to cooperate with them and allow them to finish their work.\" Students' positive attitude towards learning can often give teachers greater motivation. Michelle's happiest moment was watching the students have a positive discussion around the theme of the discussion board. She believes that joining the education profession has brought her a different experience from other professions. \"I like to share my knowledge with students.\" \"It's very meaningful to hear success stories about internships and jobs that students get from the skills they learn in this course,\" Michelle said In order to do a good job, people need solid basic knowledge, high moral quality, corresponding special skills and even rapid adaptability and learning ability. Michelle cited her position as an example: \"teaching requires a master's degree. In addition, the recruitment cycle, knowledge of various industries and the job market, as well as skills in resumes, cover letters, networking, LinkedIn, etc., are important for successfully teaching this course. Finally, I think empathy is important. Understanding the difficulties and fears students may face is very important for them to overcome difficulties and succeed.\" At the end of the interview, her advice to students is to participate in campus activities and take advantage of all opportunities at Rutgers University. \"Because I want to see everyone do well in the course and leave with useful knowledge,\" Michelle said. Developing skills and learning as much as possible will help shape students' future experiences.\r","solution":[],"lang":"zh_cn","mq_name":"pigai_callback_api_essay","progress":"0","_token":{"access_token":"487cf314f61e6bb7c0cc18427a869e8fc2856eff","client_id":"f29acd428d93ac8243aa5d6aef11bae9","user_id":"115","expires":1647981863,"scope":"all_json"},"meta_data":{"scope":"all_json"},"models":"nn"}

{"failed": "true", "message": "parse failed", "src": {"key": "PG115_11bae9_f672b27242ac3821e63696d04f07edd6", "rid": "861591", "ct": 1647990343.5608, "tit": "2022.3.22\u4f5c\u4e1a.docx", "doc": "\u8bed\u6587\uff1a\u300a\u4e00\u672c\u901a\u300bP17~18                                                                                                                                                     \n\u6570\u5b66\uff1a\u300a\u540d\u6821\u300bP35~36\n\u82f1\u8bed\uff1a1\u3001\u300a\u57fa\u8bad\u300bP22~23\n2\u3001\u80cc\u8bf5P22 A.B\u6bb5\n\u653f\u6cbb1\u3001\u300a\u57fa\u8bad\u300bP26~28\uff08\u4e0d\u4ea4\uff09\n2\u3001\u300a\u540d\u6821\u300bP23~25\uff08\u8981\u4ea4\uff09\n\u5386\u53f2\uff1a\u300a\u57fa\u8bad\u300bP34~36 \uff08\u4e0d\u4ea4\uff09\n", "solution": [], "lang": "zh_cn", "mq_name": "pigai_callback_api_essay", "progress": "0", "_token": {"access_token": "9b20d44525d8630b7f71d180ef5ce7b7dd943b79", "client_id": "f29acd428d93ac8243aa5d6aef11bae9", "user_id": "115", "expires": 1647996249, "scope": "all_json"}, "meta_data": {"scope": "all_json"}, "models": "nn"}}

{"key":"PG115_11bae9_1b4f4fc96bafe06936445a8b8217315e","rid":"861591","ct":1648006153.2564,"tit":"Answer Sheet(1).docx","doc":"Answer Sheet\rPart II\r__________  22. __________  23. __________  24. __________  25. __________\r__________  27. __________  28. __________  29. __________  30. __________\r__________  32. __________  33. __________  34. __________  35. __________\r\r_______________  37. ______________  38. ______________  39. ______________\r_______________  41. ______________  42. ______________  43. ______________\r\r_______________  45. ______________  46. ______________  47. ______________\r_______________  49. ______________  50. ______________  51. ______________\r\r_______________   _______________   53. _______________   _______________\r54. _______________   _______________    55. _______________   _______________\r_______________   _______________   57. _______________   _______________\r58. _________________________________________________________________________\r\rPart III\r_________ 60. _________ 61. _________ 62. _________ 63. _________ 64. _________ \r_________ 66. _________ 67. _________ 68. _________ 69. _________ 70. _________ \r_____________    72. ____________    73. _____________    74._____________ \r_____________    76. ____________    77. _____________\r\r________________________________________________________________________\r________________________________________________________________________\r________________________________________________________________________\r________________________________________________________________________\r________________________________________________________________________\r________________________________________________________________________\r","solution":[],"lang":"zh_cn","mq_name":"pigai_callback_api_essay","progress":"0","_token":{"access_token":"c6dd7e779c184bdeff2d9b180b9dda3d669a1735","client_id":"f29acd428d93ac8243aa5d6aef11bae9","user_id":"115","expires":1648010539,"scope":"all_json"},"meta_data":{"scope":"all_json"},"models":"nn"}

{'And one day he said to me: &quot;You ought to make a beautiful drawing, so that the children where you live can see exactly how all this is.': 'And one day he said to me: &quot;You ought to make a beautiful drawing, so that the children where you live can see exactly how all this is.', 'That would be very useful to them if they were to travel some day.': 'That would be very useful to them if they were to travel some day.', 'Sometimes,&quot; he added, &quot;there is no harm in putting off a piece of work until another day.': 'Sometimes,&quot; he added, &quot;there is no harm in putting off a piece of work until another day.', 'But when it is a matter of baobabs, that always means a catastrophe.': 'But when it is a matter of baobabs, that always means a catastrophe.', 'I knew a planet that was inhabited by a lazy man.': 'I knew a planet that was inhabited by a lazy man.', 'He neglected three little bushes&hellip;&quot;\nIndeed, as I learned, there were on the planet where the little prince lived-- as on all planets-- good plants and bad plants.': 'Indeed, as I learned, there were on the planet where the little prince lived-- as on all planets-- good plants and bad plants.', 'In consequence, there were good seeds from good plants, and bad seeds from bad plants.': 'In consequence, there were good seeds from good plants, and bad seeds from bad plants.', 'But seeds are invisible.': 'But seeds are invisible.', "They sleep deep in the heart of the earth's darkness, until some one among them is seized with the desire to awaken.": "They sleep deep in the heart of the earth's darkness, until some one among them is seized with the desire to awaken.", 'Then this little seed will stretch itself and begin-- timidly at first-- to push a charming little sprig inoffensively upward toward the sun.': 'Then this little seed will stretch itself and begin-- timidly at first-- to push a charming little sprig inoffensively upward toward the sun.', 'If it is only a sprout of radish or the sprig of a rose-bush, one would let it grow wherever it might wish.': 'If it is only a sprout of radish or the sprig of a rose-bush, one would let it grow wherever it might wish.', 'But when it is a bad plant, one must destroy it as soon as possible, the very first instant that one recognizes it.': 'But when it is a bad plant, one must destroy it as soon as possible, the very first instant that one recognizes it.'}

'''