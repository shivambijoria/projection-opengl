#bijoria,shivam
#1001359394
#2016-04-29
#Assignment_05
from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from numpy import *
import threading
#import time
#import math
import Tkinter as tk
#from tkinter import filedialog
#import os
import math
#global matrix
#matrix=[[5.5 for i in range(4)] for j in range(4)]
global vupstoragecounter
vupstoragecounter=0
global filename
filename='pyramid_05.txt'
print('Loading and displaying %s'%filename)
  
def create_pyramid():
	global Vertex
	global vertexcount
	global Face
	global Facecount
	

	glNewList(1,GL_COMPILE)
	glBegin(GL_LINES)
      
	
    
	totalnumberfaces=len(Face)
	for facenumber in range (0,totalnumberfaces-1):
    
		vertex1=Face[facenumber][0]
		vertex2=Face[facenumber][1]
		vertex3=Face[facenumber][2]
        
		glVertex3f(Vertex[vertex1][0],Vertex[vertex1][1],Vertex[vertex1][2]);
		glVertex3f(Vertex[vertex2][0],Vertex[vertex2][1],Vertex[vertex2][2]);
	    
		glVertex3f(Vertex[vertex3][0],Vertex[vertex3][1],Vertex[vertex3][2]);
		glVertex3f(Vertex[vertex2][0],Vertex[vertex2][1],Vertex[vertex2][2]);
		
		glVertex3f(Vertex[vertex1][0],Vertex[vertex1][1],Vertex[vertex1][2]);
		glVertex3f(Vertex[vertex3][0],Vertex[vertex3][1],Vertex[vertex3][2]);
		
		     
	glEnd() 
	glEndList()   
     
   
def display():
	global camera_identity
	global camera_type
	global camera_eye
	global camera_look
	global camera_vup
	global camera_wcs
	global camera_s_or_viewport
	global total_camera_count_ai
	#print('above')
	glClearColor(0,0,1,1)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	#print('below')
	for i in range(0,total_camera_count_ai+1):
		
		glFlush();
		w=glutGet(GLUT_WINDOW_WIDTH)
		h=glutGet(GLUT_WINDOW_HEIGHT)
		
		glEnable(GL_SCISSOR_TEST)
		glScissor(int(camera_s_or_viewport[i][0]*w),int(camera_s_or_viewport[i][1]*h),int((camera_s_or_viewport[i][2]-camera_s_or_viewport[i][0])*w),int((camera_s_or_viewport[i][3]-camera_s_or_viewport[i][1])*h))
		glClearColor(1,0,0,1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		if(camera_type[i]=='parallel'):
			glOrtho(camera_wcs[i][0],camera_wcs[i][1],camera_wcs[i][2],camera_wcs[i][3],camera_wcs[i][4],camera_wcs[i][5])
		else:
			glFrustum(camera_wcs[i][0],camera_wcs[i][1],camera_wcs[i][2],camera_wcs[i][3],camera_wcs[i][4],camera_wcs[i][5])
		gluLookAt(camera_eye[i][0],camera_eye[i][1],camera_eye[i][2],camera_look[i][0],camera_look[i][1],camera_look[i][2],camera_vup[i][0],camera_vup[i][1],camera_vup[i][2])
		glMatrixMode(GL_MODELVIEW)    
		glViewport(int(camera_s_or_viewport[i][0]*w),int(camera_s_or_viewport[i][1]*h),int((camera_s_or_viewport[i][2]-camera_s_or_viewport[i][0])*w),int((camera_s_or_viewport[i][3]-camera_s_or_viewport[i][1])*h))
		glCallList(1)
		
		#glPushMatrix()
		#glLoadIdentity()
		#glPopMatrix()
        
		glFlush();
		glutSwapBuffers()                             
	glDisable(GL_SCISSOR_TEST)
	
	#glLoadIdentity()
   #matrix=glGetFloatv (GL_MODELVIEW_MATRIX);
   #print(matrix)
   #print('---------display--------')

def reshape(w,h):
	za=0
	#print('in reshape')
	
	#glClearColor(0,0.0,1.0,1)
	#glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   #glClearColor(1,1.0,0.0,1)
   #glClear(GL_COLOR_BUFFER_BIT )
   #glLoadIdentity()
   
   #global matrix
   #glClearColor(1,0,0,1)
   #glViewport(0, 0,w,h); 
   #glMatrixMode(GL_PROJECTION);
   #glLoadIdentity();
   #glFrustum(-2.0, 2.0, -3.0, 3.0, 5, 20.0);
   #glMatrixMode(GL_MODELVIEW);
   #matrix=glGetFloatv (GL_MODELVIEW_MATRIX);
   #print(matrix)
   #print('---------reshape--------')
 
   

def main():

   glutInit();
   glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB|GLUT_DEPTH)
   glutInitWindowSize(500, 500); 
   glutInitWindowPosition(100, 100);
   glutCreateWindow('oh ho');
   glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
   glEnable(GL_DEPTH_TEST)
   glDepthFunc(GL_LESS);
   #init();
   glutDisplayFunc(display); 
   glutReshapeFunc(reshape);
   glutKeyboardFunc(operations)
   glutSpecialFunc(directionkeyshit)
   create_pyramid()
   glutMainLoop();
   return 0;

