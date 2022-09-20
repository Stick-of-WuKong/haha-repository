'''
Author: yhh
Date: 2022-09-19 10:10:34
LastEditTime: 2022-09-19 15:15:15
LastEditors: yhh
Description: 
FilePath: \PythonFile\week5.py
yhh
'''
class Lift():
    cus_card = ['Admin Card','Guest Card','Cleaner Card','Operator Card']

    def check_card(self,card):
        pass

class Passenger_Lift(Lift):
    def check_card(self,card):
        if(card.show_card()=='Operator Card'):
            return -1
        return 0
    def check_floor(self,card,floor):
        if(floor == card.floor_num or floor == 1 or floor ==-1):
            return 0
        else:
            return -1
            
class Cargo_Lift(Lift):
     def check_card(self,card):
        if(card.show_card() == 'Guest Card'):
            return -1
        elif(card.show_card() == 'Cleaner Card'):
            return -1
        elif(card.show_card() == 'Guest Card'):
            return -1
        return 0

class Card():
    cus_card = ['Admin Card','Guest Card','Cleaner Card','Operator Card']
    
    def __init__(self) -> None:
        self.floor_num = 0

    def set_card(self,card_str:str):
        if(card_str in ['1','2','3','4']):
            card_num = int(card_str) - 1
            self.card_str = self.__class__.cus_card[card_num]
            if(card_str=='2'):
                floor_num = input('Please input the floor num you are in:')
                if(int(floor_num) in [1,2,3,4,5,6,7,8,9,10]):
                    self.floor_num = int(floor_num)
                else:
                    print('Input Error! Please input again!')
                    print('====================================================')

                    return 1
            return 0
        else:
            print('Input Error! Please input again!')
            print('====================================================')

            return 1

    def show_card(self):
        return self.card_str

    def show_floor(self):
        return self.floor_num

class Hotel():
    cus_card = ['Admin Card','Guest Card','Cleaner Card','Operator Card']

    def first_menu(self):
        while 1:
            for i in range(4):
                print(f'{i+1}.Get {self.__class__.cus_card[i]}')
            print('q to exit')
            
            card_num = input('Input number:') 
            print('====================================================')

            if(card_num=='q'):
                return
            self.card = Card()
            while(self.card.set_card(card_num)):
                card_num = input('Input number:')
            #self.card.set_card(card_num)
            self.second_menu(self.card.show_floor())
        

    def second_menu(self,command=0):

        while(True):
            print('1.Take the passenger lift')  
            print('2.Take the freight lift')  
            print('q to exit')

            num = input('Input the number:')
            print('====================================================')

            if(num=='q'):
                return
            if(num == '1'):
                passenger_lift = Passenger_Lift()
                if(passenger_lift.check_card(self.card)):
                    print('You are not permitted to take this lift!')
                    print('====================================================')
                    continue
                self.third_menu(command)
            elif(num=='2'):
                cargo_lift = Cargo_Lift()
                if(cargo_lift.check_card(self.card)):
                    print('You are not permitted to take this lift!')
                    print('====================================================')
                    continue
                self.third_menu()
            else:
                print('Input Error! Please input again!')
                print('====================================================')



    def third_menu(self,command=0):
        self.current_floor = 1
        while(True):
            print('1.Which floor am I on now')
            print('2.Choose a floor in [-1,1,2,3,4,5,6,7,8,9,10] to go')
            print('q to exit')
            num = input('Input the choice:')
            print('====================================================')

            if(num=='q'):
                return
            if(num == '1'):
                self.show_floor()
            elif(num == '2'):
                floor = input('Input the floor I want to go:')
                if(floor.isdigit() and int(floor) in [-1,1,2,3,4,5,6,7,8,9,10]):
                    if(command!=0):
                        if(int(floor)!=command):
                            print('Can\'t go to other floor')
                            print('====================================================')

                            continue
                    self.go_to_floor(floor)
                    return 
                else:
                    print('Input Error!')
                    print('====================================================')

                
            else:
                print('Input Error! Please input again!')
                print('====================================================')
            

    def go_to_floor(self,num):
        if(num.isdigit()):
            if(int(num) in [-1,1,2,3,4,5,6,7,8,9,10]):
                self.current_floor = int(num)
                print('You are now in floor:'+ num)
                print('====================================================')
            else:
                print('Input Error!')
                print('====================================================')

        else:
            print('Input Error!')
    def show_floor(self):
        print('You are now in floor :'+ str(self.current_floor))
        print('====================================================')


hotel = Hotel()
hotel.first_menu()