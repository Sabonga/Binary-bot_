
# import time ,json
# from datetime import datetime
# from dateutil import tz
# from iqoptionapi.stable_api import IQ_Option

# import sys 


# go=IQ_Option("Email","Password")

# go.connect()#connect to go
# go.change_balance('REAL')


# pair ='NZDUSD'
# pair ='EURUSD-OTC' #type OTC
# pair ='EURGBP'
# pair ='AUDCAD'
# pair ='EURJPY'

# size =60
# time_frm =2
# maxdict = 1
# go.start_candles_stream(pair,size,maxdict)

# def mali_yam():
#     return go.get_balance()



# amount =1
#We split the current balance
# amount=float(mali_yam())
#balance data 
# def tshintsi_yam():
#     print("Your balance is   ",amount)
#     print("Please load your account now______ :")
#     choice =input(" choise to reset or exit the bot _________: ")
#     if choice=="y" or choice=="Y" or choice =="yes":
#         go.reset_practice_balance()
#         print("balance upraded" ,mali_yam())
        
#     if choice =="no" or choice=="n":
#         sys.exit()

# if amount == 0:
    # tshintsi_yam()   
    
   
    

# else :
    # print("Please wait while we locate your information .... ..")
    # time.sleep(50)

# while True :

    # storage_data = go.get_realtime_candles(pair,size)
    # print("Recieving data :" ,  storage_data)

  
    # time.sleep()
    # for stored_data in list(storage_data.keys()):
        
    #     open_=(storage_data[stored_data]['open'])
    #     close=(storage_data[stored_data]['close'])
    #     low=(storage_data[stored_data]['min'])
    #     volume=(storage_data[stored_data]['volume'])
    #     high=(storage_data[stored_data]['max'])

    #     print("###################################")
    #     print("###  ##" +' '+ pair +' '+" #######  #####  ######  ####")
    #     print("###################################")
    #     print("Recieving  open data :" ,open_)
    #     print("Recieving low data :" ,low)
    #     print("Recieving high data :" ,high)
    #     print("Recieving close data :" ,close)
    #     print("Recieving volume data :" ,volume)
    #     print("############### HACKING THE SERVERS  PLEASE WAIT ......####################")
   
        # time.sleep()
        #IN RANDS currency
        # rate =float(15.15)
        # in_rands = mali_yam()*rate 
         
       

      
    
       
        #         if open_ < close     :
        #             # time.sleep(0)
        #             if open_ < close     :
        #                 print("In for R", amount*rate)
        #                 trade_="CALL"
        #                 go.buy(amount,pair,trade_,time_frm)
        #                 print("  down >>>   going for " ,trade_)
        #                 print("balance is now R",round(mali_yam()*rate,2))        
        #                 print("###############  DONE ... ......####################")
        #                 print("############### SAYA_MANOWA ......####################")
        #                 sys.exit()


        
        #         if open_ > close    :
        #             time.sleep(30)
        #             print("In for R", round(amount*rate,2))
        #             trade_="PUT"
        #             go.buy(amount,pair,trade_,time_frm)
        #             print("up >>>   going for " ,trade_)
        #             print("balance is now R",round(mali_yam()*rate,2))        
        #             print("###############  DONE ... ......####################")
        #             print("############### SAYA_MANOWA ......####################")
        #             sys.exit()
                    # break

            

       



    