def read_cameratxt_file():
#declaration
	
		
	#file line counting and opening
	f1=open('cameras_05.txt', 'r')
	filesize=len(f1.readlines())
	
	f1.close()
	f2=open('cameras_05.txt', 'r')
	
	global total_camera_count_ai
	total_camera_count_ai=-1
	
	
	for i in range (0,filesize):
			readingline=f2.readline()
			if(readingline[0]=='c'):
				total_camera_count_ai=total_camera_count_ai+1
	
	f2.close()
	#print('camera count %d'%total_camera_count_ai)
	
	global camera_identity
	global camera_type
	global camera_eye
	global camera_look
	global camera_vup
	global camera_wcs
	global camera_s_or_viewport
	global vupstoragecounter
	global vup_axis_for_up_and_down
	vup_axis_for_up_and_down=[[0 for h in range(3)] for fg in range(total_camera_count_ai+1)]	
	vupstoragecounter=0
	camera_identity=['' for i in range (total_camera_count_ai+1)]
	camera_type=['parallel' for i in range (total_camera_count_ai+1)]
	
	camera_eye=[[0 for i in range(3)] for j in range(total_camera_count_ai+1)]
	camera_look=[[0 for i in range(3)] for j in range(total_camera_count_ai+1)]
	camera_vup=[[0 for i in range(3)] for j in range(total_camera_count_ai+1)]
	camera_wcs=[[0 for i in range(6)] for j in range(total_camera_count_ai+1)]
	camera_s_or_viewport=[[0 for i in range(4)] for j in range(total_camera_count_ai+1)]
	
	f3=open('cameras_05.txt', 'r')
	global current_camera_count_index
	current_camera_count_index=-1
	
	#parsing and storing file
	def parse_file_and_store_the_information():
		global camera_identity
		global camera_type
		global camera_eye
		global camera_look
		global camera_vup
		global camera_wcs
		global camera_s_or_viewport
		global current_camera_count_index
		for i in range (0,filesize):
			#print('---- %d'%i)
			readingline=f3.readline()
			if(readingline[0]=='c'):
      
				current_camera_count_index=current_camera_count_index+1
				#print('--- %d'%current_camera_count_index)
			if(readingline[0]=='i'):
      
				readinglinewithouti=readingline[1:]
				ifloats = [str(x) for x in readinglinewithouti.split()]
				camera_identity[current_camera_count_index]=ifloats[0]
				
			if(readingline[0]=='t'):
      
				readinglinewithouti=readingline[1:]
				tfloats = [str(x) for x in readinglinewithouti.split()]
				camera_type[current_camera_count_index]=tfloats[0]
				
				
			if(readingline[0]=='w'):
				readinglinewithoutw=readingline[1:]
				wfloats = [float(x) for x in readinglinewithoutw.split()]
				camera_wcs[current_camera_count_index][0]=wfloats[0]
				camera_wcs[current_camera_count_index][1]=wfloats[1]
				camera_wcs[current_camera_count_index][2]=wfloats[2]
				camera_wcs[current_camera_count_index][3]=wfloats[3]
				camera_wcs[current_camera_count_index][4]=wfloats[4]#nmin
				camera_wcs[current_camera_count_index][5]=wfloats[5]#nmax
				#print ('WCSYmax is %d',WCSYmax)
			if(readingline[0]=='s'):  
				readinglinewithouts=readingline[1:]
				vfloats = [float(x) for x in readinglinewithouts.split()]
				camera_s_or_viewport[current_camera_count_index][0]=vfloats[0]
				camera_s_or_viewport[current_camera_count_index][1]=vfloats[1]
				camera_s_or_viewport[current_camera_count_index][2]=vfloats[2]
				camera_s_or_viewport[current_camera_count_index][3]=vfloats[3]
			if(readingline[0]=='e'):  
				readinglinewithouts=readingline[1:]
				vrpfloats = [float(x) for x in readinglinewithouts.split()]
				camera_eye[current_camera_count_index][0]=vrpfloats[0]
				camera_eye[current_camera_count_index][1]=vrpfloats[1]
				camera_eye[current_camera_count_index][2]=vrpfloats[2]
				
			if(readingline[0]=='l'):  
				readinglinewithouts=readingline[1:]
				vpnfloats = [float(x) for x in readinglinewithouts.split()]
				camera_look[current_camera_count_index][0]=vpnfloats[0]
				camera_look[current_camera_count_index][1]=vpnfloats[1]
				camera_look[current_camera_count_index][2]=vpnfloats[2]
				
			if(readingline[0]=='u'):  
				readinglinewithouts=readingline[1:]
				vupfloats = [float(x) for x in readinglinewithouts.split()]
				camera_vup[current_camera_count_index][0]=vupfloats[0]
				camera_vup[current_camera_count_index][1]=vupfloats[1]
				camera_vup[current_camera_count_index][2]=vupfloats[2]
				
			
	parse_file_and_store_the_information()
	f3.close


