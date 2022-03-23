#2022.3.23 uvicorn wps:app --port 7002 --host 0.0.0.0 --reload
import json, time, traceback, en, fastapi, uvicorn, fire
from dsk import mkf,gecv1

app				= fastapi.FastAPI()
is_sent_valid	= lambda snt:	( snt := snt.strip(), snt.isascii() if snt else False )[-1]
valid_snts		= lambda essay: [ (snt.text,snt[0].idx  ) for snt in spacy.sntbr(essay).sents if is_sent_valid(snt.text)]

@app.get('/')
def home(): return fastapi.responses.HTMLResponse(content=f"<h2>wps api</h2><a href='/docs'> docs </a> | <a href='/redoc'> redoc </a><br>uvicorn wps:app --port 80 --host 0.0.0.0 --reload <br><br>2022.3.23")

@app.get("/wps/gecv1dsk")
def gecv1_dsk(arr:dict={"key":"1002-3", "rid":"10", "essay":"English is a internationaly language which becomes importantly for modern world. In China, English is took to be a foreigh language which many student choosed to learn. They begin to studying English at a early age. They use at least one hour to learn English knowledges a day. Even kids in kindergarten have begun learning simple words. That's a good phenomenan, for English is essential nowadays. In addition to, some people think English is superior than Chinese. In me opinion, though English is for great significance, but English is after all a foreign language. it is hard for people to see eye to eye. English do help us read English original works, but Chinese helps us learn a true China. Only by characters Chinese literature can send off its brilliance. Learning a country's culture, especial its classic culture, the first thing is learn its language. Because of we are Chinese, why do we give up our mother tongue and learn our owne culture through a foreign language?"}, 
	diffmerge:bool=False, body:str='essay', topk_snts:int=0, gecon:bool=True, dskhost:str="gpu120.wrask.com:7095", 
	check_valid_sents:bool=False, check_gec:bool=False):  
	''' when 'rid':"10", to return dsk dict, else return mkf list '''
	try:
		essay	= arr.get(body, arr.get('doc',''))
		pairs	=  valid_snts(essay) # (snt, offset) 
		if check_valid_sents : return pairs
		if topk_snts > 0 : pairs = pairs[0:topk_snts]

		snts	= [row[0] for row in pairs]
		sntdic	= gecv1.gecsnts(snts) if gecon else {snt:snt for snt in snts}
		if check_gec: return sntdic 

		dsk		= mkf.sntsmkf([ (row[0], sntdic.get(row[0], row[0])) for row in pairs], dskhost=dskhost, asdsk=True) #[{'feedback': {'_modern@confusion': {'cate': 
		[ arsnt.get('meta',{}).update({'offset': pair[1]})  for pair, arsnt in zip( pairs, dsk['snt']) ]
		dsk['info'].update(arr)
		return dsk 
	except Exception as ex:
		print(">>gecv1_dsk Ex:", ex, "\t|", arr)
		exc_type, exc_value, exc_traceback_obj = sys.exc_info()
		traceback.print_tb(exc_traceback_obj)
		return str(ex)

