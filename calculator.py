# A BASIC CALCULATOR USING pygtk
import gtk
class GUI:
	def __init__(self):
		#initialising all widgets
		self.window=gtk.Window()
		self.button1=gtk.Button('1')
		self.button2=gtk.Button('2')
		self.button3=gtk.Button('3')
		self.button4=gtk.Button('4')
		self.button5=gtk.Button('5')
		self.button6=gtk.Button('6')
		self.button7=gtk.Button('7')
		self.button8=gtk.Button('8')
		self.button9=gtk.Button('9')
		self.button0=gtk.Button('0')
		self.button_1=gtk.Button('+')
		self.button_2=gtk.Button('-')
		self.button_3=gtk.Button('*')
		self.button_4=gtk.Button('/')
		self.button_5=gtk.Button('.')
		self.button_6=gtk.Button('%')
		self.button_7=gtk.Button('C')
		self.button_8=gtk.Button('=')
		self.hbox1=gtk.HBox()
		self.hbox2=gtk.HBox()
		self.hbox3=gtk.HBox()
		self.hbox4=gtk.HBox()
		self.hbox5=gtk.HBox()
		self.hbox6=gtk.HBox()
		self.vbox=gtk.VBox()
		self.textbox=gtk.Entry(max=20)
				
		self.window.add(self.vbox)#adding vertical box to window...all the widgets are subclasses of this vertical box
		self.vbox.add(self.textbox) #adding the text entry widget to vertical box
		self.vbox.add(self.hbox1) #adding horizontal box to vertical box to add the 1st row of buttons
		#adding buttons 1 2 3 to that horizontal box
		self.hbox1.pack_start(self.button1) 
		self.hbox1.pack_start(self.button2)
		self.hbox1.pack_start(self.button3)
		
		self.vbox.add(self.hbox2)#adding another horizontal box for 2nd row of buttons
		#adding buttons 4 5 6 to this horizontal box
		self.hbox2.pack_start(self.button4)
		self.hbox2.pack_start(self.button5)
		self.hbox2.pack_start(self.button6)
		
		self.vbox.add(self.hbox3)#adding another horizontal box for the 3rd row of buttons
		#adding buttons 7 8 9 to this horizontal box
		self.hbox3.pack_start(self.button7)
		self.hbox3.pack_start(self.button8)
		self.hbox3.pack_start(self.button9)
		
		self.vbox.add(self.hbox4)#adding another horizontal box to the vertical box for 4th row of buttons
		#adding button 0 + - to this horizontal box
		self.hbox4.pack_start(self.button0)
		self.hbox4.pack_start(self.button_1)
		self.hbox4.pack_start(self.button_2)
				
		self.vbox.add(self.hbox5)#adding another horizontal box to the vertical box for 5th row of buttons
		#adding buttons * / =
		self.hbox5.add(self.button_3)
		self.hbox5.add(self.button_4)
		self.hbox5.add(self.button_5)
		
		self.vbox.add(self.hbox6)
		self.hbox6.pack_start(self.button_6)
		self.hbox6.pack_start(self.button_7)
		self.hbox6.pack_start(self.button_8)
		
		#setting dimensions of widget..dont worry abt these
		self.window.set_size_request(250, 250)
		#self.button_5.set_size_request(15,15)
		#self.button_4.set_size_request(15,15)
		#self.button_3.set_size_request(15,15)
		#self.window.set_border_width(5)
		self.button1.set_border_width(1)
		self.button2.set_border_width(1)
		self.button3.set_border_width(1)
		self.button4.set_border_width(1)
		self.button5.set_border_width(1)
		self.button6.set_border_width(1)
		self.button7.set_border_width(1)
		self.button8.set_border_width(1)
		self.button9.set_border_width(1)
		self.button0.set_border_width(1)
		self.button_1.set_border_width(1)
		self.button_2.set_border_width(1)
		self.button_3.set_border_width(1)
		self.button_4.set_border_width(1)
		self.button_5.set_border_width(1)
		self.button_6.set_border_width(1)
		self.button_7.set_border_width(1)
		self.button_8.set_border_width(1)
		
		self.window.set_title("CALCULATOR")#setting a title for the window
		#connecting singals to corresponding functions
	  	self.window.connect("destroy",self.destroy)
	  	self.button1.connect("clicked",self.num,"1")
	  	self.button2.connect("clicked",self.num,"2")
	  	self.button3.connect("clicked",self.num,"3")
	  	self.button4.connect("clicked",self.num,"4")
	  	self.button5.connect("clicked",self.num,"5")
	  	self.button6.connect("clicked",self.num,"6")
	  	self.button7.connect("clicked",self.num,"7")
	  	self.button8.connect("clicked",self.num,"8")
	  	self.button9.connect("clicked",self.num,"9")
	  	self.button0.connect("clicked",self.num,"0")
	  	self.button_1.connect("clicked",self.calc,"+")
	  	self.button_2.connect("clicked",self.calc,"-")
	  	self.button_3.connect("clicked",self.calc,"*")
	  	self.button_4.connect("clicked",self.calc,"/")
	  	self.button_5.connect("clicked",self.num,".")
	  	self.button_6.connect("clicked",self.calc,"%")
	  	self.button_7.connect("clicked",self.calc,"C")
	  	self.button_8.connect("clicked",self.calc,"=")
		
		#finally showing all widgets..it is must..otherwise the GUI wont show up
		self.hbox1.show()
		self.hbox2.show()
		self.hbox3.show()
		self.hbox4.show()
		self.hbox5.show()
		self.hbox6.show()
		self.vbox.show()
		self.button1.show()
		self.button2.show()
		self.button3.show()
		self.button4.show()
		self.button5.show()
		self.button6.show()
		self.button7.show()
		self.button8.show()
		self.button9.show()
		self.button0.show()
		self.button_1.show()
		self.button_2.show()
		self.button_3.show()
		self.button_4.show()
		self.button_5.show()
		self.button_6.show()
		self.button_7.show()
		self.button_8.show()
		#self.button_5.show()
		self.textbox.show()
		self.window.show()#it is recommended to show the window atlast so that all the widget will appear the same time
		
	#functions for closing the application when the close button is pressed	
	def destroy(self, button): 
	  	button.hide()
	  	gtk.main_quit()	

	#function executed when the operands are pressed
	def num(self,button,n):
		
		self.textbox.insert_text(n,position=20)
	#functions executed when the operators are pressed	
	def calc(self,button,sign):
		
		if sign=="+":
		    	self.memory=1#making note of operator which is pressed
		    	self.sum1=self.textbox.get_text()#acquiring the numbers in the textentry widget
		    	self.textbox.set_text("")#clearing the textentry widget
		if sign=="-":
		     	self.memory=2                   #same as above
		     	self.sum1=self.textbox.get_text()
		     	self.textbox.set_text("")
		if sign=="*":
		     	self.memory=3                    #same as above
		     	self.sum1=self.textbox.get_text()
		     	self.textbox.set_text("")
		if sign=="/":
		    	self.memory=4                    #same as above
		    	self.sum1=self.textbox.get_text()
		    	self.textbox.set_text("")
		if sign=='%':
			    self.memory=5
			    self.sum1=self.textbox.get_text()
			    self.textbox.set_text("")  
		if sign=='C':
			    self.textbox.set_text("")	      	
		    		
		if sign =="=":   #below set of lines are executed when the = operator is pressed
			sum2=self.textbox.get_text() #acquiring numbers from the textentry widget (it is in string type)
			sum=float(self.sum1) #converting the numbers(in string format) obtained earlier in the code into integer 
			sum2=float(sum2) # converting the numbers in string format to integer format
			if self.memory==1:
				result=sum+sum2    # # #                                  # # #
			if self.memory==2:     #                                          #
				result=sum-sum2    #      Doing corresponding operations      # 
			if self.memory==3:     #                                          #
				result=sum*sum2    # # #                                  # # #
			if self.memory==4:
				result=sum/sum2
			if self.memory==5:
				sum=int(sum)
				sum2=int(sum2)
				result=sum%sum2				
			result=str(result) # converting the result to string format inorder to display it
			self.textbox.set_text(result) #sending the result to the textentry widget	    		 
		    		
				
					 
		
if __name__=='__main__':
	GUI()
	gtk.main()
			