def read_input_file():
#declaration
    global Vertex
    global vertexcount
    global Face
    global Facecount
    global filename
	
    Vertex = [[0 for x in range(3)]]
    vertexcount=1
    Face = [[]]
    Facecount=0

    #file line counting and opening
    f1=open(filename, 'r')
    filesize=len(f1.readlines())
    
    f1.close()
    f=open(filename, 'r')




    #parsing and storing file
    for i in range (0,filesize):
        readingline=f.readline()
        if(readingline[0]=='v'):
      
            readinglinewithoutv=readingline[1:]
            vertexfloats = [float(x) for x in readinglinewithoutv.split()]
            #Vertex[vertexcount][0]=vertexfloats[0]
            #Vertex[vertexcount][1]=vertexfloats[1]
            #Vertex[vertexcount][2]=vertexfloats[2]
            Vertex.insert(vertexcount,[vertexfloats[0],vertexfloats[1],vertexfloats[2]])
            
            vertexcount=vertexcount+1
        if(readingline[0]=='f'):
      
            readinglinewithoutf=readingline[1:]
            faceintegers = [int(x) for x in readinglinewithoutf.split()]
            #Face[Facecount][0]=faceintegers[0]
            #Face[Facecount][1]=faceintegers[1]
            #Face[Facecount][2]=faceintegers[2]
            Face.insert(Facecount,[faceintegers[0],faceintegers[1],faceintegers[2]])
            
            Facecount=Facecount+1
           
    f.close()