def consume(queue, host='172.17.0.1', port=5672, user='pigai', pwd='NdyX3KuCq', durable=True, heartbeat=60, prefetch_count=1, debug=False,
		essay_field = 'essay', gecon=True, topk_snts= 0, # when> 0, mean only topk snts considered 
		dsk_exchange="wps-dsk", routing_key="wps-dsk-to-callback", 
		essay_exchange = 'wps-essay', expired_routing_key="wps-essay-long", timeout=3, failed_routing_key="wps-essay-failed"):
	''' set timeout = -1, when long-essay '''
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
			arr		= json.loads(body.decode(), strict=False)
			dsk		= func_timeout( int(arr.get('timeout',timeout)) ,gecv1_dsk , args=(arr,)) if timeout > 0 else  gecv1_dsk(arr, gecon=gecon, topk_snts=topk_snts)  
			ch.basic_publish(exchange=arr.get('exchange', dsk_exchange), routing_key=arr.get("routing_key",routing_key), body=json.dumps(dsk))

			if debug: 
				tim = time.time()-start
				print ("==born:", len(dsk), " timing: ", tim , "\t", dsk, flush=True)
				if timeout > 0 and tim > timeout: print (">>slow ==\n", body.decode() )

		except FunctionTimedOut:
			ch.basic_publish(exchange=essay_exchange, routing_key=expired_routing_key, body=body.decode())
			print ("expired:\n", body.decode()) 

		except Exception as err:
			ch.basic_publish(exchange=essay_exchange, routing_key=failed_routing_key, body=body.decode())
			print("Failed:", err, "\n", body.decode())
			exc_type, exc_value, exc_traceback_obj = sys.exc_info()
			traceback.print_tb(exc_traceback_obj)
			return # dont ack 

		ch.basic_ack(delivery_tag = method.delivery_tag)

	print("begin to consume queue: ", queue, host, port, flush=True)
	channel.basic_consume(queue, callback, auto_ack=False)
	channel.start_consuming()

if __name__ == '__main__':
	#print(gecv1_dsk())
	fire.Fire(consume)

'''
$uniq = md5(uniqid(md5(microtime(true)),true));
$key = 'PG'.intval($token['user_id']).'_'.substr($token['client_id'], -6).'_'.$uniq;

class util(object):
	def __init__(self, host = '127.0.0.1', port=6379, db=0):
		redis.r = redis.Redis(host=host, port=port, db=db, decode_responses=True)

	def test(self):
		arr = {"key":"PG115_11bae9_cbc77946c457a6b8c7213890e1550ebc","rid":"861591","ct":1647955287.4181,"tit":"\u6587\u5b57\u6587\u7a3f1","doc":"In 2016, the year of the year for the entire live broadcast industry, most people took a wait-and-see approach.Then, with the growth of internet technology, more and more people became involved in live streaming, and that peaked in 2020.2020 has been impacted by the novel coronavirus pneumonia, and the boom in webcasting has been even more intense, with every industry poised to take its place on the air. The publishing industry is no exception. The boom in webcasting has had a huge impact on branding and marketing channels for books.Against this background, book streaming has emerged as an emerging sales model.As well as attracting the attention of consumers, live streaming also gives books more room to spread.At present, the live book has gradually formed the scale and been popularized rapidly, but it has many shortcomings and defects.As the platform with the largest number of livestreams in our country, Jibe is naturally favored by the book livestreaming industry.Based on the research and analysis of the current situation of live books on the buffeting platform, and combining data and examples, this paper summarizes the problems encountered in the course of development, including the number of anchors, the change of audience, the change of book types, the change of sales, the opening hours and hours, the number of live shows and the growth of fans, and puts forward some suggestions to solve the problems.\n\n","solution":[],"lang":"zh_cn","mq_name":"pigai_callback_api_essay","progress":"0","_token":{"access_token":"632405641da7e4b04c742a5f00bc8e787445da9d","client_id":"f29acd428d93ac8243aa5d6aef11bae9","user_id":"115","expires":1647960286,"scope":"all_json"},"meta_data":{"scope":"all_json"},"models":"nn"}
		key = arr['key']
		essay = arr['doc']
		redis.r.hmset(key, { k : json.dumps(v) if isinstance(v,dict) or isinstance(v, list) else v for k,v in arr.items() }) 

		sntpairs =  valid_snts(essay) # (snt, offset) 
		redis.r.hset(key, 'snts', json.dumps(sntpairs) )

		snts = [row[0] for row in sntpairs]
		sntdic = gecv1.gecsnts(snts) 
		print(sntdic) 
		res = mkf.sntsmkf({snt:snt for snt in snts}, dskhost='gpu120.wrask.com:7095', asdsk=True)
		print (res)
'''