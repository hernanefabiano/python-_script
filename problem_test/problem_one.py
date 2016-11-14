#! /usr/bin/python
import timeit

def timeit(func):
    clock = (sys.platform == "win32" and time.clock or time.time)

    def wrapper(*args, **kw):
        start_time = clock()
        try:
            return func(*args, **kw)
        finally:
            total_time = clock() - start_time
            print "%s took %.3fs" % (func.func_name, total_time)
    return wrapper
    
def problem_one(num_list, len_list):
	print "\nnum_list", num_list
	
	# initialize the value of range of new datatype
	num_dict = {
		'lowest': 0, 'highest': 0
	}

	for num in num_list:
		if num:
			if num < num_dict.get('lowest'):
				num_dict['lowest'] = num
			if num > num_dict.get('highest'):
				num_dict['highest'] = num
			if num in num_dict.keys():
				num_dict[num] = num_dict.get(num) + 1
			else:
				num_dict[num] = 1

	print '\nRange is {0} - {1}\n'.format(num_dict['lowest'], num_dict['highest'])
	print 'Missing Numbers:'
	for digit in xrange(num_dict.get('lowest'), num_dict.get('highest')):
	

		if digit not in num_list:
			print '{0:3}'.format(digit)

	print '\nDuplicate Numbers:'
	for key, val in num_dict.iteritems():
		if key not in ['lowest', 'highest']:
			print '{0:3} appears {1} times'.format(key, val)
	
def problem_two():
	'''
	open the xls file for the answers
	'''
	pass

def problem(num_list, len_list):
	print "\nnum_list", num_list
	
	# initialize the value of range of new datatype
	num_dict = {
		'lowest': 0, 'highest': 1
	}

	for num in num_list:
		if num:
			if num < num_dict.get('lowest'):
				num_dict['lowest'] = num
			if num > num_dict.get('highest'):
				num_dict['highest'] = num
			if num in num_dict.keys():
				num_dict[num] = num_dict.get(num) + 1
			else:
				num_dict[num] = 1

	print '\nRange is {0} - {1}\n'.format(num_dict['lowest'], num_dict['highest'])
	print 'Missing Numbers:'
	for digit in xrange(num_dict.get('lowest'), num_dict.get('highest')):
			if digit not in num_list:
				print '{0:3}'.format(digit)

	print '\nDuplicate Numbers:'
	for key, val in num_dict.iteritems():
		if key not in ['lowest', 'highest']:
			print '{0:3} appears {1} times'.format(key, val)

def linearFibonacci(n):
	fn = f1 = f2 = 1
	for x in xrange(2, n):
		fn = f1 + f2
		f2, f1 = f1, fn

		print 'f1', f1
		print 'f2', f2
		print 'fn', fn
		
	return fn

def firstn(n):
	num = 0
	while num < n:
		yield num
		num += 1

if __name__ == "__main__":
	#print linearFibonacci(20)
	#list_data = [100000] #[3, 1, -5, 3, 3, -5, 0, 10, 1, 1]
	#problem(list_data, len(list_data))
	sum_of_first_n = sum(firstn(1000000))
	print sum_of_first_n