def directionkeyshit(Key, MouseX, MouseY):
		if Key == GLUT_KEY_LEFT: 
			for i in range(0,total_camera_count_ai+1):
				#print('--camera---')
				#print( camera_eye[i])
				
				#print( camera_look[i])
				subtracted_look=[0 for j in range(0,3)]
				subtracted_look[0]=camera_look[i][0]-camera_eye[i][0]
				subtracted_look[1]=camera_look[i][1]-camera_eye[i][1]
				subtracted_look[2]=camera_look[i][2]-camera_eye[i][2]
				#print( subtracted_look)
				
				unit_vector_in_eye_direction=[0 for k in range(0,3)]
				unit_vector_in_eye_direction[0]=-1*subtracted_look[0]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[1]=-1*subtracted_look[1]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[2]=-1*subtracted_look[2]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				
				#print(( camera_eye[i][0]*camera_eye[i][0]  + camera_eye[i][1]*camera_eye[i][1]  + camera_eye[i][2]*camera_eye[i][2]  ))
			
				distance=  math.sqrt ( subtracted_look[0]*subtracted_look[0]  +  subtracted_look[1]*subtracted_look[1]  +  subtracted_look[2]*subtracted_look[2]  ) 
				distance=distance*.05
				#print('-------)-')
				#print(distance)
				
				#calculating u axis
				zaxis=[0 for aa in range(0,3)]
				zaxis[0]=camera_look[i][0]-camera_eye[i][0]
				zaxis[1]=camera_look[i][1]-camera_eye[i][1]
				zaxis[2]=camera_look[i][2]-camera_eye[i][2]
				
				
				
				uaxis=[0 for ab in range(0,3)]
				uaxis[0]=camera_vup[i][1]*zaxis[2]-camera_vup[i][2]*zaxis[1]
				uaxis[1]=camera_vup[i][2]*zaxis[0]-camera_vup[i][0]*zaxis[2]
				uaxis[2]=camera_vup[i][0]*zaxis[1]-camera_vup[i][1]*zaxis[0]
				
				#unit vector in u direction
				unit_vector_in_u_direction=[0 for ac in range(0,3)]
				unit_vector_in_u_direction[0]=uaxis[0]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[1]=uaxis[1]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[2]=uaxis[2]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
			
				
				
				
				#noew camera location after movement in u direction
				camera_eye[i][0]=(unit_vector_in_u_direction[0]*distance)+ camera_eye[i][0]
				camera_eye[i][1]=(unit_vector_in_u_direction[1]*distance)+ camera_eye[i][1]
				camera_eye[i][2]=(unit_vector_in_u_direction[2]*distance)+ camera_eye[i][2]
				#print('--camera_eye---')
				#print(camera_eye[i])
				#print('----camera eye-----')
				#print(camera_eye[i])
			display()
		if Key == GLUT_KEY_RIGHT: 
			for i in range(0,total_camera_count_ai+1):
				#print('--camera---')
				#print( camera_eye[i])
				
				#print( camera_look[i])
				subtracted_look=[0 for j in range(0,3)]
				subtracted_look[0]=camera_look[i][0]-camera_eye[i][0]
				subtracted_look[1]=camera_look[i][1]-camera_eye[i][1]
				subtracted_look[2]=camera_look[i][2]-camera_eye[i][2]
				#print( subtracted_look)
				
				unit_vector_in_eye_direction=[0 for k in range(0,3)]
				unit_vector_in_eye_direction[0]=-1*subtracted_look[0]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[1]=-1*subtracted_look[1]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[2]=-1*subtracted_look[2]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				
				#print(( camera_eye[i][0]*camera_eye[i][0]  + camera_eye[i][1]*camera_eye[i][1]  + camera_eye[i][2]*camera_eye[i][2]  ))
			
				distance=  math.sqrt ( subtracted_look[0]*subtracted_look[0]  +  subtracted_look[1]*subtracted_look[1]  +  subtracted_look[2]*subtracted_look[2]  ) 
				distance=distance*.05*(-1)
				#print('-------)-')
				#print(distance)
				
				#calculating u axis
				zaxis=[0 for aa in range(0,3)]
				zaxis[0]=camera_look[i][0]-camera_eye[i][0]
				zaxis[1]=camera_look[i][1]-camera_eye[i][1]
				zaxis[2]=camera_look[i][2]-camera_eye[i][2]
				
				
				
				uaxis=[0 for ab in range(0,3)]
				uaxis[0]=camera_vup[i][1]*zaxis[2]-camera_vup[i][2]*zaxis[1]
				uaxis[1]=camera_vup[i][2]*zaxis[0]-camera_vup[i][0]*zaxis[2]
				uaxis[2]=camera_vup[i][0]*zaxis[1]-camera_vup[i][1]*zaxis[0]
				
				#unit vector in u direction
				unit_vector_in_u_direction=[0 for ac in range(0,3)]
				unit_vector_in_u_direction[0]=uaxis[0]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[1]=uaxis[1]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[2]=uaxis[2]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
			
				
				
				
				#noew camera location after movement in u direction
				camera_eye[i][0]=(unit_vector_in_u_direction[0]*distance)+ camera_eye[i][0]
				camera_eye[i][1]=(unit_vector_in_u_direction[1]*distance)+ camera_eye[i][1]
				camera_eye[i][2]=(unit_vector_in_u_direction[2]*distance)+ camera_eye[i][2]
				#print('--camera_eye---')
				#print(camera_eye[i])
				#print('----camera eye-----')
				#print(camera_eye[i])
			display()
		if Key == GLUT_KEY_UP: 
			global vupstoragecounter
			global vup_axis_for_up_and_down
			for t in range(0,total_camera_count_ai+1):
				if vupstoragecounter==0 :
					
					vup_axis_for_up_and_down[t][0]=camera_vup[t][0]
					vup_axis_for_up_and_down[t][1]=camera_vup[t][1]
					vup_axis_for_up_and_down[t][2]=camera_vup[t][2]
			vupstoragecounter=1
			#for e in range(0,total_camera_count_ai+1):
			#	print(vup_axis_for_up_and_down[e])
			for i in range(0,total_camera_count_ai+1):
				#print('--camera---')
				#print( camera_eye[i])
				
				#print( camera_look[i])
				subtracted_look=[0 for j in range(0,3)]
				subtracted_look[0]=camera_look[i][0]-camera_eye[i][0]
				subtracted_look[1]=camera_look[i][1]-camera_eye[i][1]
				subtracted_look[2]=camera_look[i][2]-camera_eye[i][2]
				#if i==0:
				#	print('--subtracted look---')
				#	print(subtracted_look)
				
				unit_vector_in_eye_direction=[0 for k in range(0,3)]
				unit_vector_in_eye_direction[0]=-1*subtracted_look[0]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[1]=-1*subtracted_look[1]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[2]=-1*subtracted_look[2]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				#if i==0:
				#	print('---unit_vector_in_eye_direction--')
				#	print(unit_vector_in_eye_direction)
				
				#print(( camera_eye[i][0]*camera_eye[i][0]  + camera_eye[i][1]*camera_eye[i][1]  + camera_eye[i][2]*camera_eye[i][2]  ))
			
				distance=  math.sqrt ( subtracted_look[0]*subtracted_look[0]  +  subtracted_look[1]*subtracted_look[1]  +  subtracted_look[2]*subtracted_look[2]  ) 
				#if i==0:
				#	print('---distance--')
				#	print(distance)
				
				distance=distance*.05
				#print('-------)-')
				#print(distance)
				#if i==0:
				#	print('--camera-look--')
				#	print(camera_look[i])
				#calculating u axis
				zaxis=[0 for aa in range(0,3)]
				zaxis[0]=camera_eye[i][0]-camera_look[i][0]
				zaxis[1]=camera_eye[i][1]-camera_look[i][1]
				zaxis[2]=camera_eye[i][2]-camera_look[i][2]
				#if i==0:
				#	print('---zaxis--')
				#	print(zaxis)
				
				
				uaxis=[0 for ab in range(0,3)]
				uaxis[0]=vup_axis_for_up_and_down[i][1]*zaxis[2]-vup_axis_for_up_and_down[i][2]*zaxis[1]
				uaxis[1]=vup_axis_for_up_and_down[i][2]*zaxis[0]-vup_axis_for_up_and_down[i][0]*zaxis[2]
				uaxis[2]=vup_axis_for_up_and_down[i][0]*zaxis[1]-vup_axis_for_up_and_down[i][1]*zaxis[0]
				uaxis[0]=uaxis[0]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				uaxis[1]=uaxis[1]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				uaxis[2]=uaxis[2]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				#if i==0:
				#	print('---uaxis--')
				#	print(uaxis)
				
				
				#unit vector in u direction
				unit_vector_in_u_direction=[0 for ac in range(0,3)]
				unit_vector_in_u_direction[0]=uaxis[0]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[1]=uaxis[1]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[2]=uaxis[2]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				
				
				
				
				
				
				
				#calculating vup
				vup_axis_for_up_and_down[i][0]=zaxis[1]*uaxis[2]-zaxis[2]*uaxis[1]
				vup_axis_for_up_and_down[i][1]=zaxis[2]*uaxis[0]-zaxis[0]*uaxis[2]
				vup_axis_for_up_and_down[i][2]=zaxis[0]*uaxis[1]-zaxis[1]*uaxis[0]
				vup_axis_for_up_and_down[i][0]=vup_axis_for_up_and_down[i][0]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				vup_axis_for_up_and_down[i][1]=vup_axis_for_up_and_down[i][1]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				vup_axis_for_up_and_down[i][2]=vup_axis_for_up_and_down[i][2]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				#if i==0:
				#	print('---vup_axis_for_up_and_down[i]--')
				#	print(vup_axis_for_up_and_down[i])
				
				
				
				
				#unit vector in vup_axis_for_up_and_down[i] direction
				unit_vector_in_vup_axis_direction=[0 for ac in range(0,3)]
				unit_vector_in_vup_axis_direction[0]=vup_axis_for_up_and_down[i][0]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				unit_vector_in_vup_axis_direction[1]=vup_axis_for_up_and_down[i][1]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				unit_vector_in_vup_axis_direction[2]=vup_axis_for_up_and_down[i][2]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				#if i==0:
				#	print('---vunit_vector_in_vup_axis_for_up_and_down[i]_direction--')
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction)
				
				
				
	
				#noew camera location after movement in u direction
				camera_eye[i][0]=(unit_vector_in_vup_axis_direction[0]*distance)+ camera_eye[i][0]
				camera_eye[i][1]=(unit_vector_in_vup_axis_direction[1]*distance)+ camera_eye[i][1]
				camera_eye[i][2]=(unit_vector_in_vup_axis_direction[2]*distance)+ camera_eye[i][2]
				#print('--camera_eye---')
				#print(camera_eye[i])
				#if i==0:
				#	print(camera_eye[i])
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction[0])
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction[1])
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction[2])
				#	print('----------------------------------------------------------------------------')
			display()
		if Key == GLUT_KEY_DOWN: 
			global vupstoragecounter
			global vup_axis_for_up_and_down
			for t in range(0,total_camera_count_ai+1):
				if vupstoragecounter==0 :
					
					vup_axis_for_up_and_down[t][0]=camera_vup[t][0]
					vup_axis_for_up_and_down[t][1]=camera_vup[t][1]
					vup_axis_for_up_and_down[t][2]=camera_vup[t][2]
			vupstoragecounter=1
			#for e in range(0,total_camera_count_ai+1):
			#	print(vup_axis_for_up_and_down[e])
			for i in range(0,total_camera_count_ai+1):
				#print('--camera---')
				#print( camera_eye[i])
				
				#print( camera_look[i])
				subtracted_look=[0 for j in range(0,3)]
				subtracted_look[0]=camera_look[i][0]-camera_eye[i][0]
				subtracted_look[1]=camera_look[i][1]-camera_eye[i][1]
				subtracted_look[2]=camera_look[i][2]-camera_eye[i][2]
				#if i==0:
				#	print('--subtracted look---')
				#	print(subtracted_look)
				
				unit_vector_in_eye_direction=[0 for k in range(0,3)]
				unit_vector_in_eye_direction[0]=-1*subtracted_look[0]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[1]=-1*subtracted_look[1]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[2]=-1*subtracted_look[2]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				#if i==0:
				#	print('---unit_vector_in_eye_direction--')
				#	print(unit_vector_in_eye_direction)
				
				#print(( camera_eye[i][0]*camera_eye[i][0]  + camera_eye[i][1]*camera_eye[i][1]  + camera_eye[i][2]*camera_eye[i][2]  ))
			
				distance=  math.sqrt ( subtracted_look[0]*subtracted_look[0]  +  subtracted_look[1]*subtracted_look[1]  +  subtracted_look[2]*subtracted_look[2]  ) 
				#if i==0:
				#	print('---distance--')
				#	print(distance)
				
				distance=distance*.05*-1
				#print('-------)-')
				#print(distance)
				#if i==0:
				#	print('--camera-look--')
				#	print(camera_look[i])
				#calculating u axis
				zaxis=[0 for aa in range(0,3)]
				zaxis[0]=camera_eye[i][0]-camera_look[i][0]
				zaxis[1]=camera_eye[i][1]-camera_look[i][1]
				zaxis[2]=camera_eye[i][2]-camera_look[i][2]
				#if i==0:
				#	print('---zaxis--')
				#	print(zaxis)
				
				
				uaxis=[0 for ab in range(0,3)]
				uaxis[0]=vup_axis_for_up_and_down[i][1]*zaxis[2]-vup_axis_for_up_and_down[i][2]*zaxis[1]
				uaxis[1]=vup_axis_for_up_and_down[i][2]*zaxis[0]-vup_axis_for_up_and_down[i][0]*zaxis[2]
				uaxis[2]=vup_axis_for_up_and_down[i][0]*zaxis[1]-vup_axis_for_up_and_down[i][1]*zaxis[0]
				uaxis[0]=uaxis[0]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				uaxis[1]=uaxis[1]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				uaxis[2]=uaxis[2]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				#if i==0:
				#	print('---uaxis--')
				#	print(uaxis)
				
				
				#unit vector in u direction
				unit_vector_in_u_direction=[0 for ac in range(0,3)]
				unit_vector_in_u_direction[0]=uaxis[0]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[1]=uaxis[1]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				unit_vector_in_u_direction[2]=uaxis[2]/math.sqrt  (( uaxis[0]*uaxis[0]  + uaxis[1]*uaxis[1]  + uaxis[2]*uaxis[2]  ))
				
				
				
				
				
				
				
				#calculating vup
				vup_axis_for_up_and_down[i][0]=zaxis[1]*uaxis[2]-zaxis[2]*uaxis[1]
				vup_axis_for_up_and_down[i][1]=zaxis[2]*uaxis[0]-zaxis[0]*uaxis[2]
				vup_axis_for_up_and_down[i][2]=zaxis[0]*uaxis[1]-zaxis[1]*uaxis[0]
				vup_axis_for_up_and_down[i][0]=vup_axis_for_up_and_down[i][0]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				vup_axis_for_up_and_down[i][1]=vup_axis_for_up_and_down[i][1]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				vup_axis_for_up_and_down[i][2]=vup_axis_for_up_and_down[i][2]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				#if i==0:
				#	print('---vup_axis_for_up_and_down[i]--')
				#	print(vup_axis_for_up_and_down[i])
				
				
				
				
				#unit vector in vup_axis_for_up_and_down[i] direction
				unit_vector_in_vup_axis_direction=[0 for ac in range(0,3)]
				unit_vector_in_vup_axis_direction[0]=vup_axis_for_up_and_down[i][0]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				unit_vector_in_vup_axis_direction[1]=vup_axis_for_up_and_down[i][1]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				unit_vector_in_vup_axis_direction[2]=vup_axis_for_up_and_down[i][2]/math.sqrt  (( vup_axis_for_up_and_down[i][0]*vup_axis_for_up_and_down[i][0]  + vup_axis_for_up_and_down[i][1]*vup_axis_for_up_and_down[i][1]  + vup_axis_for_up_and_down[i][2]*vup_axis_for_up_and_down[i][2]  ))
				#if i==0:
				#	print('---vunit_vector_in_vup_axis_for_up_and_down[i]_direction--')
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction)
				
				
				
	
				#noew camera location after movement in u direction
				camera_eye[i][0]=(unit_vector_in_vup_axis_direction[0]*distance)+ camera_eye[i][0]
				camera_eye[i][1]=(unit_vector_in_vup_axis_direction[1]*distance)+ camera_eye[i][1]
				camera_eye[i][2]=(unit_vector_in_vup_axis_direction[2]*distance)+ camera_eye[i][2]
				#print('--camera_eye---')
				#print(camera_eye[i])
				#if i==0:
				#	print(camera_eye[i])
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction[0])
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction[1])
				#	print(unit_vector_in_vup_axis_for_up_and_down[i]_direction[2])
				#	print('----------------------------------------------------------------------------')
			display()
		

