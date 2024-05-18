import api
import subprocess
from slide3 import Slide3
import requests
import time
def main():
	slide3 = Slide3()
	cmd0 = "node -e \"require('./hack/rt.js').rt()\""
	print(cmd0)
	rt = subprocess.run(cmd0, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	(challenge, gt) = api.register()
	print(challenge)
	print(gt)
	cmd1 = "node -e \"require('./hack/w.js').send(" + "\'" + gt + "\',\'" + challenge + "\',\'" + rt + "\')\""
	print(cmd1)
	w = subprocess.run(cmd1, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(w)
	(c, s) = api.get_c_s(challenge, gt, w)
	cmd2 = "node -e \"require('./hack/ww.js').send(" + "\'" + gt + "\',\'" + challenge + "\',\'" + rt + "\')\""
	print(cmd2)
	w = subprocess.run(cmd2, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(w)
	api.get_type(challenge, gt, w)
	(challenge, bg_url, slice_url) = api.get_new_challenge_bg_slice(challenge, gt)
	dis = slide3.calculated_distance(bg_url, slice_url)
	print(dis)
	cmd3 = "node -e \"require('./hack/www.js').send(" + str(dis) + ",\'" + gt + "\',\'" + challenge + "\'," + str(c) + ",\'" + s + "\',\'"+ rt + "\')\""
	print(cmd3)
	w = subprocess.run(cmd3, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(w)
	time.sleep(2)
	res = api.ajax(challenge, gt, w)
	print(res)
 
def main1():
	cmd0 = "node -e \"require('./hack/rt.js').rt()\""
	print(cmd0)
	rt = subprocess.run(cmd0, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	(challenge, gt) = api.register()
	cmd1 = "node -e \"require('./hack/w.js').send(" + "\'" + gt + "\',\'" + challenge + "\',\'" + rt + "\')\""
	print(cmd1)
	w = subprocess.run(cmd1, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(w)
	(c, s) = api.get_c_s(challenge, gt, w)

def main2():
	slide3 = Slide3()
	cmd0 = "node -e \"require('./hack/rt.js').rt()\""
	print(cmd0)
	rt = subprocess.run(cmd0, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	rt = "380a363aac234049"
	challenge = "359ec7be639cc637a4fd42e63e4e469d	"
	gt = "4d91184f0308d36a3bc4b2b01b845a6b"
	c =  [12, 58, 98, 36, 43, 95, 62, 15, 12]
	s = "64617357"
	
	cmd2 = "node -e \"require('./hack/ww.js').send(\'" + rt + "\')\""
	print(cmd2)
	w = subprocess.run(cmd2, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(w)
	api.get_type(challenge, gt, w)


	time.sleep(1)
	(challenge, bg_url, slice_url) = api.get_new_challenge_bg_slice(challenge, gt)
	dis = slide3.calculated_distance(bg_url, slice_url)
	print(dis)
	
	
	cmd3 = "node -e \"require('./hack/www.js').send(" + str(dis) + ",\'" + gt + "\',\'" + challenge + "\'," + str(c) + ",\'" + s + "\',\'"+ rt + "\')\""
	print(cmd3)
	w = subprocess.run(cmd3, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	time.sleep(5)
	res = api.ajax(challenge, gt, w)
	print(res)


def main3():
	slide3 = Slide3()
	suc = 0
	fail = 0
	while suc < 100:
		print(suc)
		print(fail)
		cmd0 = "node -e \"require('./hack/rt.js').rt()\""
		# print(cmd0)
		rt = subprocess.run(cmd0, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
		(challenge, gt) = api.register()

		# print(challenge)
		# print(gt)
		# cmd1 = "node -e \"require('./hack/w.js').send(" + "\'" + gt + "\',\'" + challenge + "\',\'" + rt + "\')\""
		# print(cmd1)
		# w = subprocess.run(cmd1, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
		# print(w)
		(c, s) = api.get_c_s(challenge, gt, None)

		# cmd2 = "node -e \"require('./hack/ww.js').send(\'" + rt + "\')\""
		# print(cmd2)
		# w = subprocess.run(cmd2, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
		# print(w)
		api.get_type(challenge, gt, None)

		(c, s, challenge, bg_url, slice_url) = api.get_new_c_s_challenge_bg_slice(challenge, gt)
		dis = slide3.calculated_distance(bg_url, slice_url)
		cmd3 = "node -e \"require('./hack/www.js').send(" + str(dis) + ",\'" + gt + "\',\'" + challenge + "\'," + str(c) + ",\'" + s + "\',\'"+ rt + "\')\""
		# print(cmd3)
		w = subprocess.run(cmd3, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
		time.sleep(0.2)
		res = api.ajax(challenge, gt, w)
		if res['success'] == 1:
			suc += 1
		else:
			fail += 1
		
	print(suc / (suc + fail))

def main4():
	slide3 = Slide3()

	cmd0 = "node -e \"require('./hack/rt.js').rt()\""
	print(cmd0)
	rt = subprocess.run(cmd0, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	(challenge, gt) = api.register()

	print(challenge)
	print(gt)
	cmd1 = "node -e \"require('./hack/w.js').send(" + "\'" + gt + "\',\'" + challenge + "\',\'" + rt + "\')\""
	print(cmd1)
	w = subprocess.run(cmd1, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(w)
	(c, s) = api.get_c_s(challenge, gt, w)

	cmd2 = "node -e \"require('./hack/ww.js').send(" + "\'" + gt + "\',\'" + challenge + "\',\'" + rt + "\')\""
	print(cmd2)
	w = subprocess.run(cmd2, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	print(w)
	api.get_type(challenge, gt, None)

	(c, s, challenge, bg_url, slice_url) = api.get_new_c_s_challenge_bg_slice(challenge, gt)
	dis = slide3.calculated_distance(bg_url, slice_url)
	cmd3 = "node -e \"require('./hack/www.js').send(" + str(dis) + ",\'" + gt + "\',\'" + challenge + "\'," + str(c) + ",\'" + s + "\',\'"+ rt + "\')\""
	print(cmd3)
	w = subprocess.run(cmd3, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
	time.sleep(2)
	res = api.ajax(challenge, gt, w)
	print(res)
	
if __name__ == '__main__':
    main4()