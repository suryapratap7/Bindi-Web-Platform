from django.shortcuts import render
from django.http import HttpResponse
from .models import Programs
import json, urllib

# Create your views here.

check=0;
code_id_map=dict()
degree=""




def page2view(request):

	course_list=list()
	idList = list()
	code_list=list()
	idList2= list()
	code_list_new= list()
	newList=list()
	
	


	if request.method=='GET':
		url= "https://cims.cecs.anu.edu.au/api/course/"
		response= urllib.urlopen(url)
		data=json.loads(response.read())

		for course in data:
			##for key in career.iteritems():
			##career=data['results'][x] ['career']
			code = course['code']
			idl = course['id']

			#code_id_map= dict({idl:code})
			#code_id_map.update({code:idl})
			course_list.append(idl)
			
			course_list.append(code)

			
			global check 

			check = request.GET['start_year']

			global degree

			degree = request.GET['degree']

			
	# 		context={
       
 #       			"start_year":request.GET['start_year'],

 #       			'code_id_map': code_id_map
	# }

	if request.method=='GET':
		url= "https://cims.cecs.anu.edu.au/api/courseinstance/"
		response= urllib.urlopen(url)
		data=json.loads(response.read())

		for row in data:
			##for key in career.iteritems():
			##career=data['results'][x] ['career']
			if row['teachingsession']== 2:
				idList.append(row['id'])

			if row['teachingsession']== 1:
				idList2.append(row['id'])	



        if degree=='MASTERS':
        
				
    		for i in range (len(course_list)):
    			for row_id in idList:
    			
    				if (row_id == course_list[i]) and course_list[i+1][4]>="6" and course_list[i+1][4]<="8":
    					code_list.append(course_list[i+1])

    			for row_id_i in idList2:
    				if row_id_i == course_list[i] and course_list[i+1][4]>="6" and course_list[i+1][4]<="8":
    					code_list_new.append(course_list[i+1])	
    	else:
    	
    		for i in range (len(course_list)):
    			for row_id in idList:
    			
    				if (row_id == course_list[i]) and course_list[i+1][4]>="1" and course_list[i+1][4]<="5":
    					code_list.append(course_list[i+1])

    			for row_id_i in idList2:
    				if row_id_i == course_list[i] and course_list[i+1][4]>="1" and course_list[i+1][4]<="5":
    					code_list_new.append(course_list[i+1])	



    	context = {
       
       			"start_year":request.GET['start_year'],

       			'code_list': code_list,

       			'code_list_new': code_list_new,
       			'newList': newList
		}			
    			
			

	return render(request, "page2.html", context)

def index(request):
	programs= Programs.objects.all()
	academic_career=list()

	if request.method=='GET':

		url = "https://cims.cecs.anu.edu.au/api/academiccareer/"
		response= urllib.urlopen(url)
		data=json.loads(response.read())

		##for row in data:

		
        for career in data:
			##for key in career.iteritems():
			##career=data['results'][x] ['career']
			academic_career.append(career['career'])

			context = {

			 'academic_career': academic_career,
			 'programs':programs
 



			}
	##num=random.randint(0,10000000)
	return render(request, "base.html", context)

def page3view(request):

	course_list=list()
	idList = list()
	code_list=list()
	idList2= list()
	code_list_new= list()
	
	


	if request.method=='GET':
		url= "https://cims.cecs.anu.edu.au/api/course/"
		response= urllib.urlopen(url)
		data=json.loads(response.read())

		for course in data:
			##for key in career.iteritems():
			##career=data['results'][x] ['career']
			code = course['code']
			idl = course['id']

			#code_id_map= dict({idl:code})
			#code_id_map.update({code:idl})
			course_list.append(idl)
			course_list.append(code)
		

	if request.method=='GET':
		url= "https://cims.cecs.anu.edu.au/api/courseinstance/"
		response= urllib.urlopen(url)
		data=json.loads(response.read())

		for row in data:
			##for key in career.iteritems():
			##career=data['results'][x] ['career']
			if row['teachingsession']== 2:
				idList.append(row['id'])

			if row['teachingsession']== 1:
				idList2.append(row['id'])	


				
    	if degree=='MASTERS':
        
				
    		for i in range (len(course_list)):
    			for row_id in idList:
    			
    				if (row_id == course_list[i]) and course_list[i+1][4]>="6" and course_list[i+1][4]<="8":
    					code_list.append(course_list[i+1])

    			for row_id_i in idList2:
    				if row_id_i == course_list[i] and course_list[i+1][4]>="6" and course_list[i+1][4]<="8":
    					code_list_new.append(course_list[i+1])	
    	else:
    	
    		for i in range (len(course_list)):
    			for row_id in idList:
    			
    				if (row_id == course_list[i]) and course_list[i+1][4]>="1" and course_list[i+1][4]<="5":
    					code_list.append(course_list[i+1])

    			for row_id_i in idList2:
    				if row_id_i == course_list[i] and course_list[i+1][4]>="1" and course_list[i+1][4]<="5":
    					code_list_new.append(course_list[i+1])	
		


    	context = {
       
       			"check": check,

       			'code_list': code_list,

       			'code_list_new': code_list_new
		}			
    			
	
	return render(request, "page3.html",context)


def page4view(request):

	context = {

		"check":check


	}

	return render(request, "extra.html",context)	



	