def operations(Key, MouseX, MouseY):
		global camera_vup
		global camera_eye
		global camera_look
		global total_camera_count_ai
		global filename
		if Key == 'x': 
			glMatrixMode(GL_MODELVIEW);
			glRotatef(5,1,0,0)
			display()
		if Key == 'X':
			glMatrixMode(GL_MODELVIEW);
			glRotatef(-5,1,0,0)
			display()
		if Key == 'y': 
			glMatrixMode(GL_MODELVIEW);
			glRotatef(5,0,1,0)
			display()
		if Key == 'Y':
			glMatrixMode(GL_MODELVIEW);
			glRotatef(-5,0,1,0)
			display()
		if Key == 'z': 
			glMatrixMode(GL_MODELVIEW);
			glRotatef(5,0,0,1)
			display()
		if Key == 'Z':
			glMatrixMode(GL_MODELVIEW);
			glRotatef(-5,0,0,1)
			display()	
		if Key == 's':
			glMatrixMode(GL_MODELVIEW);
			glScalef(1.05,1.05,1.05)
			display()	
		if Key == 'S':
			glMatrixMode(GL_MODELVIEW);
			glScalef((1/1.05),(1/1.05),(1/1.05))
			display()	
		if Key == 'f':
			for i in range(0,total_camera_count_ai+1):
				#print('--camera---')
				#print( camera_eye[i])
				
				#print( camera_look[i])
				subtracted_look=[0 for j in range(0,3)]
				subtracted_look[0]=camera_look[i][0]-camera_eye[i][0]
				subtracted_look[1]=camera_look[i][1]-camera_eye[i][1]
				subtracted_look[2]=camera_look[i][2]-camera_eye[i][2]
				#print( subtracted_look)
				#if i==3:
				#	print('--substracted_look---')
				#	print(subtracted_look)
				
				
				
				
				unit_vector_in_eye_direction=[0 for k in range(0,3)]
				unit_vector_in_eye_direction[0]=-1*subtracted_look[0]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[1]=-1*subtracted_look[1]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[2]=-1*subtracted_look[2]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				#if i==3:
				#	print('--unit_vector---')
				#	print(unit_vector_in_eye_direction)
				
				
				
				
				#print(( camera_eye[i][0]*camera_eye[i][0]  + camera_eye[i][1]*camera_eye[i][1]  + camera_eye[i][2]*camera_eye[i][2]  ))
			
				distance=  math.sqrt ( subtracted_look[0]*subtracted_look[0]  +  subtracted_look[1]*subtracted_look[1]  +  subtracted_look[2]*subtracted_look[2]  ) 
				#if i==3:
				#	print('--distance---')
				#	print(distance)
				
				distance=distance*0.95
				#print('-------)-')
				#print(distance)
				#if i==3:
				#	print('--new_distance---')
				#	print(distance)
				
				
				#now adding new distance in unit vector direction
				camera_eye[i][0]=(unit_vector_in_eye_direction[0]*distance)+ camera_look[i][0]
				camera_eye[i][1]=(unit_vector_in_eye_direction[1]*distance)+ camera_look[i][1]
				camera_eye[i][2]=(unit_vector_in_eye_direction[2]*distance)+ camera_look[i][2]
				#if i==3:
				#	print('--camera_eye---')
				#	print(camera_eye[i])
				
			display()
		if Key == 'b':
			for i in range(0,total_camera_count_ai+1):
				#print('--camera---')
				#print( camera_eye[i])
				
				#print( camera_look[i])
				subtracted_look=[0 for j in range(0,3)]
				subtracted_look[0]=camera_look[i][0]-camera_eye[i][0]
				subtracted_look[1]=camera_look[i][1]-camera_eye[i][1]
				subtracted_look[2]=camera_look[i][2]-camera_eye[i][2]
				#print( subtracted_look)
				
				unit_vector_in_eye_direction=[0 for k in range(0,3)]
				unit_vector_in_eye_direction[0]=-1*subtracted_look[0]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[1]=-1*subtracted_look[1]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				unit_vector_in_eye_direction[2]=-1*subtracted_look[2]/math.sqrt  (( subtracted_look[0]*subtracted_look[0]  + subtracted_look[1]*subtracted_look[1]  + subtracted_look[2]*subtracted_look[2]  ))
				
				#print(( camera_eye[i][0]*camera_eye[i][0]  + camera_eye[i][1]*camera_eye[i][1]  + camera_eye[i][2]*camera_eye[i][2]  ))
			
				distance=  math.sqrt ( subtracted_look[0]*subtracted_look[0]  +  subtracted_look[1]*subtracted_look[1]  +  subtracted_look[2]*subtracted_look[2]  ) 
				#print(distance)
				distance=distance*22/21
				#print('-------)-')
				#print(distance)
				
				
				#now adding new distance in unit vector direction
				camera_eye[i][0]=(unit_vector_in_eye_direction[0]*distance)+ camera_look[i][0]
				camera_eye[i][1]=(unit_vector_in_eye_direction[1]*distance)+ camera_look[i][1]
				camera_eye[i][2]=(unit_vector_in_eye_direction[2]*distance)+ camera_look[i][2]
				#if i==3:
				#	print('--camera_eye---')
				#	print(camera_eye[i])
				
			display()
		if Key == 'p':
			for q in range(0,total_camera_count_ai+1):
				
				if(camera_type[q]=='parallel'):
					camera_type[q]='perspective'
				else:
					if(camera_type[q]=='perspective'):
						camera_type[q]='parallel'
				
			display()
		if Key == 'n': 
			print "Enter a file name:",
			filename = raw_input()
			print('loading %s'%filename)
			print('Switch to opengl Window and hit d to load your file')
		if Key=='d'	:
			read_cameratxt_file()
			glMatrixMode(GL_MODELVIEW);
			glLoadIdentity()
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			#matrix=glGetFloatv (GL_MODELVIEW_MATRIX);
			#print(matrix)
			#matrix=glGetFloatv (GL_PROJECTION_MATRIX);
			#print(matrix)
			read_cameratxt_file()
			read_input_file()
			create_pyramid()
			display()
		
		
			
		
read_cameratxt_file()
read_input_file()	
main()
